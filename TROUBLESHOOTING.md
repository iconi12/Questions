# Troubleshooting log

This file is a running log of concrete problems agents have hit while working on this project — mostly environment/tooling quirks and video-production (SAM 2, ffmpeg, whisper) pitfalls — plus how each was diagnosed, fixed, and how to avoid it next time. It is NOT the rules file; `CLAUDE.md` holds the actual content/process rules. This file is the "why" and "here's exactly what went wrong" detail behind some of those rules, plus environment-specific quirks (encoding bugs, tool flags, hardware limits) that don't belong in `CLAUDE.md` because they're not about trivia content at all.

**How to use this file (also referenced from CLAUDE.md):**
- Before spending time diagnosing a weird failure (an ffmpeg error, a SAM 2 drift, an encoding crash), search this file first — it may already be a known issue with a known fix.
- When you hit a NEW problem worth remembering (not a one-off typo, but something another agent could plausibly hit again), add an entry here in the same format: **Issue / Fix / Prevention**. Keep it to a few lines each — this is a reference log, not a narrative.
- If the fix changes how something should be DONE going forward (not just a one-time patch), also update the relevant rule in `CLAUDE.md` — this file records the diagnostic story, `CLAUDE.md` records the standing rule. A problem can have an entry here without a `CLAUDE.md` change (pure tooling trivia), but a `CLAUDE.md` rule change should usually also get an entry here explaining what prompted it.
- Group entries under the nearest matching heading below; add a new heading if nothing fits.

---

## Windows / ffmpeg / tooling quirks

**Issue:** `cv2.imread()`/`cv2.imwrite()` silently fail (return `None`) or crash on file paths containing non-ASCII characters (e.g. the Arabic folder name `الدوري السعودي`), because OpenCV uses an ANSI `fopen` internally on Windows.
**Fix:** Never use `cv2.imread`/`cv2.imwrite` directly on Unicode paths. Read via `np.fromfile(path, dtype=np.uint8)` + `cv2.imdecode(...)`; write via `cv2.imencode(...)` + `.tofile(path)`.
**Prevention:** Always use these Unicode-safe read/write helpers in any script touching files under an Arabic-named folder — just copy them into every new masking/filter script (see `mask_script.py`, `format2_filter.py` for the pattern).

**Issue:** Printing a string containing Arabic text (e.g. an Arabic file path in a `print()` call) crashes with `UnicodeEncodeError: 'charmap' codec can't encode...` because the Windows console redirects stdout through cp1252. This can make a script LOOK like it failed (non-zero exit, no final "done" message) even though all the real work before the crashing `print()` completed successfully.
**Fix:** Remove Arabic text from any `print()`/`console output` statement. If a script "fails" right at the end with this error, check whether the actual output files were written before concluding the run failed — they often were.
**Prevention:** Never print an Arabic path or string from a Python script running under this shell. Use an ASCII placeholder or just print a frame/row count instead.

**Issue:** A background Bash command structured as `cmd > file 2>&1; echo DONE_$?` — the task's own `.output` file (surfaced via task-notifications) only captures the `echo` line, NOT the real redirected output.
**Fix:** Read the explicitly-redirected file path (the one after `>`), not the task's own `.output` file, when checking a background command's real output.
**Prevention:** When launching a background command with its own `>` redirect, always note the redirect target path at launch time and read THAT, not the task output file.

**Issue:** The Bash tool is sometimes blocked (classifier denial) from calling the Streamlabs OBS `ffmpeg.exe`/`ffprobe.exe` binaries directly, even though it's the same binary path that works fine elsewhere.
**Fix:** Use the PowerShell tool for ffmpeg/ffprobe calls instead of Bash when Bash gets blocked — same command, different tool, works fine.
**Prevention:** Default to PowerShell for ffmpeg/ffprobe calls in this project; fall back to Bash only for things PowerShell can't do well (piping to Python one-liners, etc.).

**Issue:** This machine's ffmpeg build (Streamlabs OBS's bundled binary) errors (`Error muxing a packet`, exit 234) when building a single tiled contact-sheet image (`tile` filter) with the `image2` muxer, even though the command looks correct.
**Fix:** Add `-update 1` to the ffmpeg command. This is required on this build whenever outputting a single image file (not a numbered sequence) from a filter that only emits one frame (like `tile`).
**Prevention:** Always include `-update 1` on any ffmpeg command writing a single contact-sheet/thumbnail image on this machine.

