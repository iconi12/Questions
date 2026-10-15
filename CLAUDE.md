# Trivia Question Team — Rules

## Goal
Write Arabic trivia questions for every section listed in `sections.md`, review them, and produce a final Excel file `questions.xlsx`.
Each question has: section, question, answer, points (100 / 300 / 500).

## Roles
- **writer** (Sonnet 5.5): writes questions. The ONLY agent allowed to create or edit files.
- **reviewer** (Opus 5.5): reads and checks. NEVER edits any file — sends feedback to writer by message.
- **lead**: coordinates sections and builds `questions.xlsx` at the end.

## Files
- `sections.md` — the list of sections (provided by the human). Do not add or rename sections.
- `staging/<section>.csv` — working file per section (encoding: utf-8-sig so Arabic opens correctly in Excel).
  - Columns: `section, question, answer, points, question_image, answer_image, status, note`
  - `question_image` and `answer_image` are optional image URLs (leave empty if none).
  - `status` is one of: `pending`, `pass1_ok`, `pass2_ok`, `approved`, `flagged`
- `questions.xlsx` — final output, built by lead with openpyxl from `approved` rows only.
  - One sheet per section, columns: `السؤال | الجواب | النقاط | صورة السؤال | صورة الجواب | ملاحظات أو أجوبة مقبولة`, sorted by points. The 6th column carries the row's `note` for approved rows that have a host-relevant one (accepted variants, explicit wrong-but-tempting answers, disambiguation) — leave it empty when there's nothing host-critical.
  - Plus a sheet `flagged` listing every flagged row with its note, for the human to decide.

## Quantity
- Minimum per section: 100 questions at 100 points, 100 at 300, 100 at 500 (300 total).
- Counts refer to `approved` rows. Keep writing until each level reaches 100 approved.

## Difficulty definitions
Imagine 10 random Saudi adults hearing the question:
- **100** — 7 or more of them would answer correctly.
- **300** — about 3–4 would answer correctly; needs interest in the topic.
- **500** — 2 or fewer would answer correctly; needs specialist knowledge or serious fandom.
- When unsure between two levels, choose the harder question, not the easier one.
- A 500 question must be hard because of the knowledge it needs, not because of confusing wording.
- **Difficulty = how few people can RECALL the answer — not how old the fact is.** A recent event can be 500 if few people remember the exact detail; an old event can be 100 if everyone learned it.
  Human's reference 500: "من سجّل ركلة الجزاء في مباراة سويسرا والبوسنة والهرسك في كأس العالم 2026؟" — the match is recent and many watched it, but few remember who took the penalty. That is the model for a 500.

## Core quality rules (human, 2026-10-14) — HIGHEST PRIORITY, ALL SECTIONS
These came from the human reviewing finished output. They apply to every section, and override any older rule or heuristic in this file that conflicts with them.

### A. Short questions with no hints
A question contains ONLY what is needed for it to have exactly one correct answer. Every extra word is a hint.
- **Clause test** — for each descriptor, date, place or name in the question, ask: "If I delete this, does the question get a second valid answer?"
  - No → it is a hint. Delete it.
  - Yes → it is needed. Keep it.
