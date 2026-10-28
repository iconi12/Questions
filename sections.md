# Sections

Work through the sections in this order. Do not add, rename, or merge sections.
Each section has notes on its scope and special rules — they override the general rules in CLAUDE.md where they conflict.

## Scope boundaries (to avoid duplicates across sections)
- A topic that has its own section belongs ONLY to that section.
- السعودية: excludes Saudi football, dialects, and restaurants (they have their own sections).
- تاريخ: excludes WWI, WWII, السيرة النبوية, and قصص الأنبياء.
- جغرافيا: excludes capitals (they belong to دول و عواصم).
- معلومات عامة: only questions that don't fit any other section.
- سيارات، صراع العروش، هاري بوتر، ون بيس، هجوم العمالقة، ناروتو، بيتر كول ساول، بريكنغ باد، ألعاب الفيديو، إلدن رينغ، ذا بويز، إنفينسبل، مارفل، سيد الخواتم، ديزني وبيكسار، فرندز، سبونج بوب، كول أوف ديوتي بلاك أوبس زومبيز، مسلسلات رمضانية، دريم وركس: their topics belong only to them — no question about any of these in معلومات عامة or any other section, including each other (e.g. no Breaking Bad fact in بيتر كول ساول or vice versa, no Elden Ring fact in ألعاب الفيديو, no DreamWorks film in ديزني وبيكسار or vice versa).
- **سبيستون (section 42) is the one exception to this rule (human, 2026-10-24):** it may overlap with ون بيس، هجوم العمالقة، ناروتو or any other section covering a show that also aired dubbed on the Spacetoon channel. Write the same event/fact in both sections if it fits both — don't delete or avoid it here just because it's also in-scope elsewhere.

---

## 1. السعودية
History, geography, culture, landmarks, Vision 2030, notable facts about Saudi Arabia. Excludes Saudi football, dialects, restaurants, cars and anything else that has its own section (see Scope boundaries above). See CLAUDE.md's Reference examples and Operational heuristics (from the السعودية calibration batches) — this section set the house calibration style every other section follows.

## 2. معلومات عامة
Mixed general knowledge: science, inventions, records, everyday facts. Only questions that don't fit any other section (see Scope boundaries above) — before writing a row here, check whether it actually belongs to one of the other 45 sections; if it could, it belongs there, not here.

## Football sections (3 كاس العالم، 4 الدوري السعودي، 5 الدوري الانجليزي) — shared rules
From the human's review of الدوري السعودي (2026-10-16). Apply to all three football sections.

**Pin the match** (CLAUDE.md Core rule B)
- Two teams meet twice in a league season. Every question about a league match names the leg — ذهاب or إياب — plus the season. Alternatives that also pin it: the date, or the final score.
- Cup and tournament matches: name the round (دور الـ16، نصف النهائي، النهائي...).
- **A pinning score can itself be a leak (lead addition, 2026-10-16).** Before using a final score to pin a match, Grep the section's csv for that score. If another approved row's own answer or note already states that score for a similar matchup (e.g. "which two clubs beat النصر 3-1"), the score gives that answer away — pin by leg/date/round instead. Caught 2026-10-16: a رونالدو row pinned with "بفوز الهلال 3-1" leaked half of a different approved row's answer.