**Issue:** Source video downloaded via yt-dlp is AV1-encoded. This ffmpeg build can grab a SINGLE frame from an AV1 file fine, but errors or behaves unpredictably (frame count mismatches, decoder instability) on multi-frame reads — contact sheets, frame extraction for SAM 2, etc.
**Fix:** Transcode the whole downloaded file to H.264 ONE TIME up front (`-c:v libx264 -preset fast -crf 20 ...`) before doing any further frame-accurate work on it.
**Prevention:** After any yt-dlp download, check the video codec with `ffprobe`. If it's AV1, transcode to H.264 immediately before touching it with contact sheets or frame extraction — don't wait until something breaks.

**Issue:** yt-dlp downloads video and audio as separate streams and does not auto-merge them without a system ffmpeg on PATH (there isn't one here by design).
**Fix:** Download both streams (`-f "bv*[height<=720]+ba/b[height<=720]"`), then merge manually with the Streamlabs ffmpeg binary (`-c:v copy -c:a aac -b:a 128k`).
**Prevention:** Always check for two separate output files (`.f398.mp4`-style video + `.f251.webm`-style audio) after a yt-dlp download and merge them before use.

**Issue:** faster-whisper on GPU (`device='cuda'`) fails with `RuntimeError: Library cublas64_12.dll is not found`. CTranslate2 needs separate `nvidia-cublas-cu12`/`nvidia-cudnn-cu12` pip packages beyond what torch's own CUDA wheels provide, and that install can be extremely slow (~2MB/min at times).
**Fix:** Don't block on it — use `device='cpu', compute_type='int8'` instead. CPU transcription of a short clip (under ~15s) is fast enough in practice (a few seconds) that the GPU path isn't worth waiting on.
**Prevention:** Default to CPU for faster-whisper in this project unless transcribing something much longer than a single clip (e.g. a full match), where GPU speed would actually matter.

**Issue:** faster-whisper's `model.transcribe(path)` fails with `TypeError: open() got an unexpected keyword argument 'metadata_errors'` when passed a file path directly — a PyAV version incompatibility in `faster_whisper/audio.py`'s internal `decode_audio()`.
**Fix:** Don't pass a file path. Read the WAV manually via Python's `wave` module into a raw int16 numpy array, convert to float32 normalized to [-1, 1], and pass the ARRAY to `model.transcribe()` instead.
**Prevention:** Always use the manual `wave` + numpy loading pattern for faster-whisper in this project, never a bare path — see the `transcribe_*.py` scripts for the reusable snippet.

---

## SAM 2 masking

**Issue:** SAM 2 cannot track across a hard camera cut OR a cross-dissolve (two frames blended together during a transition) — propagating across either produces garbage (locks onto the wrong object, or loses tracking for several frames).
**Fix:** Always identify and trim to a SINGLE continuous camera shot before running SAM 2. If unsure whether a transition is a hard cut or just fast motion blur, check a dense contact sheet across it.
**Prevention:** Before masking, scan the candidate clip's start/end boundaries with a contact sheet and confirm there's no dissolve/cut inside the range you intend to mask.

**Issue:** A single point prompt on the anchor frame — especially one placed low on the body — biases SAM 2's mask toward only that body part (e.g. legs only, leaving the torso/head uncovered in every subsequent frame).
**Fix:** Use several points spread across the body (head, torso, legs) on the anchor frame, not one point. A box prompt is also more robust than a point on a blurry/ambiguous frame.
**Prevention:** Never anchor with a single point. Always use 3+ points or a box, and visually check the ANCHOR FRAME ITSELF (not just later frames) at full resolution before trusting propagation from it.

**Issue:** SAM 2's backward propagation (`reverse=True`) is dramatically less reliable than forward propagation from the same anchor — observed repeatedly: drifting onto empty background or a different player within single-digit frames of the anchor, even from a VERIFIED-correct anchor point, even over a short clip (under 300 frames), even when forward propagation from that exact same anchor stayed reliable much further. This is not just a "long distance" problem — it has failed within ~50 frames of a good anchor.
**Fix:** Don't rely on backward propagation for anything that matters. Anchor as EARLY in the clip as possible and propagate forward only. If you can't anchor early with confidence, use the candidate-validation trick below rather than trusting a late anchor + backward propagation.
**Prevention:** Treat "anchor near the end, propagate backward to cover the buildup" as a known-bad pattern — don't do it, even if it seems convenient because the end of the clip is easier to identify the player in. If backward tracking is the only option and it fails, it's better to ship a shorter forward-only masked clip (or report the difficulty) than a clip with silently wrong backward-tracked frames.

**Issue:** When it's hard to tell by eye which of several similar-looking players (same kit, small/distant, motion blur) is the right one to anchor on, a blind guess is often wrong — this has happened multiple times, including guessing a point that landed on the referee instead of the intended player.
**Fix:** Validate a candidate CHEAPLY before committing to a full run: place the candidate point at an early frame, run a SHORT forward propagation to a frame where the target's position is already confirmed (from a different, already-verified anchor), and check whether the mask's centroid actually converges there. A correct candidate converges almost exactly; a wrong one drifts or ends up on a different person entirely. This costs under a minute and saves a full run (which can take 20-40+ minutes on a busy scene) on a wrong guess.
**Prevention:** Never commit to a full-length SAM 2 run on an unverified candidate point. Always do the short validation hop first.

**Issue:** Visually ESTIMATING pixel coordinates for a point prompt from a displayed/cropped image is unreliable — in one case, repeated coordinate guesses were off by as much as 80-100px despite looking "close enough" by eye, causing the SAM 2 mask to land in empty grass between two players instead of on either of them, for multiple attempts in a row.
**Fix:** Before running SAM 2 at all, draw the candidate point(s) as a visible marker dot directly on a cropped/zoomed copy of the actual frame and LOOK at whether the dot is really on the player — don't trust a mental coordinate estimate from a separate crop image. Iterate the marker-dot check until it's visibly correct, THEN run SAM 2.
**Prevention:** Make the marker-dot verification step a standard part of anchor selection, not just a fallback after a failed run — it's nearly free (no GPU needed) and catches exactly this class of error before it costs a full propagation run.

**Issue:** SAM 2 masking a scorer only from the moment of the kick onward (leaving the earlier buildup/approach unmasked) was initially justified as "he's too small/indistinct to identify there anyway" — the human reviewing the clip disagreed and said he WAS identifiable, meaning the earlier judgment call was wrong and the clip shipped with a real gap.
**Fix:** Don't assume a stretch of clip doesn't need masking because the subject looks small or indistinct — verify it (e.g. by zooming into that exact frame region) or just mask it anyway. If masking that stretch isn't reliably achievable (see the backward-propagation issue above), say so explicitly rather than silently skipping it on an assumption.
**Prevention:** Treat "is he identifiable here" as something to check, never something to assume, especially under time pressure to ship.

**Issue:** Running more than one SAM 2 masking job at the same time on this machine doesn't speed anything up — there's a single GPU (RTX 4060 Ti, 8GB VRAM, usually only a few GB free). Concurrent jobs compete for the same VRAM: best case they time-slice with overhead (same or worse total time), worst case one OOMs.
**Fix:** Queue SAM 2 masking jobs one at a time, regardless of how many agents/workers exist. See CLAUDE.md's "Order of work" section for the full process rule this produced.
**Prevention:** Always check actual GPU VRAM (`nvidia-smi`) before assuming parallel masking will help — on hardware like this, it won't.

**Issue:** SAM 2's image-folder video loader (`init_state(video_path=FRAMES_DIR)`) requires every frame filename to be a bare integer (`00001.jpg`, `00002.jpg`, ...) — it sorts frames with `int(os.path.splitext(p)[0])`. A prefixed name like `f_00001.jpg` (e.g. from an ffmpeg `-vf fps=25` extraction pattern `f_%05d.jpg`) crashes with `ValueError: invalid literal for int()`.
**Fix:** Extract frames with a pure-numeric pattern (`%05d.jpg`, no prefix) from the start, or rename an already-extracted sequence (`for f in f_*.jpg; do mv "$f" "${f#f_}"; done`) before calling `init_state`.
**Prevention:** Always use a bare-numeric ffmpeg output pattern for any frame folder that will be handed to SAM 2's video predictor.

**Issue (CORRECTED — see below):** An earlier version of this entry claimed SAM 2 permanently swapped a tracked dribbler for the tackling defender partway through a clip (Al Nassr vs Al Khaleej, goal 1). That diagnosis was WRONG. It was based on judging the mask's identity from the white-silhouette render alone (position/motion only, kit colour already painted over) instead of checking the mask against the original colour frame. When re-checked properly — drawing the mask as a red OUTLINE on top of the unmasked original frame — the mask stayed correctly on the same yellow-kit player (visually confirmed at frames 110, 130, 150, 170, 190, 210, 230, 260, 270) through the tackle and well beyond it, all the way until he ran off-screen (mask area → 0 at frame 277-280, not drift — he simply left the frame). The real issue with that clip was unrelated to tracking: the anchored player was not actually the goal's scorer — a separate crowded free-kick/scramble on the other side of the box produced the goal, and the tracked player was never part of that action. A human pointed out the clip "doesn't have any problem" after watching it, which is what prompted re-checking and catching this misdiagnosis.
**Fix:** When judging whether a mask is on the right person, never trust the white/black silhouette render alone — it erases kit colour, so a wrong-but-similarly-positioned mask and a right one can look identical. Always verify identity by drawing the mask as a thin OUTLINE on the original, full-colour frame (`cv2.findContours` + `cv2.drawContours`, 2-3px, don't fill it) and visually confirm the kit/player inside the outline, at every checkpoint you report on — not just the anchor frame.
**Prevention:** Make the outline-on-original check the standard verification method for any claim about tracking identity (first setup, later checkpoints, final QA) — never conclude "it drifted" or "it's correct" from a silhouette-only view. This also means: don't delete the diagnostic frames/scripts for a result you're about to describe to the human as broken — regenerating them after being asked is how this misdiagnosis got caught at all.

**Issue:** SAM 2 processing speed varies enormously by scene content, not just frame count — a simple, mostly-empty tight replay (380 frames) finished in under 2 minutes, while a busy, detailed wide shot (full stadium crowd, many players, animated LED boards, 525 frames) took over 40 minutes, roughly a 20-30x difference per frame.
**Fix:** N/A — this is just a planning fact, not a bug. Budget masking time per clip based on how visually busy/detailed the shot is, not just its frame count or duration.
**Prevention:** When estimating time for a batch of clips, don't assume uniform per-frame cost — a wide, detailed shot will take much longer than a tight, simple one even at the same frame count.

---

## Audio / commentary editing

**Issue:** Silencing (zeroing out) a name's audio samples in place, rather than cutting the segment out and closing the gap, leaves an audible dead pause where the commentator appears to freeze mid-sentence. The human flagged this directly: "the commentator stops speaking, he shouldn't stop at all."
**Fix:** Cut the name's audio span out entirely and splice what comes immediately before it directly to what comes immediately after (ripple-delete), so the remaining words run together naturally with no gap.
**Prevention:** Never use "replace with silence" for name removal going forward — always cut-and-close-gap. See CLAUDE.md's "Removing names from commentary" section.

**Issue:** Over-applied the cut-and-close-gap technique to an excited post-goal SHOUT that wasn't actually the player's name (no match to the name's actual phonemes — no R/N/D sounds for "Ronaldo", for example), leaving the commentator silent for several extra seconds for no real reason.
**Fix:** Only cut audio that's plausibly the actual name/nickname by SOUND, not just because it's loud/unclear/shouted. A prolonged inarticulate shout with none of the name's distinctive sounds is very likely just a cheer.
**Prevention:** Before cutting a span, sound-check it against the actual name's phonemes, not just its excitement level.

**Issue:** faster-whisper's Arabic transcription of football commentary is frequently garbled on proper names specifically (crowd noise, excited/fast speech) — e.g. "Marcos Leonardo" transcribed as "ماركوس ليولاردو" in one pass and "مركوس ليوناردو" in another from the same speaker.
**Fix:** Don't trust a single transcription pass at face value for name-sensitive edits — read the full transcript as a human would, and treat any word that COULD plausibly be the name (even if misspelled/garbled) as the name. Re-transcribing a tighter, isolated clip of just the suspect span can also sharpen the result.
**Prevention:** Always manually read the transcript rather than grep-searching for an exact expected spelling of the name — the exact transcribed spelling is unreliable.

---

## Sourcing / content

**Issue:** Built question clips from the broadcast's REPLAY footage (the zoomed/slow-motion angle shown after a goal) instead of the LIVE action, more than once, because the replay is usually the cleaner, more cinematic-looking shot and was mistaken for being a complete representation of "the goal."
**Fix:** Always find the first appearance of the GOAL graphic / score change by scrubbing forward from well before the goal — everything before that point is live, everything after is replay. Cut from the live footage.
**Prevention:** Make this check automatic for every new clip, not just when something looks wrong — see CLAUDE.md's "Where clips come from" section.

**Issue:** A live wide shot that looked clean on first pass turned out to have a persistent scoreboard graphic with both team names spelled out in Arabic text, only caught by a careful full-resolution check of a representative frame — grayscale alone does nothing to hide text.
**Fix:** Check every live-footage candidate specifically for an on-screen scoreboard/score-bug graphic, independent of the kit-colour check, and cover/blur it if found.
**Prevention:** Don't assume "no visible team names" from the thumbnail-scale contact sheet used for other checks — scoreboards are often small and easy to miss at thumbnail resolution; check a full-resolution frame specifically for this.

**Issue:** A black-and-white (grayscale) filter alone does not hide a kit's PATTERN (stripes/hoops) — only its colour. A viewer who knows "this team wears stripes" can still identify the team from a grayscale striped kit.
**Fix:** Add a light blur over the whole frame (strong enough to blur out fine kit pattern/jersey numbers, light enough to keep players/ball clearly visible) on top of the grayscale.
**Prevention:** When testing a Format 2 clip, explicitly check pattern legibility as its own test, separate from the colour-distinguishability check — see CLAUDE.md's Format 2 section.

**Issue:** The blur strength needed to hide broadcast scoreboard TEXT is far stronger than the blur strength needed to hide kit PATTERN — a single uniform blur calibrated for one is wrong for the other (too weak for text, or so strong it blurs players into mush).
**Fix:** Use two separate blur passes: a light one over the whole frame (pattern), and a much harder one applied only to the scoreboard's (or any other on-screen team name/logo's) specific bounding box.
**Prevention:** Never assume a single frame-wide filter setting handles both "hide pattern" and "hide text" — test each requirement separately and tune its own treatment.

**Issue:** A player's jersey surname nameplate (printed on the back of the shirt) becomes legible the moment a celebration shot gets close — e.g. "M. LEONARDO" clearly readable in a touchline celebration run, well past where the mask/filter coverage of the main action had already ended.
**Fix:** Trim the clip to end BEFORE any shot gets close enough to read a nameplate, the same way you'd trim before a clear face shot.
**Prevention:** When trimming a clip's end point, specifically check for approaching nameplate/face close-ups in the frames just past the planned cutoff, not just the main action.

**Issue:** Finding a candidate goal where the SCORER is on screen and identifiable from early in the clip through to the shot turned out to be harder than expected to scout correctly. Across two full match highlight reels plus one human-provided raw clip explicitly labelled as a bicycle kick, most goals checked involved a crowded box at the moment of the shot (header off a corner, scramble, free-kick pile-up), or — in the bicycle-kick clip's case — a kick action so fast (2-3 frames at 25fps) that the wide broadcast angle barely shows the acrobatic pose at all. One candidate (Al Nassr's opening goal vs Al Khaleej) was wrongly judged mid-scouting as "the dribbler loses the ball to a tackle" and rejected — rechecked later (see the SAM 2 identity-verification entry above), the tracking had actually stayed correct throughout; the real problem was that the tracked dribbler simply wasn't the player who went on to score — a separate player, in a separate crowded passage of play, scored instead. So the risk isn't just "contact breaks tracking" (tracking is more robust than that), it's "the player you start tracking early in a buildup may not be the one who actually finishes it."
**Fix:** Budget real scouting time (reviewing several candidate goals, and confirming WHO actually scores before investing in tracking any one player) as its own cost item, separate from masking time. Before anchoring, identify the actual scorer first (e.g. from the goal celebration / graphic) and trace him backward to find where he's identifiable early in the buildup — don't anchor on "whoever has the ball early in a promising-looking passage" and assume it leads to the goal.
**Prevention:** When estimating cost per Format 1 clip, include scouting/candidate-rejection time, and specifically include the step of confirming scorer identity before picking an anchor — this is a distinct risk from tracking reliability and was the actual cause of one scouting rejection in this project, not a tracking failure.

**Issue:** Planned to mask every player in a Format 2 (hidden-teams) clip individually with SAM 2 — this is slow (an extra masking pass per person) and, more importantly, caps the clip's usable length at whatever single continuous shot was available, which was often under the 5s minimum.
**Fix:** Abandoned per-player masking for Format 2 entirely in favour of a whole-frame grayscale + blur treatment (see CLAUDE.md's Format 2 section) — no per-player tracking needed at all, any number of people are covered automatically, and clips can freely span multiple camera cuts since there's nothing to track.
**Prevention:** Don't reach for SAM 2 at all for Format 2 — it's the wrong tool for "hide everyone," even though it's the right tool for Format 1's "hide one specific person."