- **Cover test** — cover the answer and read the question as a player: does anything in it point toward the answer (a nickname, a famous trait, a well-known club, a nationality, the answer's first word, a related famous fact)? If yes, cut it.
- Do NOT add "famous" descriptions to help the player (الشهير، الملقب بـ، أبرز، المعروف بـ...) unless that description IS the question.
- Examples:
  - ❌ ما اسم المدينة الساحلية المطلة على البحر الأحمر التي تُعرف بعروس البحر الأحمر وتُعد بوابة الحرمين؟
    ✅ ما المدينة السعودية الملقّبة بعروس البحر الأحمر؟ → جدة
  - ❌ ما اسم المشروع العملاق الذي تبنيه السعودية في أقصى الشمال الغربي ضمن رؤية 2030 ويضم مدينة (ذا لاين)؟
    ✅ ما المشروع الذي تتبع له مدينة ذا لاين؟ → نيوم
  - ❌ ما اسم المعاهدة التي وقّعها الملك عبدالعزيز مع بريطانيا عام 1915م، واعترفت فيها بريطانيا بحكمه على نجد والأحساء والقطيف؟
    ✅ ما المعاهدة التي وقّعها الملك عبدالعزيز مع بريطانيا عام 1915؟ → معاهدة دارين

### B. Short does NOT mean vague
Cutting hints must never leave the question open to more than one answer.
- ❌ من هداف كأس العالم؟ (which edition? all-time?) → ✅ من هداف كأس العالم 2022؟
- ❌ ما أول خط سكة حديد في السعودية؟ (the Ottoman Hejaz Railway is a rival answer) → ✅ ما أول خط سكة حديد أنشأته الدولة السعودية؟
- These qualifiers pass the clause test (deleting them creates a second answer), so they stay. That is the difference between a needed detail and a hint.

### C. Strict section relevance
- The question must be ABOUT the section's subject — not merely mention it, take place in it, or involve someone from it.
- Test: a player who chose this category — would they expect this question? If the link to the section is incidental, the row is rejected.
  - Examples of incidental (reject): in الكويت, a science fact whose only link is that the scientist was Kuwaiti-born; in كاس العالم, a country's public holiday after a win; in عالم الحيوان, a sports team named after an animal.
- Out-of-scope rows are DELETED, not reworded into scope. When unsure, reject — there is no shortage of in-scope questions.

### D. 500 questions must not be mostly old history
- Difficulty must come from recall (see the definition above), not from age.
- In sections that are NOT historical by nature (everything except الحرب العالمية الاولى، الحرب العالمية الثانية، تاريخ، السيرة النبوية، قصص الانبياء):
  - At most 3 in every 10 of a batch's 500 questions may be about events before the year 2000.
  - At least 3 in every 10 must be about the last ~15 years — exact details of recent events (who scored/missed/assisted, the second or third place, the runner-up, the exact count, the person behind a recent decision).
  - "In which year...?" must not be the default 500 form. At most 2 in every 10 500s may have a year as the answer.
- In historical sections, a 500 should be a precise detail of a known event (who commanded, where exactly, how many) rather than an obscure event almost nobody has heard of.
- Reminder: "small set of people" answers (e.g. the 2 players who missed in a shootout) are allowed — see the كاس العالم notes on rule 2.

## Calibration (first section only)
Before mass writing, writer produces 5 questions per level for the first section and stops.
The human approves or adjusts them; the approved ones are pasted below as the reference for all sections.

### Reference examples
Approved from the السعودية calibration batch (2026-10-01). Wording tightened on 2026-10-14 to the concise, no-hint style of Core rule A — answers and tiers are unchanged. Copy this STYLE, not the old long style.

- 100:
  - ما عاصمة السعودية؟ → الرياض
  - ما عملة السعودية؟ → الريال السعودي
  - من مؤسس المملكة العربية السعودية؟ → الملك عبدالعزيز
  - ما أكبر صحراء رملية متصلة في العالم؟ → الربع الخالي
  - ما أشهر جبل في المدينة المنورة؟ → جبل أحد
  - ما المشروع الذي تتبع له مدينة ذا لاين؟ → نيوم (moved down from 300 — the single most marketed Saudi project name, encountered passively regardless of interest)
  - ما اسم الخطة السعودية التي أُطلقت عام 2016 لتنويع الاقتصاد؟ → رؤية 2030 (moved down from 300 — the umbrella term used in government/media messaging more than any single project name)
- 300:
  - ما أول موقع سعودي أُدرج في قائمة التراث العالمي لليونسكو؟ → الحِجر (مدائن صالح)
  - في أي عام أُعلن توحيد المملكة العربية السعودية؟ → 1932
  - ما أول خط سكة حديد أنشأته الدولة السعودية؟ → الرياض–الدمام ("أنشأته الدولة السعودية" is needed — without it the Ottoman Hejaz Railway is a second answer. The old wording put the answer inside the question.)
  - ما أكبر جزيرة سعودية؟ → جزيرة فرسان الكبرى (moved down from 500 — too well known)
- 500:
  - ما المعاهدة التي وقّعها الملك عبدالعزيز مع بريطانيا عام 1915؟ → معاهدة دارين
  - ما أطول وادٍ في السعودية؟ → وادي الرمة
  - ما اسم أول بئر نفط تجاري في السعودية؟ → بئر الدمام رقم 7
  - ما أعلى جبل في السعودية؟ → جبل السودة (the question names what the answer is — a mountain, not a "peak")
  - Note: all four of these are about geography or the early 1900s. That is NOT the target mix for 500 — see Core rule D, and the human's recent-event reference under Difficulty definitions.

Lessons from calibration, applicable to all sections:
- A question must ask for exactly the kind of thing the answer is (don't ask for a "قمة" when the answer is a جبل's name, etc.) — check this noun-match explicitly in Pass 3.
- Keep well-known facts (e.g. a famous island most people recognize) at 300, not 500 — 500 is reserved for genuinely obscure/specialist knowledge.
- Stay within the section's own scope — a historically interesting event (e.g. a diplomatic meeting) that isn't really *about* the section's subject belongs elsewhere or not at all.
- When a verifiable fact has a disputed quantity (e.g. an exact length/date range that varies by source) but an undisputed identity/superlative, question the identity only, not the disputed number.

### Operational heuristics (from massive review, batches 1-5 of السعودية)
Converged on by writer and reviewer through 158 approved rows (2026-10-01). These are working rules, not just lessons from one incident — apply them going forward on every section. Grouped by the pass each belongs to.

**Difficulty (Pass 2):**
- ~~500 holds reliably for pre-1970 named things~~ — REPLACED 2026-10-14 by Core rule D. Age is no longer a route to 500 by itself; it caused 500s to cluster on early-1900s facts. What still holds: modern things the state actively PUBLICIZED (projects, campaigns, institutions) are rarely 500, because publicity spreads the name. A recent event's small detail that nobody publicized (who took the penalty, who came second) is a strong 500.
- Within heritage and traditional topics the discriminator is promotion, not age — specifically MANUFACTURED AWARENESS (a campaign actively pushing the name into public view), not fame in general. If an item has a UNESCO listing it was built around, is the subject of a national festival, has its own museum, or supplied a logo, it is 300 however ancient its roots. A craft that merely gets demonstrated as one of many at a heritage festival (incidental display) is not thereby promoted — it stays 500 if nothing else marks it as a campaign's subject. A nickname or fact that spread culturally without anyone pushing it (e.g. a city's traditional epithet) is also not manufactured awareness — a player either happens to know it or doesn't, which is the 300 "needs interest" case, not the 100 case. Applying "well-known" as a bare fame test instead of this narrower test collapses the 300 band.
- If an ordinary person encounters the fact in daily life, it is 100 no matter how institutional the subject sounds. For regulators specifically, the split is consumer-facing vs. industry-facing, not promoted vs. unpromoted: a food/drug authority is 100 because its approvals are on every package and its recalls are public news, while a securities regulator or a development fund is 300 because an ordinary person never transacts with it, however important it is.
- A year-recall question sits one band above recognition of the same event: everyone knows the weekend changed, far fewer can date it.
- When unsure between two levels, choose the harder — but check the row isn't hard only because of confusing wording.

