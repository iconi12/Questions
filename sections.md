# Sections

Work through the sections in this order. Do not add, rename, or merge sections.
Each section has notes on its scope and special rules — they override the general rules in CLAUDE.md where they conflict.

## Scope boundaries (to avoid duplicates across sections)
- A topic that has its own section belongs ONLY to that section.
- السعودية: excludes Saudi football, dialects, and restaurants (they have their own sections).
- تاريخ: excludes WWI, WWII, السيرة النبوية, and قصص الأنبياء.
- جغرافيا: excludes capitals (they belong to دول و عواصم).
- معلومات عامة: only questions that don't fit any other section.
- سيارات، صراع العروش، هاري بوتر: their topics belong only to them — no car, Game of Thrones or Harry Potter questions in معلومات عامة or any other section.

---

## 1. السعودية
History, geography, culture, landmarks, Vision 2030, notable facts about Saudi Arabia.

## 2. معلومات عامة
Mixed general knowledge: science, inventions, records, everyday facts.

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
Countries and capitals. For countries with disputed or multiple capitals, either avoid them or state the official one clearly.

## 7. الحرب العالمية الاولى

## 8. الحرب العالمية الثانية

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

## 13. البحرين

## 14. الامارات

## 15. عمان

## 16. لهجات سعودية
Meanings of Saudi dialect words and expressions.
- Name the region in the question when the word is regional (e.g. "في اللهجة النجدية").
- Avoid words whose meaning differs between regions unless the region is stated.

## 17. تاريخ
Islamic, Arab, and world history (see scope boundaries above).

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

**Media quota (human, 2026-10-21):** across the section's 300 rows, include 12 rows with a `question_image` and 12 rows with a `question_video` — 4 images and 4 videos at EACH point tier (100/300/500). These count toward the normal 100-per-tier totals, they are not extra rows on top.
- Images and video clips do NOT need masking/blurring/editing — they show the scene/character as-is. A video clip still needs trimming to the right moment/length (5–15s) per the standing Video and audio rules, and must not show the answer (e.g. a "what did X say after this" clip ends BEFORE the line is said).
- Image question style: "من هذا؟" (a character) or "ماذا حدث هنا؟ / وش صار هنا؟" (a scene/moment) — picture must not give the answer away by itself beyond what the question asks.
- Video question style: "وش قال هاري بعد هذي اللقطة؟" (what did a character say right after this clip), "وش سبب هذا الحدث؟" (what caused this event), "وش سوت هيرمايني هنا؟" (what did a character do here), or similar — the clip is the question's "description", the question text still must follow all question rules (one answer, no hints).
- Sourcing: film stills/clips are copyrighted, unlike sports broadcast highlights — follow the Image rules strictly (Wikimedia Commons preferred; the Harry Potter wiki may host stills but verify they're stable, direct image links). For video, check `media/هاري بوتر/raw/` first; if it's empty, flag to lead before sourcing clips from elsewhere — don't assume the same sourcing approach as the football sections' match highlights applies to studio film footage.

The 8 Harry Potter films only (2001–2011).
- Not the books, not Fantastic Beasts, not The Cursed Child, not the HBO series.
- Where the films differ from the books, the film's version is the answer. Book-only characters, scenes and details (e.g. Peeves) are out of scope.
- Topics: characters, events, spells, creatures, places, objects, houses. Production (cast, directors) is allowed but at most ~1 in 10 rows.
- Names and spells: common Arabic spelling (هيرميون جرينجر، دمبلدور، هوغوورتس، إكسبيليارموس), with the English name or incantation in note as accepted.
- Name the film when the fact belongs to one film or changes between films.
- "Who said this?" questions: quote only a short line (a few words), never long passages.
- Sources: the Harry Potter wiki — check the entry describes the film version (its "Behind the scenes" sections list book/film differences).
- Difficulty scale: imagine 10 Saudi adults **who have watched all 8 films**.
  - 100 — main characters and iconic moments.
  - 300 — needs attention while watching.
  - 500 — a precise detail of a known scene, not obscure lore.
- Core rule D's era quotas don't apply here.