**Section scope** — applies to all three football sections, not just الدوري السعودي
- Each league section (الدوري السعودي، الدوري الانجليزي) is about its OWN league only: that league's matches, clubs, players' seasons in it, titles, scorers, transfers INTO it. كاس العالم is about the tournament itself — its matches, players, records.
- Out of scope for a league section: a player's career, transfers, or matches in any OTHER league or country; a player's national-team appearances; anything that's really about كاس العالم or another competition.
- Out of scope for كاس العالم: anything not about the match/tournament/players/records themselves (e.g. a country's domestic reaction to a result) — see the كاس العالم operational heuristics below.
- Caught 2026-10-16: "من أول لاعب سعودي احترف في أوروبا؟" (سامي الجابر) was rejected for exactly this — a player's foreign pro career has nothing to do with the Saudi league, even though the fact is Saudi-flavored. The same test applies in الدوري الانجليزي to a player's career before/after the Premier League, and in كاس العالم to anything about a player's club career.

**Difficulty — human calibration**
Audience: young Saudis who follow football. In the first review, agents rated far too HIGH — about 35 rows marked 300/500 were really 100. Default lower:
- **100** — what any young fan knows: champions, top scorers, famous signings and transfers, star players' clubs, results of big matches that trended, records everyone talked about.
- **300** — needs following the league closely: the scorer of a specific league match between known clubs (human example: who scored Al-Nassr's goal against Al-Qadsiah in the 2025-26 second leg = 300), a specific match result from a past season, a mid-table detail.
- **500** — almost no fan remembers it: assist makers, the scorer in a match between smaller clubs, the exact minute, substitutes, details from older seasons, second-place or third-place details.
- Ask: "Would a young Saudi who watches the league every week know this without searching?" Yes → 100. Only if they paid close attention → 300. Almost none → 500.
- **Match-scorer 300-vs-500 test (reviewer-dawri, proven over 5 batches, 2026-10-16).** This specific question shape — "who scored for [club] in [match]" — kept getting misjudged; writers kept aiming at "not a star player" instead of the real test, which is about the GOAL's role, not the scorer's fame:
  - **300** — a big-four club's (الهلال، النصر، الاتحاد، الأهلي) ONLY goal, or the DECIDING goal, in a pinned league match, from the 2023-24 season onward.
  - **500** — anything else in this shape: a smaller club's scorer, an own goal, a non-deciding goal in a big win (2nd/3rd goal of a blowout), or a match from 2022-23 or earlier.
  - A star player's name does NOT make a goal 300 by itself — Ronaldo/Talisca/etc. scoring the 2nd goal of a 3-1 win is still 500, because the goal itself is forgettable even if the scorer isn't.
  - **Extra condition: the scorer must not be the club's obvious star/fame guess for that goal (fame-leak test, same principle as كاس العالم's).** If a player's existing fame alone lets a player guess them as "probably who scored" without knowing the actual fact, it's 100, not 300 — e.g. بنزيما for الاتحاد's only goal, or محرز for a 1-0 derby winner. These are the cases the human already marked 100 (rows 268, 272, 276).

## 3. كاس العالم
FIFA World Cup history — men's tournament only (human ruling, 2026-10-15). The FIFA Women's World Cup is out of scope here; no other section covers it either, so exclude it entirely rather than placing it elsewhere. Any question about records or "most ..." must state "up to [year/tournament]".

## 4. الدوري السعودي
Saudi Pro League. Time-sensitive facts must include the season (e.g. "في موسم 2023-2024").
Media filename code: `spl`.

## 5. الدوري الانجليزي
Premier League. Same time-sensitive rule as الدوري السعودي.

**Human-written base batch — frozen (human, 2026-10-16).** Lines 2–152 of `staging/الدوري الانجليزي.csv` (151 rows) are written and approved by the human directly, not by writer/reviewer. They are frozen: writer and reviewer must NOT edit, delete, reword, retier, or re-review them — leave them exactly as they are. They serve as the points/difficulty reference for every new الدوري الانجليزي question going forward (the same role the calibration examples play for other sections) — match their style and judge new rows' 100/300/500 tier against them. New rows are appended after line 152 and go through the normal pipeline.

## 6. دول و عواصم
Countries and capitals, worldwide. For countries with disputed or multiple capitals, either avoid them or state the official one clearly.
- The question asks for a country's capital, or (reversed) which country a named capital belongs to — not other geography facts (جغرافيا, section 23, covers those; this section owns capitals specifically, see Scope boundaries above).
- Difficulty, same 10-Saudi-adults scale: 100 = well-known countries/capitals (own region, major world powers, capitals that match a common assumption). 300 = less common but identifiable with some interest in geography. 500 = small/obscure countries, or a capital that surprises people (not the country's best-known/largest city).

## 7. الحرب العالمية الاولى
World War I (1914–1918): battles, countries and alliances, key figures and leaders, major campaigns, the Middle East/Ottoman front, outcomes and treaties (e.g. سايكس بيكو، معاهدة فرساي). Historical section — Core rule D's era/recency quotas don't apply (see CLAUDE.md's list of historical-section exemptions).

## 8. الحرب العالمية الثانية
World War II (1939–1945): battles, countries and alliances, key figures and leaders, major campaigns and turning points, outcomes. Historical section — Core rule D's era/recency quotas don't apply (see CLAUDE.md's list of historical-section exemptions).

## 9. اعلام
Flags of the world's countries. Two question formats only:
- **Image question**: `question_image` shows the flag (Wikimedia Commons / flagcdn.com), question asks "ما اسم الدولة التي يتبع لها هذا العلم؟" or similar — answer is the country name, no answer image needed.
- **Description question**: the question is a text description of a distinguishing, verifiable detail of the flag (a specific object, exact colors/shapes, a unique feature — e.g. "ما العلم الوحيد الذي يظهر فيه سلاح AK-47؟" → موزمبيق). No `question_image` (that would give it away). Always set `answer_image` to a direct link of that flag, so the host can show it when revealing the answer.
- Difficulty is recognition-based, same 10-Saudi-adults scale: 100 = instantly recognizable flags (own-region, major powers, iconic colors). 300 = less common but still identifiable with some interest in geography/flags. 500 = flags/details almost no one would recognize or know by description alone.
- No duplicate country across the section from a mere color/shape restate of another row's clue — each row's distinguishing detail must be unique to that flag.
- Human ruling (2026-10-14, revised): for flags that are 1-to-1 (or near enough) visually identical to another country's (e.g. Chad/Romania, Indonesia/Monaco, Ireland/Côte d'Ivoire) — COMBINE both formats, don't pick just one. Show the real flag as `question_image` AND include the disambiguating text in the question that names the lookalike (e.g. "ما الدولة الأفريقية التي يكاد علمها يطابق علم رومانيا؟" with Chad's flag shown). Naming the lookalike here is NOT a hint — it's required, because without it the lookalike country would itself be a second valid/defensible answer (the image alone can't rule it out, so the row would violate rule 2's "no X or Y"). Also add a host-only note ruling out the lookalike explicitly (e.g. "لا يُقبل رومانيا"). This replaces the earlier image-only-only ruling for this specific case.
- A combined lookalike row (showing A's flag, naming B) teaches the player B's flag — so B must never get its own separate row in the section.
- Human ruling (2026-10-14): the CLAUDE.md 100-per-tier minimum does NOT apply to this section. There are only ~40 countries whose flag 7+/10 Saudi adults would instantly recognize, nowhere near 100. Write every genuinely good question at each tier (both formats, plus a second row per country allowed when it tests a clearly different, non-overlapping detail, plus organization flags — Olympic, UN, Arab League, GCC — where they fit the format) and stop each tier there. Don't force in weak/miscalibrated rows just to hit a number.
- A second row for a country already covered by an image row only works if it asks something the image can't show (e.g. what an emblem/symbol on the flag means or commemorates) — an image row already reveals every visual detail, so a second description row restating a visible detail leaks the first row's answer.

## 10. الغاز
Riddles. Rules differ from the rest:
- The answer must be the single obvious answer once revealed — no riddles with several valid answers.
- Difficulty is how hard it is to solve, using the same "10 Saudi adults" scale.
- Pass 1 checks the riddle's logic instead of web search.

## 11. الكويت
History, geography, culture, landmarks, notable facts about Kuwait specifically.
- Same Saudi-specific test as السعودية's 2026-10-04 ruling, applied to Kuwait: a heritage/culture item shared across the Gulf stays here only if it's Kuwait-named, Kuwait-promoted by a Kuwaiti institution/campaign, or tied to a Kuwaiti place/region/person named in the question. Generic shared-Gulf culture (already covered from the Saudi side's non-Saudi-specific items in معلومات عامة) does not get rewritten here from a Kuwaiti angle — check معلومات عامة for an existing row on the same cultural item before writing a new one.

## 12. قطر
History, geography, culture, landmarks, notable facts about Qatar specifically.
- Same Saudi-specific test as السعودية's/الكويت's ruling, applied to Qatar: a heritage/culture item shared across the Gulf stays here only if it's Qatar-named, Qatar-promoted by a Qatari institution/campaign, or tied to a Qatari place/region/person named in the question. Generic shared-Gulf culture does not get rewritten here from a Qatari angle — check معلومات عامة for an existing row on the same cultural item first.

## 13. البحرين
History, geography, culture, landmarks, notable facts about Bahrain specifically.
- Same Saudi-specific test as السعودية's/الكويت's ruling, applied to Bahrain: a heritage/culture item shared across the Gulf stays here only if it's Bahrain-named, Bahrain-promoted by a Bahraini institution/campaign, or tied to a Bahraini place/region/person named in the question. Generic shared-Gulf culture does not get rewritten here from a Bahraini angle — check معلومات عامة for an existing row on the same cultural item first.

## 14. الامارات
History, geography, culture, landmarks, notable facts about the UAE specifically.
- Same Saudi-specific test as السعودية's/الكويت's ruling, applied to the UAE: a heritage/culture item shared across the Gulf stays here only if it's UAE-named, UAE-promoted by an Emirati institution/campaign, or tied to an Emirati place/region/person named in the question. Generic shared-Gulf culture does not get rewritten here from an Emirati angle — check معلومات عامة for an existing row on the same cultural item first.

## 15. عمان
History, geography, culture, landmarks, notable facts about Oman specifically.
- Same Saudi-specific test as السعودية's/الكويت's ruling, applied to Oman: a heritage/culture item shared across the Gulf stays here only if it's Oman-named, Oman-promoted by an Omani institution/campaign, or tied to an Omani place/region/person named in the question. Generic shared-Gulf culture does not get rewritten here from an Omani angle — check معلومات عامة for an existing row on the same cultural item first.

## 16. لهجات سعودية
Meanings of Saudi dialect words and expressions only — not Gulf-wide slang shared with other countries (that belongs in معلومات عامة unless it's distinctly Saudi), not other countries' dialects.
- Name the region in the question when the word is regional (e.g. "في اللهجة النجدية").
- Avoid words whose meaning differs between regions unless the region is stated.
- Sources: a recognized dialect dictionary/glossary, or a clearly consistent usage across multiple independent sources — avoid relying on a single anecdotal source for a word's meaning, since dialect meanings get disputed easily.
- Difficulty, same 10-Saudi-adults scale: 100 = words/expressions used and understood nationwide. 300 = regional or generational — understood mainly by people from that region or an older generation. 500 = old-fashioned or highly local words most young Saudis wouldn't recognize unprompted.

## 17. تاريخ
Islamic, Arab, and world history — excludes الحرب العالمية الاولى، الحرب العالمية الثانية، السيرة النبوية، and قصص الأنبياء, which each have their own section (see Scope boundaries above).
- Topics: historical events, figures, dynasties, caliphates, battles, treaties, civilizations — not limited to Saudi/Arab history, but excluding the four sections named above.
- Historical section — Core rule D's era/recency quotas don't apply (see CLAUDE.md's list of historical-section exemptions); a 500 here should be a precise detail of a known event rather than an obscure one almost nobody has heard of.

## 18. عالم الحيوان

## 19. السيرة النبوية
Rules for all religious sections (19–22):
- Only from the Quran and authentic Sunnah (صحيح). No weak or fabricated narrations, no إسرائيليات.
- Write the source in `note` (e.g. "صحيح البخاري 6018" or the surah and ayah).
- Avoid matters of scholarly disagreement.
- Reviewer verifies EVERY question in these sections with search, including 100-point ones.

## 20. اكمل الحديث
The question gives the beginning of a hadith; the answer is its ending.
- Text must match the source wording exactly.
- Authentic hadith only, with collection and number in `note`.

## 21. قصص الانبياء
Same religious rules as section 19.

## 22. معاني القران
Meanings of Quranic words or verses.
- Meanings must come from a recognized tafsir; name it in `note`.
- Quranic text must be exact.

## 23. جغرافيا

## 24. مطاعم السعودية
Well-known Saudi restaurants and chains.
- Restaurants open, close, and change — prefer stable facts (origin city, founding, signature dish).
- Every question is verified with search.

## 25. سيارات
Section code for media filenames: `car`.
Identify the car from media. Every row is one of four formats — no text-only questions:
- **Exterior photo** — `question_image` shows the outside of the car with every brand mark hidden.
- **Interior photo** — `question_image` shows the cabin (dashboard, steering wheel, seats, console) with every brand mark hidden.
- **Sound** — `question_audio` holds a clip of the car (engine, exhaust, start-up). (Note: CLAUDE.md's general video/audio rules deliver audio-only questions as an `.mp4` with a still cover, in `question_video` — follow CLAUDE.md's audio-only build method; `question_audio` here is kept only as the section's own historical column name for that same clip.)
- **Video** — `question_video` holds a short clip (driving shot, a distinctive feature or sound in motion, start-up) built per CLAUDE.md's Video and audio rules (filename, format, length, media/ storage). Every brand mark visible in the frame must be hidden/cropped exactly like a photo row — same method and same check.

**What the question asks**
- The question says exactly what is asked:
  - "ما الشركة المصنّعة لهذه السيارة؟" → brand only (e.g. تويوتا)
  - "ما اسم هذه السيارة؟" → brand + model (e.g. تويوتا لاندكروزر)
- Never ask for the model year — too many valid answers.
- If the model's generations look clearly different, the photo must show one generation, and note names it (e.g. "الجيل 300، 2021+"). The answer stays brand + model unless the question asks for the generation.
- Put the English name in note as accepted (e.g. "Land Cruiser").
- Badge-engineered twins (near-identical cars sold under two brands, e.g. Toyota 86 / Subaru BRZ, some Chevrolet/GMC trucks): avoid, unless the photo clearly shows a design difference — otherwise the twin is a second valid answer.

**Hiding brand marks (photos)** — the core rule of this section
- Hide EVERY mark that names or identifies the brand or model: grille emblem, steering-wheel badge, wheel-centre caps, rear badge and model lettering, brand name spelled on the bonnet/tailgate/sills, screen start-up logo, gear knob, headrest or seat embroidery, floor mats, key, dealer plate frame.
- Do NOT hide design features that aren't marks (grille shape, light signature, body lines) — those are the clue.
- Method: writer downloads the source image, covers each mark with a solid plain box (grey or black) using Python + Pillow, and saves it as `media/cars/<brand>-<model>-<ext|int>-<n>.jpg`. No blur — blurred badges can still be read.
- writer opens the edited image (Read tool) and checks it, zooming into crops where needed. reviewer repeats this independently in Pass 3. One visible mark = fail.
- If hiding the marks leaves too little to recognise the car, choose a different photo.

**Image source and storage**
- Source photos from Wikimedia Commons only (licensed for reuse). Put the original Commons file page URL in note, for attribution.
- `question_image`, like every other section, holds a direct https:// link — never a local path (human ruling, 2026-10-20: images are always a URL, project-wide; `media/<section>/` is for video/audio clip files only, matched by filename through the admin panel — see Video and audio rules).
- Because the edited (marks-masked) file is a new file that doesn't exist anywhere public, writer must publish it to get that URL: save it to `media/cars/<brand>-<model>-<ext|int>-<n>.jpg` as before, then `git add`/`git commit`/`git push` that file to `origin/master`, then set `question_image` to `https://raw.githubusercontent.com/iconi12/Questions/master/media/cars/<same filename>`. After pushing, fetch the raw URL once to confirm it actually resolves before marking the row done.
- `answer_image` (optional): direct link to the original, unedited Commons photo, for the reveal.
- Pass 1 verifies the photo really shows the stated model and generation — Commons descriptions are sometimes wrong (facelifts, twins, mislabelled uploads). Confirm with a second source if there's any doubt.

**Sound rows**
- No separate column — built as an audio-only `.mp4` per CLAUDE.md's Video and audio rules (still cover + sound, same `question_video`/`answer_video` columns and naming convention as a normal video row). The cover must be a neutral image (not a photo of the car) since the car itself is what's being guessed.
- Only cars with a genuinely distinctive sound. Most cars sound alike, so sound rows are a minority and do not count toward any quota — write only the truly identifiable ones.
- Source: a direct audio file (.ogg / .mp3 / .wav) from Wikimedia Commons is preferred. A YouTube link is allowed only with an exact start time (`?t=`), the end second in note, and "لا تُعرض الشاشة" in note — the video title would reveal the answer.
- The clip must contain no speech or on-screen text naming the car.
- Agents cannot listen to audio. Sound rows are judged on the source's description only, and every sound row gets "يحتاج سماع" in note. lead adds a sheet `audio_check` to questions.xlsx listing all sound/video rows for the human to check.

**Difficulty**
- 100 — cars common on Saudi roads or iconic worldwide, exterior photo, brand or brand + model (e.g. a current Land Cruiser).
- 300 — recognisable to people who follow cars.
- 500 — needs real car enthusiasm: rare models, older generations, interiors of less common cars, sounds.
- An interior photo is usually one tier harder than the exterior of the same car.
- Core rule D's era quotas don't apply here; difficulty comes from how recognisable the car is.
- Spread across brands — no more than ~10% of the section from one brand.

## 26. صراع العروش (Game of Thrones)
The HBO TV series only (8 seasons, 2011–2019).
- Not the books (A Song of Ice and Fire), and not House of the Dragon or any other spin-off.
- Where the show differs from the books, the show's version is the answer. A detail that exists only in the books is out of scope, even if true.
- Topics: characters, events, places, houses, sigils and words, episodes. Production (cast, filming locations) is allowed but at most ~1 in 10 rows.
- Names: common Arabic spelling (جون سنو، دينيرس تارجيريان، كينغز لاندينغ), with the English name in note as accepted.
- If a fact changes during the show (who rules, who is alive, titles), the question names the season.
- "Who said this?" questions: quote only a short line (a few words), never long passages.
- Sources: the Game of Thrones wiki or HBO material — check the entry describes the show, not the books (the wiki marks book/show differences).
- Difficulty scale: imagine 10 Saudi adults **who have watched the whole series**, not 10 random people — players who pick this category are viewers.
  - 100 — main characters and iconic moments.
  - 300 — needs attention while watching.
  - 500 — a precise detail of a known scene (who did it, a minor character's name in a famous scene), not obscure background lore.
- Core rule D's era quotas don't apply here.

## 27. هاري بوتر (Harry Potter)
Video/image filename code: `hp`

**Quantity override (human, 2026-10-22):** this section's target is 450 total, not the usual 300 — 150 approved at EACH of 100/300/500, not 100. This replaces CLAUDE.md's global 100-per-tier minimum for this section only. Already-approved rows stay as they are — this only means writing more, not revisiting what's done.

**Question-form variety (human, 2026-10-22):** too many rows so far ask "ما اسم..." (what is the name of...). From here on, write noticeably more rows in other forms: "ماذا حدث..." / "وش صار..." (what happened), "ماذا قال... / وش قال..." (what a character said), "من فعل..." (who did something) — event- and action-based questions, not just naming. Don't rewrite or delete any existing approved or pending row to fit this — it only applies to new rows going forward. Aim for these forms to clearly outnumber "ما اسم" rows across the next batches, not just appear occasionally.

**Difficulty calibration (human, 2026-10-21) — read this before rating ANY row.** In batch 1, the human corrected 6 of 50 rows on points, 5 of them 500 → 100, all genuinely iconic, widely-remembered scenes: Dobby being freed by Harry, Harry secretly teaching Dumbledore's Army, Hagrid carrying "dead" Harry out of the Forbidden Forest. These are exactly what the section's own scale calls 100 ("main characters and iconic moments") — not 500. The pattern behind the mistake: rating a row by "does this require remembering a specific scene" instead of "would most of the 10 Saudi adults who watched all 8 films instantly recognize this moment." A scene being specific is not the same as a scene being obscure — the most famous, emotional, visually iconic moments in the films ARE specific scenes, and they are still 100s. Reserve 500 for a detail that actually needs close attention or memory beyond the main story beat (an exact line, a minor character, which of two similar scenes). Before marking any row's points in this section, re-run this test explicitly, don't default to "it's a scene, so it's at least 300."
Writer/reviewer: re-sweep every row already written in this section (not just future ones) against this test before the next batch goes out — don't wait for the human to catch each instance individually.

**Media quota (human, 2026-10-21):** across the section's 300 rows, include 12 rows with a `question_image` and 12 rows with a `question_video` — 4 images and 4 videos at EACH point tier (100/300/500). These count toward the normal 100-per-tier totals, they are not extra rows on top.
- Images and video clips do NOT need masking/blurring/editing — they show the scene/character as-is. A video clip still needs trimming to the right moment/length (5–15s) per the standing Video and audio rules, and must not show the answer (e.g. a "what did X say after this" clip ends BEFORE the line is said).
- Image question style: "من هذا؟" (a character) or "ماذا حدث هنا؟ / وش صار هنا؟" (a scene/moment) — picture must not give the answer away by itself beyond what the question asks.
- Video question style: "وش قال هاري بعد هذي اللقطة؟" (what did a character say right after this clip), "وش سبب هذا الحدث؟" (what caused this event), "وش سوت هيرمايني هنا؟" (what did a character do here), or similar — the clip is the question's "description", the question text still must follow all question rules (one answer, no hints).
- Sourcing: film stills/clips are copyrighted, unlike sports broadcast highlights — follow the Image rules strictly (Wikimedia Commons only, no exceptions for this section). For video, check `media/هاري بوتر/raw/` first.
- **Video sourcing policy (human, 2026-10-22):** `media/هاري بوتر/raw/` is empty and the human has decided agents should source clips themselves (same approach as the football sections' highlight sourcing), understanding this carries more copyright exposure than a sports highlight does — it's scripted studio film content, not a recap of a live event. Practical guidance: prefer a single short, uncommented clip (no reaction/review overlay) over a full scene; avoid anything with a third-party channel's visible watermark (same as the existing video rule already requires); keep clips as short as the question needs (5–15s per the standing rule) rather than longer than necessary. This is a one-time decision for this section — don't extend it to any other section without asking again.
- **Image sourcing policy (human, 2026-10-21):** Commons has no free in-scene film stills, only free-licensed actor photos — so mix the approach across the 12 image rows:
  - For a row about a CHARACTER, an actor photo is fine ("من هذا الممثل الذي جسّد شخصية X؟" / "من هذه الممثلة التي جسّدت شخصية X؟") — but these count as production trivia against the section's ~1-in-10 cap, so budget at most ~3 of the 12 image rows this way.
  - For the rest, search case-by-case for free-licensed stills that aren't in-scene character shots — objects (wands, the Golden Snitch), creatures, posters/promotional art, locations used for filming (real places, e.g. Alnwick Castle, Christ Church Oxford), logos/symbols (house crests, the Deathly Hallows symbol) are more likely to have a genuinely free Commons image than a copyrighted frame of a character. Verify each one actually loads and shows the right thing before using it, same as any image.
  - If no free image exists for a planned row's topic after a real search attempt, pick a different topic for that image slot rather than forcing a weak match — there's no shortage of Harry Potter topics to choose from.

The 8 Harry Potter films only (2001–2011).
- Not the books, not Fantastic Beasts, not The Cursed Child, not the HBO series.
- Where the films differ from the books, the film's version is the answer. Book-only characters, scenes and details (e.g. Peeves) are out of scope.
- Topics: characters, events, spells, creatures, places, objects, houses. Production (cast, directors) is allowed but at most ~1 in 10 rows.
- **Answer format (human, 2026-10-21, tightened 2026-10-22):** for any answer that's a name/title (character, person, place, spell, object, film/book title) OR an exact line actually spoken on screen, put the English right in the answer field too, after the Arabic — e.g. "عباءة الإخفاء Invisibility Cloak", "يجب ألا أكذب I must not tell lies". Not just in note anymore.
  - **Does NOT apply** to a plain description, action, or paraphrase of what happens — even if it's easy to translate. "أن يأكلوهما Eat them" (row 228, what Aragog lets his spiders do) is wrong: nobody says "eat them" on screen, that's an invented English gloss of a summary, not a name or a real quote. Same for "ترتد عليه فيفقد ذاكرته Spell backfires" (row 226) — a paraphrase, not dialogue. These should be Arabic only.
  - The test: would an English-speaking fan recognize this exact English text as the thing's actual name, or as a line really spoken in the film? If you're translating/summarizing rather than citing an established name or real quote, leave English out.
  - This applies to every row with this kind of answer, past and future. Writer: sweep the whole file again — this time removing wrongly-added English from description/action answers, not just adding it to names. Don't just fix the 2 cited rows.
- Name the film when the fact belongs to one film or changes between films.
- "Who said this?" questions: quote only a short line (a few words), never long passages.
- Sources: the Harry Potter wiki — check the entry describes the film version (its "Behind the scenes" sections list book/film differences).
- Difficulty scale: imagine 10 Saudi adults **who have watched all 8 films**.
  - 100 — main characters and iconic moments.
  - 300 — needs attention while watching.
  - 500 — a precise detail of a known scene, not obscure lore.

## 28. ون بيس (One Piece)
Video/image filename code: `op`
The anime only (ongoing). Not the manga — where they differ, the anime's version is the answer.
- No fixed episode cutoff (human, 2026-10-22): write from whatever's currently aired; re-check anchor-point superlatives ("the first/only/latest to...") if new episodes air before this section is finished.
- Topics: characters, crews, Devil Fruits, events, arcs, islands, bounties. Production (voice cast, studio) at most ~1 in 10 rows.
- Names: common Arabic spelling (لوفي، زورو، نامي، الوان بيس), English/Japanese name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule — Arabic + English only when the ANSWER itself is a name/title or an exact spoken line, never because the question mentions one.
- Sources: One Piece Wiki (Fandom) — confirm anime vs. manga-only content, the wiki marks the difference.
- Difficulty scale: imagine 10 Saudi adults who follow the anime.
  - 100 — main characters, iconic moments, the Straw Hat crew.
  - 300 — needs real engagement with the story (a named Devil Fruit, a specific arc detail).
  - 500 — a precise detail of a known scene (a minor character, an exact bounty number, a specific episode's event), not obscure background lore.
- Core rule D's era quotas don't apply here.

## 29. هجوم العمالقة (Attack on Titan)
Video/image filename code: `aot`
The anime only (4 seasons, complete). Not the manga — where they differ, the anime's version is the answer.
- Topics: characters, Titans, factions, events, places. Production at most ~1 in 10 rows.
- Names: common Arabic spelling (إيرين ييغر، مايكاسا، ليفاي)، English/Japanese name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- Sources: Attack on Titan Wiki (Fandom) — confirm anime vs. manga-only content.
- Difficulty scale: imagine 10 Saudi adults who've watched the whole anime.
  - 100 — main characters and iconic moments.
  - 300 — needs attention while watching.
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.

## 30. ناروتو (Naruto)
Video/image filename code: `nrt`
The anime only — Naruto, Naruto Shippuden, and the sequel series Boruto are all in scope unless a question specifically needs pinning to one (then name it, e.g. "في ناروتو شيبودن"). Not the manga.
- No fixed cutoff on Boruto content (human, 2026-10-22): write from whatever's currently aired.
- Topics: characters, jutsu, villages, clans, events. Production at most ~1 in 10 rows.
- Names: common Arabic spelling (ناروتو، ساسكي، كاكاشي)، English/Japanese name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- Sources: Narutopedia (Fandom) — confirm anime vs. manga-only, and which series (original/Shippuden/Boruto) the fact belongs to.
- Difficulty scale: imagine 10 Saudi adults who've watched the anime (through Shippuden at least).
  - 100 — main characters and iconic moments.
  - 300 — needs attention while watching.
  - 500 — a precise detail of a known scene, not obscure lore. A Boruto-only detail that casual original-series fans wouldn't know leans 500.
- Core rule D's era quotas don't apply here.

## 31. بيتر كول ساول (Better Call Saul)
Video/image filename code: `bcs`
The AMC TV series only (6 seasons, complete, 2015–2022).
- Not Breaking Bad (separate section, no crossover questions in either section even though they share a universe/characters) — a Better Call Saul row must be about something that happens/is established IN this show, not something only confirmed by Breaking Bad.
- Topics: characters, cases, events, places. Production at most ~1 in 10 rows.
- Names: common Arabic spelling (جيمي ماكغيل، كيم ويكسلر، مايك إيرمانتراوت)، English name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- "Who said this?" questions: quote only a short line, never long passages.
- Sources: Breaking Bad Wiki's Better Call Saul section (Fandom) — confirm the fact is from this show.
- Difficulty scale: imagine 10 Saudi adults who've watched the whole series.
  - 100 — main characters and iconic moments.
  - 300 — needs attention while watching.
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.

## 32. بريكنغ باد (Breaking Bad)
Video/image filename code: `bb`
The AMC TV series only (5 seasons, complete, 2008–2013).
- Not Better Call Saul (separate section, no crossover questions in either — a Breaking Bad row must be about something established IN this show, not only confirmed by the spin-off) and not El Camino unless explicitly allowed later.
- Topics: characters, events, places, the drug business's details as portrayed. Production at most ~1 in 10 rows.
- Names: common Arabic spelling (والتر هوايت، جيسي بينكمان، غوستافو فرينغ)، English name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- "Who said this?" questions: quote only a short line, never long passages.
- Sources: Breaking Bad Wiki (Fandom).
- Difficulty scale: imagine 10 Saudi adults who've watched the whole series.
  - 100 — main characters and iconic moments.
  - 300 — needs attention while watching.
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.

## 33. ألعاب الفيديو (Video Games)
Video/image filename code: `vg`
General gaming/esports knowledge and culture — NOT deep lore of any single game that has its own section (see إلدن رينغ, section 34; a question about Elden Ring specifically belongs there, not here).
- Topics: consoles/platforms, major franchises and their famous characters (at a general-knowledge level, not deep lore), esports tournaments/teams (including Saudi esports, e.g. Team Falcons), game industry facts (studios, publishers, release history), gaming culture. A deep-lore question about one specific game's story/mechanics belongs in that game's own section if one exists, or is likely too niche for this section.
- Names: common Arabic spelling with the English/original name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule — applies here too (judge the answer, not the question).
- Sources: the game/franchise's own wiki, official sites, Liquipedia for esports.
- Difficulty scale (human, 2026-10-16's general framing applies): judge by what YOUNG SAUDI gamers would know — mainstream/competitive titles and Saudi esports are EASY here, not hard.
  - 100 — major franchises, consoles, well-known esports teams/events (e.g. Team Falcons winning a major).
  - 300 — needs real interest in gaming (a specific tournament result, a studio's other games).
  - 500 — a precise detail few but dedicated gamers would know.
- Core rule D's era quotas don't apply here, but recent (last ~10 years) gaming/esports content should still be well represented given the young-Saudi-audience skew toward current gaming culture.

## 34. إلدن رينغ (Elden Ring)
Video/image filename code: `er`
The game Elden Ring, including its Shadow of the Erdtree expansion. Not other FromSoftware games (Dark Souls, Bloodborne, Sekiro) unless a question is explicitly about a crossover/shared element.
- Topics: characters, bosses, locations, items, lore, mechanics.
- Names: common Arabic spelling with the English name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- Sources: Elden Ring Wiki (Fextralife or IGN) — confirm base game vs. Shadow of the Erdtree if it matters to the question.
- Difficulty scale: imagine 10 Saudi adults who've played through the game.
  - 100 — main characters, bosses and iconic moments (Malenia, the Elden Ring itself, the open world's main story beats).
  - 300 — needs real engagement with the game (a specific boss's location, an item's effect).
  - 500 — a precise, easy-to-miss detail (an NPC's exact dialogue, an obscure item, a hidden area), not something every player would've encountered.
- Core rule D's era quotas don't apply here.

## 35. ذا بويز (The Boys)
Video/image filename code: `boys`
The Prime Video TV series only. Not the comics — where they differ, the show's version is the answer. Not spin-offs (Gen V) unless explicitly allowed later.
- No fixed season cutoff (human, 2026-10-22): write from whatever's currently aired.
- Topics: characters (The Seven, the Boys), events, Compound V, corporate/Vought storylines. Production at most ~1 in 10 rows.
- Names: common Arabic spelling (هومي لاندر، بوتشر، ستارلايت)، English name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- "Who said this?" questions: quote only a short line, never long passages.
- Sources: The Boys Wiki (Fandom) — confirm show vs. comic-only content.
- Difficulty scale: imagine 10 Saudi adults who've watched the whole show (through the latest aired season).
  - 100 — main characters and iconic moments.
  - 300 — needs attention while watching.
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.

## 36. إنفينسبل (Invincible)
Video/image filename code: `inv`
The Prime Video animated series only. Not the comics — where they differ, the show's version is the answer.
- No fixed season cutoff (human, 2026-10-22): write from whatever's currently aired.
- Topics: characters, powers, events, factions. Production (voice cast) at most ~1 in 10 rows.
- Names: common Arabic spelling (مارك غرايسون/إنفينسبل، أومني-مان)، English name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- Sources: Invincible Wiki (Fandom) — confirm show vs. comic-only content.
- Difficulty scale: imagine 10 Saudi adults who've watched the whole show (through the latest aired season).
  - 100 — main characters and iconic moments.
  - 300 — needs attention while watching.
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.

## 37. مارفل (Marvel)
Video/image filename code: `mcu`
**Scope (human, 2026-10-22): the Marvel Cinematic Universe theatrical FILMS only.** Not the Disney+ shows (WandaVision, Loki, etc.), not the comics, not non-MCU Marvel films (Sony's older Spider-Man series, Fox's X-Men/Deadpool pre-MCU). If a fact is only established in a Disney+ show, it's out of scope for this section.
- Topics: characters, events, films, villains, powers/abilities as shown on screen. Production (cast, directors) at most ~1 in 10 rows.
- Names: common Arabic spelling (توني ستارك/آيرون مان، ثانوس، كابتن أمريكا)، English name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- Name the film when a fact belongs to one film or changes between films (characters die/return, team rosters change, etc.).
- "Who said this?" questions: quote only a short line, never long passages.
- Sources: Marvel Cinematic Universe Wiki (Fandom) — NOT the general Marvel/comics wiki, which mixes in comic-only continuity.
- Difficulty scale: imagine 10 Saudi adults who've watched the MCU films.
  - 100 — main characters and iconic moments.
  - 300 — needs attention while watching.
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.

## 38. سيد الخواتم (Lord of the Rings)
Video/image filename code: `lotr`
Peter Jackson's original trilogy films only (The Fellowship of the Ring, The Two Towers, The Return of the King, 2001–2003). Not The Hobbit trilogy, not the Amazon Rings of Power series, not the books — where the films differ from Tolkien's books, the film's version is the answer.
- Topics: characters, places, events, items (the Ring, swords, etc.), races (hobbits, elves, etc.). Production (cast, New Zealand filming locations) at most ~1 in 10 rows.
- Names: common Arabic spelling (فرودو، غاندالف، آراغورن، موردور)، English name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- "Who said this?" questions: quote only a short line, never long passages.
- Sources: Tolkien Gateway or the One Wiki to Rule Them All (Fandom) — check the entry describes the film version, since book/film differences are significant in this trilogy.
- Difficulty scale: imagine 10 Saudi adults who've watched the trilogy.
  - 100 — main characters and iconic moments.
  - 300 — needs attention while watching.
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.

## 39. ديزني وبيكسار (Disney+Pixar)
Video/image filename code: `dp`
**Scope (human, 2026-10-24): classic Disney animation + Pixar theatrical animated films only.** Not Disney+ live-action or non-Pixar original shows, not Marvel (separate section, MCU films only), not Star Wars, not Disney's live-action remakes of its own animated films unless a question is explicitly about the remake and says so.
- Topics: characters, plots, songs, villains, sidekicks, voice actors (production at most ~1 in 10 rows).
- Names: common Arabic spelling (الملك الأسد، سيمبا، شركة المرح المحدودة، وودي وباز) with the English title/name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule — judge the answer, not the question.
- Name the film when a fact belongs to one film specifically (e.g. a song, a specific sidekick).
- "Who said this?" / "what did X sing?" questions: quote only a short line, never long passages.
- Sources: Disney Wiki or Pixar Wiki (Fandom).
- Difficulty scale: imagine 10 Saudi adults who grew up watching Disney/Pixar films.
  - 100 — iconic films, main characters, iconic moments/songs.
  - 300 — needs real engagement with a specific film (a secondary character, a plot detail).
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.

## 40. فرندز (Friends)
Video/image filename code: `friends`
The NBC sitcom only (10 seasons, 1994–2004). Not spin-offs, not the 2021 reunion special unless a question is explicitly about the reunion and says so.
- Topics: the six main characters, running jokes/catchphrases, events, guest stars, episode plots. Production at most ~1 in 10 rows.
- Names: common Arabic spelling (روس، راتشيل، تشاندلر، مونيكا، جوي، فيبي) with the English name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- "Who said this?" questions: quote only a short line (catchphrases like "We were on a break!" are fair game, exactly as said), never long passages.
- Name the season when a fact changes across the show (relationships, jobs, apartments).
- Sources: Friends Central Wiki (Fandom) or IMDb episode guides.
- Difficulty scale: imagine 10 Saudi adults who've watched the whole series.
  - 100 — main characters and iconic moments/running jokes.
  - 300 — needs attention while watching (a specific episode's plot, a recurring guest character).
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.

## 41. سبونج بوب (SpongeBob SquarePants)
Video/image filename code: `sb`
The animated series only. No fixed episode cutoff (still airing, same approach as ون بيس) — write from whatever's aired; not the theatrical movies unless a question is explicitly about one and says so.
- Topics: characters, events, running jokes, places (قاع الهامور). Production at most ~1 in 10 rows.
- Names: common Arabic spelling (سبونج بوب، سكوير، باتريك، سكويدوارد، السيد كرابس) with the English name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- "Who said this?" questions: quote only a short line, never long passages.
- Sources: SpongeBob Wiki (Fandom).
- Difficulty scale: imagine 10 Saudi adults who grew up watching the show.
  - 100 — main characters and iconic moments/running jokes.
  - 300 — needs real engagement with the show (a specific episode's plot, a recurring minor character).
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.

## 42. سبيستون (Spacetoon)
Video/image filename code: `st`
**Scope (human, 2026-10-24): any show that aired dubbed in Arabic on the Spacetoon channel** — not one single IP. Examples: كابتن ماجد (Captain Tsubasa), غرايندايزر، دورايمون، مغامرات عدنان، ساسوكي، and similar Spacetoon-era cartoons/anime. This section is the one exception to the project's section-exclusivity rule (see Scope boundaries above): it may overlap with ون بيس، هجوم العمالقة، ناروتو or any other section whose show also aired on Spacetoon — write the question in both places if it genuinely fits both.
- Audience note: this is a nostalgia section. The target "10 Saudi adults" are the now-18–30 audience who watched these shows as children on Spacetoon — judge difficulty by what THEY remember from childhood viewing, not by how obscure a detail is to a non-viewer.
- Topics: characters, events, theme songs/intros, running jokes, across any Spacetoon-aired show. Spread across different shows — don't cluster on one.
- Names: common Arabic spelling as used in the Spacetoon dub (this is usually different from the Japanese/English original — e.g. كابتن ماجد not Captain Tsubasa) — this Arabic dub name IS the primary name for this section, not a translation of it. Put the original Japanese/English title in note.
- Answer format: per CLAUDE.md's movie/TV-series rule, but applied to the Arabic dub name — English goes in note here rather than the answer field, since the Spacetoon-dub Arabic name is what the audience actually knows (unlike other sections, there often isn't a widely-known English form the Saudi audience would recognize).
- Sources: the show's own wiki (Fandom) where one exists and covers the dub; otherwise general web search — note any case where only the original (non-dubbed) version's facts are verifiable, since dub-specific details (dubbed character names, cut content) are less documented online.
- Difficulty scale: imagine 10 Saudi adults who watched Spacetoon as kids.
  - 100 — the most-watched/iconic shows and their main characters.
  - 300 — needs having actually watched the specific show closely.
  - 500 — a precise detail of a known scene or a less-remembered show, not obscure lore.
- Core rule D's era quotas don't apply here.
- **Focus and franchise cap (human, 2026-10-27):** the section had too many rows from ون بيس، هنتر × هنتر، ناروتو and دراغون بول — keep each of these four at about 5 rows (the most iconic) and write no more about them. Don't let any single show dominate (المحقق كونان، الديجيمون، السنافر، دورايمون are already large) — spread new rows across other Spacetoon-aired shows. Put the new emphasis on Spacetoon ITSELF and its music:
  - **Planets (كواكب سبيستون):** the channel groups its shows into planets, each a genre/classification (e.g. بون بون، أبجد، زمردة، أكشن، مغامرات، رياضة، كوميديا). Ask which planet a show belongs to, what a planet stands for, which shows a planet holds. The lineup changed (10 planets at the 2000 launch: أبجد، أفلام، أكشن، بون بون، زمردة، كوميديا، مغامرات، رياضة، علوم، تاريخ; cut to 7 in March 2013; علوم returned Sep 2013 and أفلام Sep 2015, giving 9 now, تاريخ gone) — anchor any fact that changed to a stated date; stable genre facts need none. Show-to-planet placements: use only what a source states. Source: ar.wikipedia سبيستون.
  - **Openings / theme songs:** the Arabic-dub intros — which show, who sang it, a short lyric line (only when two sources agree).
  - **OSTs / background music** of the shows.
  - **Picture questions on iconic works** Spacetoon aired: `question_image` per the image rules (the image must not reveal the answer).
  - Without source audio files from the human, music rows are text questions; no clips are made.
  - **MANDATORY — every question names its show (human, 2026-10-27):** سبيستون is not one specific category; it holds dozens of unrelated shows, so a player cannot guess which show a question is about. Every question must therefore state the show's name ("في المحقق كونان…", "في مغامرة الديجيمون…") or contain a character/object that unambiguously identifies one show (لوفي، غوكو، ران، شرشبيل). Naming the show is NOT a hint — the clause test doesn't remove it, because deleting it leaves the question open to many shows (Core rule B). These do NOT identify a show: "the villain / the children / the case / the dog / the team", a generic place or case name, or a common first name (وسيم، عامر، أمجد، زاجل). Reviewer: fail any row that doesn't pass this, in every pass. (An audit on 2026-10-27 found 26 approved rows that failed it; they were reworded.)
  - **Questions are about the shows, the dub, the channel and its music** — not about unrelated events that merely involve a Spacetoon show (e.g. a Riyadh Season statue of Grendizer was rejected under Core rule C).
  - **No title-translation trivia:** don't write rows that just ask for a show's original/English/Japanese title (low value for this audience); ask about the show's content, dub, planets, songs or music.
  - **Proof images for new rows (Core rule E):** each new row needs a loadable `answer_image` (or `answer_video`) that proves the specific fact. Human ruling (2026-10-27): news-site or channel images are allowed as proof (e.g. Logopedia planet logos), downloaded normally (no mirrors, proxies or workarounds), saved to `media/spacetoon/`, and published via git as Rule E describes. If no proof can be found after a real search, the row may be approved without an image (CLAUDE.md Core rule E, human ruling 2026-10-27): note what was tried and "no proof image found" in `note`. Never attach a weak or merely topical image just to fill the field. Existing approved rows are exempt until the separate resweep; rows reopened only to add the show name don't need an image either.

## 43. كول أوف ديوتي بلاك أوبس زومبيز (Call of Duty: Black Ops Zombies)
Video/image filename code: `codz`
**Scope (human, 2026-10-24): the Zombies co-op mode across all Black Ops titles** (Black Ops, Black Ops II, Black Ops III, Black Ops 4, Black Ops Cold War, Black Ops 6, and any later Black Ops game). Not multiplayer or campaign modes of these games, and not Zombies modes from non-Black-Ops Call of Duty games (Modern Warfare, WWII, Vanguard) — those are out of scope entirely, not placed in ألعاب الفيديو either.
- Topics: maps, Easter eggs/endings, the four main characters (Richtofen، Dempsey، Nikolai، Takeo) and later casts, perks, wonder weapons, game mechanics (the Pack-a-Punch, the box, round mechanics), story line.
- Names: common Arabic spelling with the English name in note as accepted (e.g. "باك-أ-بانش Pack-a-Punch").
- Answer format: per CLAUDE.md's movie/TV-series rule — applies here too (judge the answer, not the question).
- Name the specific Black Ops title when a fact belongs to one game (a map, a character's game-specific role) or changes across games.
- Sources: Call of Duty Wiki (Fandom), the Zombies-specific sections.
- Difficulty scale: imagine 10 Saudi adults who've played Black Ops Zombies.
  - 100 — the most iconic maps/characters/moments (e.g. Nacht der Untoten, the original four characters).
  - 300 — needs real engagement with the mode (a specific map's Easter egg step, a specific wonder weapon).
  - 500 — a precise, easy-to-miss detail (an exact Easter egg requirement, an obscure map, a minor character), not something every player encountered.
- Core rule D's era quotas don't apply here.

## 44. مسلسلات رمضانية (Ramadan series)
Video/image filename code: `ramadan`
**Scope (human, 2026-10-24): Saudi and Gulf-produced Ramadan drama series only**, any year. Not Egyptian, Syrian or other non-Gulf Arab Ramadan series.
- Topics: characters, plots, actors, memorable scenes/lines, which year/Ramadan a series aired.
- Name the series (and year, if more than one season/series shares a name) when a fact could otherwise apply to more than one show.
- Answer format: per CLAUDE.md's movie/TV-series rule — English in the answer only for an actor's name that has an established English spelling, essentially never for a purely Arabic show/character name (leave English out unless there's a genuine established Latin-script form).
- "Who said this?" questions: quote only a short line, never long passages.
- Sources: these are mostly NOT covered by a dedicated wiki — rely on web search (Arabic entertainment news sites, IMDb, the production company's own announcements). Require a source for every row regardless of points (treat like Pass 1's "slightest doubt" standard, every time) — this section has thinner, less reliable sourcing than wiki-backed sections and is more prone to misremembered/uncorroborated claims.
- Difficulty scale: imagine 10 Saudi adults who follow Gulf Ramadan drama.
  - 100 — the most-watched, most-talked-about series and their main characters/stars.
  - 300 — needs having followed that specific series.
  - 500 — a precise detail of a known scene or a less-remembered series, not obscure trivia.
- Core rule D's era quotas don't apply here.

## 45. دريم وركس (DreamWorks)
Video/image filename code: `dw`
DreamWorks Animation's theatrical animated films only (Shrek, Madagascar, Kung Fu Panda, How to Train Your Dragon, Trolls, etc.). Not Netflix/TV spin-off series of these franchises unless a question is explicitly about one and says so (same films-only approach as ديزني وبيكسار, for consistency).
- Topics: characters, plots, songs, villains, sidekicks, voice actors (production at most ~1 in 10 rows).
- Names: common Arabic spelling (شريك، حمار، كونغ فو باندا، بو) with the English title/name in note as accepted.
- Answer format: per CLAUDE.md's movie/TV-series rule.
- Name the film when a fact belongs to one film specifically.
- "Who said this?" questions: quote only a short line, never long passages.
- Sources: DreamWorks Animation Wiki (Fandom).
- Difficulty scale: imagine 10 Saudi adults who've watched these films.
  - 100 — iconic films, main characters, iconic moments.
  - 300 — needs real engagement with a specific film (a secondary character, a plot detail).
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.