**Wording and leaks (Pass 3):**
- A leak is the answer's DISTINGUISHING element appearing in the question. Nationality words (السعودي/السعودية) and category nouns (هيئة، صندوق، معاهدة، معركة، مبادرة، جامعة) shared between question and answer are not leaks — treating them as such would bar every Saudi-named entity from ever being an answer.
- For cross-row leaks, a mention matters only when it reproduces the other question's identifying relationship, not merely its name. "أبها، عاصمة عسير" restated another row's own framing and had to go; naming العلا as a trade-route waypoint has nothing to do with a different row's royal-commission framing and was fine.
- Naming something that is a 100-level answer elsewhere transfers no information, because the player already knew it. The test is whether hearing it tells them something they didn't know.
- Watch for leaks that aren't same-language: an English abbreviation in the question can decode to the Arabic answer (KSrelief → مركز الملك سلمان للإغاثة).
- Before submitting, read each question with the answer covered and check the answer's words aren't still visible in it. Re-run this on any row you reword for a Pass 1 reason too — a fix aimed at one pass routinely breaks another.
- **Process-of-elimination leak.** A question must not use as a reference point an entity that is both (a) the same kind of thing as the answer and (b) a plausible wrong guess — ideally the most plausible one. Naming such an entity as a landmark silently eliminates it and does the player's narrowing for them; it works by removing an option rather than revealing one, which is why it's easy to miss next to the standard same-row and cross-row leaks above. The clear case: "العاصمة الأولى لآل سعود، الواقعة قرب الرياض" → الدرعية, where الرياض is a city, the answer is a city, and it is the single likeliest wrong guess because people assume the current capital was always the capital. Both conditions must hold — the rule is narrow by design. A reference of a different category is normal, legitimate clueing and should not be removed: a project west of Riyadh, a university north of Jeddah, a historic district within Jeddah. Nor does a same-category reference matter when it was never a credible answer — naming Mecca in a mild-climate question eliminates nothing, since Mecca's heat is well known. Check the difficulty consequence too: a row that needed this fix was easier than its tier implied while the distractor was being eliminated for the player, so re-check its tier after fixing.

**Facts (Pass 1):**
- Sourcing is tiered. Political, military, institutional and legal history has dense state-published sourcing (Saudipedia, SPA, الدرر السنية, the official gazette). Crafts, folk vocabulary, regional attribution and trade-route lore are covered mostly by lifestyle journalism that paraphrases itself, drifts on regions, and sometimes grafts a UNESCO listing onto the wrong property. In the soft lanes, require an institutional source or question identity and function only — not region, date or listing status.
- For every "first", "largest" or "only", check whether a sourced rival claim exists.
- Watch for entities that have been renamed, merged or superseded, and anchor the question to the era you mean (e.g. a body later elevated to an agency, or a number later superseded by a unified one).
- Where several names or variants are genuinely in use, pick one and list the others in note as acceptable.

**Scope:**
- A landmark, object or practice of Saudi Arabia belongs here. A fact that is true independently of Saudi Arabia and merely happens to be located in it does not — the Hajj month belongs elsewhere, كسوة الكعبة belongs here.
- Human ruling (2026-10-04): a heritage item shared across the Gulf or Arab world stays in السعودية only if it passes one Saudi-specific test: Saudi-named, Saudi-promoted by a Saudi institution or campaign, or tied to a Saudi region, place or institution named in the question. Being common in Saudi life or part of shared Gulf heritage is not enough.

**Process:**
- Read level breakdowns out of the file rather than deriving them from a previous message. A wrong breakdown that sums correctly is the easiest kind to miss.
- Approved rows are frozen by default; reopening one is reserved for structural problems (e.g. an approved answer is a common name, like a king, that keeps colliding with new rows' required context) — not for optional polish.

### Operational heuristics — كاس العالم (from human spot-check, 2026-10-08)

**Difficulty / clueing (Pass 2 + Pass 3):**
- Don't include an identifying hint (nationality, club affiliation, team name) that isn't needed for a single interpretation and that pushes the question below its tier's intended difficulty. If the match/teams are already named in the question, restating a player's nationality is redundant and an easy giveaway — drop it. Example: "...اللاعب الأرجنتيني الذي سجل هدف بلاده... في مباراتها أمام السعودية..." → drop "الأرجنتيني" once the match is already stated as السعودية-الأرجنتين.
- Club-affiliation descriptors ("نجم برشلونة الشاب", "حارس مرمى الهلال") that aren't needed to pin down who's being asked about make a 100-level question too easy — cut them so the player has to know the World Cup moment itself, not just recognize a famous club name.
- On a notorious/iconic incident (a famous foul, bite, miss), check whether a "flavor" clue (team name, nationality) is doing work the incident's own fame should already be doing. If the incident alone is identifying, cut the clue — keep the points unchanged.
- Don't bury the actual subject behind a secondary participant's action. Ask directly for the who/what/how many/when of the event itself ("من اللاعب الذي أضاع ركلة جزاء في مباراة فرنسا والمغرب بكأس العالم 2026؟") rather than wrapping it around what someone else did to them ("نجم فرنسا الذي تصدى [الخصم] لركلة جزاء سددها").

**Concision (rule 8):**
- Drop confirmation/announcement dates that don't narrow the answer (e.g. "التي أكد الفيفا في ديسمبر 2024م أنها ستستضيف..." → "من هي الدولة التي ستستضيف كأس العالم 2034؟"). Ask for the fact directly.

**Scope:**
- A كاس العالم question must be about the match, tournament, players, or records themselves — not a participating country's own domestic/civic reaction to a result (e.g. a public-holiday announcement). That's out of scope entirely for this section, regardless of how it's worded.

**Topic selection (Pass 3):**
- Avoid trivial physical/design-detail trivia about the trophy or ceremony objects that doesn't answer a real who/what/how many/when about the tournament (e.g. "ما الشكل الذي يحمله اللاعبان المجسّدان في أعلى الكأس؟"). Prefer facts actually about the competition.

**Anchor years (Pass 1 + Pass 2):**
- Any "up to [year]" record/"only team to..." question must be anchored to the LATEST tournament actually covered by the section's content, not a stale earlier cutoff. Now that 2026 is covered, re-check every existing anchor-year superlative and update stale ones (e.g. "...حتى نسخة 2022م؟" for a still-true-in-2026 fact → "...حتى نسخة 2026م؟").

**Facts must match the exact edition named (Pass 1):**
- Verify the fact is true for the SPECIFIC tournament year stated, not just true in general. A real honor/award from one World Cup must not get reattributed to a different edition, especially when the same team/player appears in both — re-verify with search against the exact year before approving.

**500-tier variety:**
- Don't default every 500 to pre-1970/historical obscurity. Most current 500s cluster on very old history (1900s-era facts), which is one valid path but not the only one — and over-clustering on it violates rule 6 (spread across the topic).
- A second valid path to 500: a small, exact, verifiable detail from a RECENT match that's hard to remember or notice even though it isn't old — e.g. naming the specific players who missed penalties in a shootout, who was subbed on at a specific minute, who conceded a specific own goal. These are hard because almost no one tracks that level of detail afterward, not because the event is obscure or old. Human's example: "من هم اللاعبين الذين أضاعوا ضربات الترجيح في مباراة كولومبيا وسويسرا في كأس العالم 2026؟"
- When the answer to this style of question is a small set of multiple people (e.g. 2 players who both missed), that's fine and is NOT an "X or Y" violation of rule 2 — rule 2 bars uncertain/alternative answers, not a complete, exact, verifiable set. Keep the set small (2-3 max) and make sure every name in it is independently verified.
- Apply this going forward on any NEW or backfill 500-point كاس العالم rows (including ones you write to replace a count lost from this resweep) — don't reopen already-approved 500s just to diversify them, that's optional polish, not a structural fix.

## Question rules
1. Arabic (فصحى بسيطة), clear wording, only one possible interpretation.
2. One correct answer, short (1–4 words). No "X or Y" answers.
3. The answer must not appear in, or be obvious from, the question — no hints of any kind (Core rule A).
4. Verifiable facts only. No opinions, no disputed matters, nothing likely to change (current office holders, records) unless the question includes a date.
5. No duplicates — within the section or across sections (rephrased versions count as duplicates).
   Check with the Grep tool, not by reading files (see Token efficiency).
6. Spread questions across the whole topic of the section; don't cluster on one sub-topic.
7. Follow the section's notes in `sections.md`.
8. Keep questions concise: include only the clues needed to identify the answer. Drop official-name expansions, dates, and descriptors that don't narrow the answer. Apply the clause test (Core rule A) — but never cut a detail that keeps the answer unique (Core rule B).
9. The question must be centrally about its section (Core rule C).
10. 500 questions follow the mix in Core rule D.

## Image rules (optional)
Images are optional — add one only when it genuinely helps the question or the answer.
1. Must be a direct link to the image file (ends in .jpg / .png / .svg / .webp), not a page that contains it.
2. Prefer stable sources: Wikimedia Commons (`upload.wikimedia.org`). For country flags, `flagcdn.com` is also fine.
3. No images from social media, news sites, or search-result thumbnails — those links break.
4. A question image must not reveal the answer.
5. The link must be checked and confirmed to load the correct image before approval.

## Token efficiency (human, 2026-10-15)
These rules cut cost without lowering quality. Follow them on every batch.

**Duplicate checks — Grep, never full reads**
- Never read whole `staging/*.csv` files to look for duplicates. As the project grows they become hundreds of thousands of tokens.
- For each new row, Grep across `staging/*.csv` for:
  1. the answer (and its main variant, e.g. with/without "ال"), and
  2. 1–2 distinctive key terms from the question (a name, place, event).
- Read only the rows Grep returns, and judge whether they ask the same thing.
- A rephrased duplicate shares its answer or its key subject, so these two searches catch it.

**Read only what you need**
- writer and reviewer read only the current batch's rows (filter by `status`), not the whole section file.
- Read a file once per pass; don't re-read it after every small edit.

**Short messages**
- reviewer lists ONLY the rows with problems, then ends with one summary line: `pass 2: rows 1–50 — 44 OK, 6 issues`. Do not write `row N: OK` for each passing row.
- writer replies only with what changed or a counter-argument — no restating of the rows.

**Searching**
- Use WebSearch first; open a page with WebFetch only when the search snippets don't settle the fact.
- One good source is enough when it's authoritative (official site, Wikipedia with citation, the relevant wiki for TV/film). Add a second source only when the first is weak or sources conflict.
- No searches for 100-point rows unless there's real doubt (as in Pass 1), except where `sections.md` requires every row to be searched.

**Images**
- Open each image once to check it, and again only after an edit. Don't re-open approved images.

## Workflow
1. Work one section at a time, in the order of `sections.md`.
2. writer adds questions in batches of 50 rows with `status=pending`, then messages reviewer.
   Before sending, writer self-checks every row: scope (Core rule C), clause test and cover test (Core rule A), one answer only (Core rule B), and counts the batch's 500 mix (Core rule D). Fix before sending — don't leave it to the reviewer.
3. Each batch goes through 3 review passes, in order. Each pass checks ONLY its own focus (see below).
   A row moves forward only when it passes: `pending` → `pass1_ok` → `pass2_ok` → `approved`.
4. In every pass, reviewer replies with problem rows only, plus one summary line (see Token efficiency):
   - `row 7: wrong answer — correct is X — source: <link>`
   - `row 9: points mismatch — this is 100, not 500`
   - `pass 1: rows 1–50 — 47 OK, 3 issues`
5. writer fixes or replies with a counter-argument, then updates status.
   If a fix changes the question or answer, the row goes back to `pending` and restarts from pass 1.
6. Disagreements: max 2 rounds per row per pass. If still unresolved, writer sets `status=flagged` and writes both views in `note`.
7. When a section reaches its counts, reviewer tells lead it is done, and the team moves to the next section.

## Review passes
Treat each pass as a fresh check — do not assume a row is correct because it passed an earlier pass.

### Pass 1 — Scope gate, then factual accuracy
- FIRST, before any search: is the row centrally about the section (Core rule C)? If not → `row N: out of scope — delete`. Do not verify facts for it and do not suggest a rewording. When unsure, reject.
- Verify the answer is correct and is the only correct answer.
- Use web search for every 300 and 500 question, and for any 100 question with the slightest doubt. Never approve a doubtful fact from memory alone.
- Reject facts that are disputed or likely to change (rule 4).

### Pass 2 — Difficulty
- Check the points match the difficulty definitions and reference examples.
- Check the 100 / 300 / 500 levels in the batch are clearly different from each other.
- Check a 500 question is hard because of knowledge, not confusing wording.
- Check a 500 question is hard because few people RECALL the answer — not because the event is old. A 500 that is hard only because it is from the early 1900s (and nobody would know it however interested they are) is rejected or replaced.
- Count the batch's 500 mix against Core rule D (pre-2000 share, recent share, year-as-answer share). If the batch breaks it, say which rows to replace: `batch: 500 mix fails — 6/10 pre-2000; replace rows X, Y, Z with recent-detail questions`.
- If a hint was removed in Pass 3 of an earlier round, re-check the tier: a row that was leaning on a hint was easier than it looked.

### Pass 3 — Wording and duplicates
- One possible interpretation only; clear Arabic. Not vague — if the question allows a second valid answer, it fails (Core rule B).
- The answer is not in, or obvious from, the question.
- Run the clause test and the cover test on EVERY row (Core rule A). For each hint, name it: `row 12: hint — "الملقب بالدون" points to the answer; cut it`. A row passes only with zero hints.
- Length check: if a question is longer than ~15 words, justify each clause with the clause test or cut it.
- Answer is short (1–4 words), no "X or Y".
- No duplicates or rephrased duplicates across `staging/*.csv` — checked with Grep (see Token efficiency), not by reading the files.
- Questions are spread across the section's topic, not clustered.
- Images (if any): link loads, shows the right thing, follows the image rules, and the question image doesn't reveal the answer.
- Scope (second check, after rewording): the row is still centrally about its section per Core rule C and sections.md — not a general fact that merely happens to be located in, or involve someone from, the section's subject. (For السعودية: a Saudi landmark, object, practice or person, not a general fact that happens to be on Saudi territory.)