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
  - Columns: `section, question, answer, points, question_image, answer_image, question_video, answer_video, status, note`
  - `question_image` and `answer_image` are optional image URLs (leave empty if none).
  - `question_video` and `answer_video` are optional clip FILENAMES, not paths or links (e.g. `ksa-500-017.mp4`) — see Video and audio rules. Leave empty if none.
  - `status` is one of: `pending`, `pass1_ok`, `pass2_ok`, `approved`, `flagged`
- `questions.xlsx` — final output, built by lead with openpyxl from `approved` rows only.
  - One sheet per section, columns: `السؤال | الجواب | النقاط | صورة السؤال | صورة الجواب | مقطع السؤال | مقطع الإجابة | ملاحظات أو أجوبة مقبولة`, sorted by points. The last column carries the row's `note` for approved rows that have a host-relevant one (accepted variants, explicit wrong-but-tempting answers, disambiguation) — leave it empty when there's nothing host-critical.
  - Plus a sheet `flagged` listing every flagged row with its note, for the human to decide.
- `upload/<section>.csv` — also built by lead, one per section, from the same `approved` rows. This is the file the human uploads to the game's admin panel, so its format is fixed:
  - encoding `utf-8-sig`, header row exactly: `question,answer,points,image,answer_image,video,answer_video`
  - `points` is 100 / 300 / 500; empty cells stay empty. No status, note or section columns.
- `media/<section>/` — every video file (and its poster image) used by that section. See Video and audio rules.
- `TROUBLESHOOTING.md` — a log of concrete problems agents have hit (mostly environment/tooling quirks and SAM 2/ffmpeg/whisper pitfalls in video production), how each was fixed, and how to prevent it recurring. Search it before spending time diagnosing a weird failure — it may already be known. Add to it (in the same Issue/Fix/Prevention format) whenever you hit a new problem worth remembering; if the fix also changes a standing process, update the relevant rule here in CLAUDE.md too — this file has the "why", CLAUDE.md has the rule.

## Quantity
- Minimum per section: 100 questions at 100 points, 100 at 300, 100 at 500 (300 total).
- Counts refer to `approved` rows. Keep writing until each level reaches 100 approved.

## Difficulty definitions
**Audience (human, 2026-10-16):** the people playing this game are mostly YOUNG Saudis (roughly 18–30). Judge every question by them — not by the average Saudi adult, and not by a specialist.
- What young Saudis follow is EASY for this audience: gaming and esports, football (Saudi league, European leagues, World Cup), social media, recent Saudi events and projects, current pop culture.
- Older history, traditional heritage and things older generations know from experience are HARDER for this audience than they would be for the general public.
- Human's calibration example: "من فاز ببطولة الأندية في كأس العالم للرياضات الإلكترونية 2024؟" → Team Falcons is **100**, not 500 — most young Saudi players know it.

Imagine 10 typical players of this game (young Saudis) hearing the question:
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
- **Pin every event to ONE occurrence (human, 2026-10-16).** If the thing asked about happened more than once — two teams meet twice a season, a tournament or award recurs, a ruler visited a place twice — the question must say which one: the leg (ذهاب / إياب), round, date, edition, or final score. A season or year alone is not enough when the event happened twice inside it.
  - ❌ من سجّل هدف النصر ضد القادسية في الدوري موسم 2025-2026؟ (they met twice that season)
  - ✅ من سجّل هدف النصر ضد القادسية في إياب الدوري موسم 2025-2026؟
  - A final score or "the only goal" is a valid way to pin a match: "من سجّل هدف المباراة الوحيد بين الأهلي والاتحاد في ذهاب الدوري موسم 2025-2026؟"

### B2. No opinion words (human, 2026-10-16)
- Do not use subjective words — أفضل، أعظم، أقوى، أجمل — in a question. They turn a fact into an opinion (rule 4) and can have more than one answer.
- Allowed only when they are part of an OFFICIAL award or a measurable record, and then name it: "من فاز بجائزة أفضل لاعب في الدوري السعودي موسم 2024-2025؟" ✅ / "من أكثر لاعب تسجيلاً..." ✅ (measurable).
- If removing the word leaves a complete question, remove it.

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

### Movie/TV-series/game sections (human, 2026-10-22) — applies to هاري بوتر، صراع العروش، ون بيس، هجوم العمالقة، ناروتو، بيتر كول ساول، بريكنغ باد، ذا بويز، إنفينسبل، مارفل، سيد الخواتم، ألعاب الفيديو، إلدن رينغ، ديزني وبيكسار، فرندز، سبونج بوب، سبيستون، كول أوف ديوتي بلاك أوبس زومبيز، مسلسلات رمضانية، دريم وركس, and any future section of this kind

**Question-form variety:** reading finished output, the human found too many rows asking "ما اسم..." (what is the name of...) and not enough asking about events, speech or actions. Write noticeably more rows as "ماذا حدث؟ / وش صار؟" (what happened), "ماذا قال...؟ / وش قال...؟" (what a character said), and "من فعل...؟" (who did something) — not just naming things. These event/action forms should clearly outnumber "ما اسم" rows in a section's output, not just appear occasionally alongside them. This is a going-forward instruction for new rows; it is not a reason to rewrite or delete rows already written or approved under the older mix. Reviewer: when checking a batch's spread (rule 6), also weigh its mix of question forms, not just its topic spread, and flag a batch where naming questions dominate.

**Answer format — Arabic + English for names (human, 2026-10-21/22):** when an answer is a name or title (character, person, place, spell, object, film/book/episode title) that has an established English form, put the English right in the answer field after the Arabic — e.g. "عباءة الإخفاء Invisibility Cloak", "يجب ألا أكذب I must not tell lies". The same applies to an EXACT line actually spoken on screen in the original language. It does NOT apply to a plain description, action or paraphrase of what happens, even one that's easy to translate — "أن يأكلوهما Eat them" and "ترتد عليه فيفقد ذاكرته Spell backfires" are both wrong, invented glosses of a summary, not names or real quotes. Test before adding English: would a fan recognize this exact text as the thing's actual established name, or as a line really said on screen? If you're translating/summarizing rather than citing something established, leave English out. This was first discovered as an over-correction in هاري بوتر (English got added to generic nouns like "Dragon" and "Cat", and to descriptions, before being caught and reversed) — apply the tightened version from the start in any new movie/series section.
**Judge the ANSWER, never the question (human, 2026-10-22):** a second over-correction pattern in هاري بوتر: English was added because the QUESTION mentioned a name or character, even when the ANSWER itself wasn't a name/title/quote. The question's content is irrelevant to this rule — a question can be packed with proper nouns while its answer is a plain description, and that answer still gets no English. Judge only what the answer text itself is, every time, independent of what the question asks about.

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
6. **(human, 2026-10-22) If the question image is edited/masked in any way** (cropped to hide a logo, blurred, watermark removed, etc. — this does not include a normal unedited photo), `answer_image` must be the raw, unedited version of that same image, so the answer visibly matches what was hidden. If the question image needs no editing, `answer_image` is optional as usual.

## Video and audio rules (optional)
Clips are optional, like images — add one only when watching or hearing it IS the question (a goal, a celebration, a voice, a song intro, a sound). Never add a clip as decoration. Clips are for السؤال وجوابه only; حروف has none.

**How the game uses them.** The CSV holds only the clip's filename. When the human uploads a section, they pick `upload/<section>.csv` AND all the files in `media/<section>/`; the admin panel matches each filename in the sheet to a file, compresses nothing, uploads them, and stores the links. A name in the sheet with no matching file, or two files with the same name, blocks the upload. So the filename is the only link between the row and the clip — get it exactly right.

**Filenames**
- Lowercase Latin letters, digits and hyphens only, then the extension: `ksa-500-017.mp4`. No spaces, no Arabic, no brackets.
- Unique across the WHOLE project, not just the section: start every name with the section's short code (pick one per section and list it in `sections.md`), then the points, then a running number.
- The answer clip of the same row adds `-a`: `ksa-500-017-a.mp4`.
- A poster image (the still shown before play) has the SAME name with `.jpg`: `ksa-500-017.jpg`. The panel attaches it automatically. Always provide one.
- In the CSV write the name only — never a path (`media/...`) and never a URL.

**Video format** — the game plays these on phones and TVs, including iPhone Safari:
- `.mp4`, video H.264 (`yuv420p`), audio AAC, with `faststart`. (`.webm` is accepted but avoid it; `.mov` / `.m4v` must be converted.)
- Max 720p, 30 fps.
- Length 5–15 seconds. Cut to the moment the question is about — no intros, logos or replays.
- Size: aim for under 1 MB, keep under 3 MB. Files over 25 MB are refused by the upload.
- Convert and make the poster with ffmpeg (one command each):
  ```
  ffmpeg -i in.mov -ss START -t SECONDS -vf "scale='min(1280,iw)':-2,fps=30" -c:v libx264 -preset slow -crf 27 -pix_fmt yuv420p -c:a aac -b:a 96k -ac 1 -movflags +faststart ksa-500-017.mp4
  ffmpeg -ss 1 -i ksa-500-017.mp4 -vframes 1 -vf scale=640:-2 -q:v 4 ksa-500-017.jpg
  ```
  If the sound is not part of the question (or would give the answer away), drop it: replace `-c:a aac -b:a 96k -ac 1` with `-an`.
- Check every file before marking the row: `ffprobe` shows `h264` + `aac` (or no audio), duration 5–15 s, and the size is under 3 MB.

**Audio-only questions** (a voice, a song, a sound effect)
- The game has no separate audio column. An audio question is delivered as an `.mp4` with a still picture over the sound, in the same `question_video` / `answer_video` column, with the same naming rules.
- Build it from the sound file and a cover image:
  ```
  ffmpeg -loop 1 -i cover.jpg -i sound.mp3 -c:v libx264 -tune stillimage -pix_fmt yuv420p -vf "scale=1280:-2" -c:a aac -b:a 96k -ac 1 -shortest -movflags +faststart ksa-300-042.mp4
  ```
- The cover must not reveal the answer: use a neutral image (the section's logo, a plain colour, or a ❓). Use the same cover as the poster `.jpg`.
- Length 5–15 seconds, like video. Start on the part that is asked about.

**Content**
- The question clip must not reveal the answer: no on-screen names, captions, scoreboards, jersey names or commentary that says it. Cut or crop them out, or mute the commentary. Run the cover test on the clip as well as the text.
- **(human, 2026-10-22) If a row has a `question_video`, it must have an `answer_video`** that shows or says the answer — no longer optional. The answer clip doesn't need masking/editing; it's there to visibly confirm the answer after the question clip.
- The question text still has to work: it says what to watch or listen for ("من سجّل هذا الهدف؟", "لمن هذا الصوت؟") and follows every question rule. The clip replaces a description; it does not replace the question.
- Record where each clip came from in `note` (link + timestamp). Use only material the project may use; no clips with a visible watermark of another channel.
- reviewer checks each clip in Pass 3 like an image: the file exists in `media/<section>/`, the name in the CSV matches it exactly, it plays, shows the right moment, and does not leak the answer.

### Football clip questions (human, 2026-10-20) — every football section
Applies to every section about football (كاس العالم، الدوري السعودي، الدوري الانجليزي, and any football section added later). These are three extra question formats on top of normal text questions. All the general clip rules above still apply.

**Where clips come from**
- The human puts the source goal clips in `media/<section>/raw/`. writer works only from those files — never downloads match footage. If the raw folder is empty, write text questions and tell the lead.
- `note` records the raw file name, the match (teams, competition, season, leg/round) and the minute of the goal.
- **Use the LIVE action, not the broadcast's replay** (human, 2026-10-21 — said twice, for both Format 1 and Format 2, so treat as a hard rule for every format). Broadcasts show a goal once live, then a "GOAL" graphic, then one or more zoomed/slow-motion replays from different angles, before returning to live play for the restart. Always cut from the LIVE moment — the real-time wide shot of the buildup and the goal as it actually happened — never from the replay, even though the replay is usually the cleaner, more cinematic-looking shot and is tempting to use for that reason. To tell them apart: scrub forward from well before the goal and find the FIRST time the "GOAL" graphic/score change appears — everything before that point in time is live; the replay angles come after it, however the footage is packaged in the file. A replay is also often recognizable on its own (a camera angle switch straight into a dramatic slow-in on the scorer, no crowd/stadium wide shot establishing it, sometimes a visible on-screen "replay" cue), but the graphic-timing check is the reliable one.
- Live wide shots usually carry a persistent scoreboard graphic (team names/abbreviations, score, clock) that a tighter replay angle often doesn't — check every candidate clip for this and crop or cover it (Format 2 especially; see below) rather than assuming a clean live shot has no on-screen text to deal with.
- Jersey nameplates are another text leak, not just the scoreboard: a player's surname is often printed on the back of his shirt and becomes legible the moment the camera gets close (e.g. a celebration run to the touchline/corner flag). This applies to Format 1 (it names the scorer directly) and Format 2 (naming him can out his team to anyone who knows which club he plays for) alike — end the clip before any shot gets close enough to read it, the same way you'd end before a clear face shot.
- **The `answer_video` is the same clip UNEDITED** (human, 2026-10-21): the `question_video` is the masked/blurred/grayscale/name-cut version built per the format below; `answer_video` is the same moment trimmed from the raw source with none of that applied — original picture (scorer visible, kits and teams in full colour, no masking or blur) and original commentary (names and all), so it plainly shows or says the answer. Same naming convention as any other clip (`-a` suffix, e.g. `spl-100-003-a.mp4`) and still needs its own poster, format/length/size checks, and "يحتاج سماع" note if it has commentary.

**Order of work — text first, video editing second (human, 2026-10-21)**
- Within a section, write the TEXT for every clip row before editing a single video: pick the raw clip, write the question, write the answer, fill in `note` (match, minute, format, planned `question_video`/`answer_video` filenames) — working from the raw footage as reference only, no masking/blurring/encoding yet. Only once every row's text for the whole section is written (and has been through as much of the normal pass 1/2/3 review as doesn't depend on the edited file existing — fact-checking, difficulty, wording, duplicates) does the section move to the editing phase.
- The editing phase — actually producing every row's `question_video`/`answer_video`/poster files — then runs through the section's rows **one clip at a time, not in parallel**. This isn't just a tidiness preference, it's a hardware constraint: see below.
- **Check the actual hardware before editing, don't assume it** — GPU model and free VRAM (`nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv`) and CPU core count. What that tells you:
  - Format 1 needs SAM 2 on the GPU. If the machine has a single GPU with limited VRAM (check — as of 2026-10-21 this machine has one RTX 4060 Ti with 8GB, of which only a few GB are free), running SAM 2 for more than one clip at the same time does not speed anything up: both jobs compete for the same VRAM, at best time-slicing with overhead (same or worse total time) and at worst one job runs out of memory and crashes. Masking jobs must be queued and run one at a time regardless of how many agents/workers exist, unless a future check finds multiple GPUs or enough spare VRAM to genuinely fit more than one job at once.
  - Format 2 no longer uses the GPU (just an OpenCV blur pass + ffmpeg encode) and candidate-sourcing/scanning/transcription are CPU work, not GPU work — on a machine with many CPU cores (this one: 20 cores/28 threads) that work has real room to parallelize without hitting the GPU bottleneck. But per the rule above, do the actual per-clip editing sequentially anyway, to keep the process simple and because Format 1's GPU step is the binding constraint for the section as a whole regardless of what Format 2 could do on its own.
  - If the hardware changes (more VRAM, multiple GPUs, a different machine entirely), re-check before assuming the sequential rule still applies — the rule follows from what the hardware can actually do, not from a fixed number.

**Format 1 — hidden scorer or hidden assist** → "من سجّل هذا الهدف؟" (hidden scorer) or "من صنع هذا الهدف؟" (hidden assist, human 2026-10-21 — "who made this goal", i.e. who provided the assist)
- Video of the goal with the commentator's audio.
- Hidden scorer: the scorer is replaced by a solid silhouette (pure white or pure black, whichever contrasts with the pitch better) that follows the player's EXACT outline in every frame — the body, legs and arms stay visible as a shape, so his movement, run and finish are clear. Not a box, not a blur. His name is removed from the commentary (see Commentary below), along with his nickname and anything that names him indirectly. Answer: the scorer's name.
- Hidden assist: same masking method, but applied to the player who provided the assist (the pass, cross, cutback or knock-down that led directly to the goal) instead of the scorer — he stays visible and audible as normal, he isn't the secret. Only the assist provider's name and nickname are removed from the commentary. Answer: the assist provider's name. Only use this version when the goal has one clear, single, identifiable assist — don't force it onto a scrappy goal (a deflection, a loose-ball scramble with no clean pass) or one with no assist at all (a solo run, a direct free kick, a penalty).
- Everyone else (besides whichever of the two is hidden) stays as they are — teams, kits and stadium are fair clues.

**Format 2 — hidden teams** → "من الفريقان في هذا الهدف؟" (or "لأي فريق هذا الهدف؟" — the question says which is asked)
- Video of the goal where the teams cannot be identified. **Do NOT use Format 1's per-player silhouette method for this** (human, 2026-10-21) — it means tracking every single person on screen individually, which in practice is slow, fragile (SAM 2 drift gets worse with more people and busier shots — see the Masking lessons below), and makes the clip's length hostage to however long one continuous untracked-by-a-cut shot happens to be. Instead:
  - Apply a whole-frame black-and-white (grayscale) filter to the entire clip (e.g. ffmpeg `hue=s=0`) so kit colours can't be told apart. No per-player tracking or masking needed — every person on screen is covered by the same filter automatically, however many of them there are and for the whole clip.
  - Grayscale alone is not enough (human, 2026-10-21): colour is gone but a kit's PATTERN survives it — a striped or hooped kit still reads as striped/hooped in black and white, and a fan who knows "this team wears stripes" can use that to narrow down who's playing even with no colour and no names. **Also apply a light grayscale blur over the whole frame**, strong enough that kit pattern and jersey numbers stop being legible, but light enough that players and the ball stay clearly visible as sharp, trackable shapes — never blur so much that it's hard to tell where the players or the ball are. There's no single correct blur number; it depends on the source resolution and how close the camera is — tune it by eye against this test: can you still tell a striped kit from a solid one? If yes, it's not enough yet.
  - Check it actually hides the teams: open a frame and confirm the two kits don't still read as visibly different shades of grey (very light vs. very dark kits can still be told apart by brightness alone even without colour — if so, this clip/kit pairing doesn't work for Format 2, pick a different one), and that no kit pattern is still readable.
  - **The scoreboard needs its own, much HARDER blur, applied on top of the light whole-frame one** (human, 2026-10-21) — the light blur that's correctly calibrated for kit pattern is nowhere near strong enough to make broadcast scoreboard text illegible; test this separately, don't assume the whole-frame pass covers it. The scoreboard is a fixed-position overlay (same box in every frame of a given shot), so measure its bounding box once and apply a second, strong blur (e.g. ffmpeg `boxblur` or a masked heavier `gblur`, or do it in Python/OpenCV with `cv2.GaussianBlur` on just that region) only over that box. The same applies to any other on-screen team name, logo, crest or caption — a fixed graphic gets its own hard blur over its own box; don't rely on the whole-frame light blur to hide text or logos anywhere.
  - A solid colour box instead of blur also works and is simpler, but a blur reads as a more natural part of the shot (human preferred it, 2026-10-21) — use blur unless a specific graphic is awkward to blur cleanly.
  - If a fan banner, flag or sign with a team's colours/pattern shows up in the crowd and the whole-frame light blur doesn't fully obscure it, that's a case-by-case call — a harder, localized blur over just that area (tracked by position if it moves) is the same technique as the scoreboard fix. Detecting the pitch/grass boundary per frame (HSV threshold for green, blur everything above it) is a reliable way to isolate "the stands" from "the pitch" if a crowd-wide fix is needed, so the whole stands can get a harder pass without touching the players — reach for this only if a specific graphic is actually a problem, not as a default for every clip.
  - Commentary: remove every player name, team name, nickname and city that would reveal a team — or mute the audio entirely if too many remain. A commentator who names a star player by name alone (without a visible kit) is often enough on its own to reveal the team to an informed viewer, so treat a single clear name mention as reason enough to mute the whole clip rather than try to cut around it.
  - Because there's no per-player masking to hold together, Format 2 clips can freely use a longer continuous shot, or even span a hard camera cut, as long as nothing in any shot visibly identifies a team (colour or text) — this format is NOT bound by the "single continuous shot" constraint that Format 1's tracking needs.
- Answer: both teams (e.g. "الهلال والنصر"), or the one team if the question asks for one. A two-team answer is allowed (like the small-set rule in كاس العالم).

**Format 3 — commentary only** → "من سجّل هذا الهدف؟" or "من الفريقان في هذا الهدف؟"
- Audio only: the commentator describing the goal, built as an audio-only `.mp4` (see Audio-only questions above) with the neutral cover.
- Remove the scorer's AND the assister's names (and nicknames). For the "teams" question, also remove team names and anything naming a team.
- The commentary must still describe the goal enough to identify it — if the description is just shouting with nothing left after the cuts, don't use that clip.

**Masking the hidden player — scorer or assist provider (Format 1 only — Format 2 uses the grayscale method above, not this)**
- Same method whichever of the two is hidden for a given row (see Format 1 above) — everything below just says "the hidden player" or "him" for whichever one it is.
- Use video segmentation that tracks a person across frames — SAM 2 (Segment Anything 2) with the GPU. Mark the player on the first frame (a point or box), let it track, then paint the mask solid white/black and re-encode with ffmpeg.
- Mark the ANCHOR frame with several points spread across the body (head, torso, legs), not one point. A single point — especially one placed low — can bias the mask toward only that body part (e.g. legs only, with the torso/head left uncovered). Check the anchor frame itself at full resolution before trusting propagation from it.
- Check the mask: make ONE contact-sheet image of 12 frames spread across the clip (ffmpeg `tile` filter) and open it. Every frame must show the target fully covered — head, torso and legs, not just part of him — nothing leaking at the edges, and the silhouette following him (not a teammate, not the goalkeeper) after he crosses other players. If tracking jumps to another player or part of him is missing, re-mark and re-run. Don't rely on one wide contact sheet alone for a long or wide-angle clip — spot-check individual frames at full resolution, especially anywhere players cluster or cross.
- If the hidden player goes behind others or off-screen and the mask can't hold, cut the clip shorter or don't use it.
- End the clip before the celebration if the celebration shows his face, shirt name or number up close.
- **Anchor as early as possible and propagate forward, not backward.** SAM 2's tracking is not symmetric in practice: propagating backward from an anchor placed near the goal/kick (to cover the earlier buildup) can drift onto empty background or a different player within a handful of frames, especially in a wide/full-pitch shot where the target is small and surrounded by similar-looking teammates — even when forward propagation from that same anchor stays reliable much further. Place the anchor at or near the first frame of the clip and propagate forward through the whole thing. Do not assume a stretch of the clip "doesn't need" masking because the hidden player looks too small or indistinct to identify at that scale — verify it, don't assume it; he must be covered everywhere he's on screen, including the deep buildup.
- When it's hard to tell by eye which of several similar players in an early, wide-shot frame is the one to hide, validate a candidate before committing to a full run: place the candidate point, propagate forward only a short distance to a frame where his position is already confirmed (e.g. from a point you already verified visually), and check the resulting mask's centroid lands on/near that known position. A correct candidate converges almost exactly; a wrong one drifts or lands on someone else. This is far cheaper than guessing and finding out only after a full-length run.
- Prefer a clip that shows the move, not just the finishing touch in isolation — include the pass or cross that set up the goal where the footage allows it, trimmed to a single continuous camera shot (see the cut rule above). A tight replay of only the final touch is a worse question clip than one that also shows how the chance came about.

**Removing names from commentary (all formats)**
- Transcribe the clip with word timestamps (faster-whisper, Arabic) and find every word to remove: the name, nicknames, short forms, and repeated or drawn-out shouts of the name ("رونالدووو").
- **Cut the word out and close the gap — do not silence/mute it in place.** Muting leaves a dead pause where the commentator appears to freeze mid-sentence, which sounds broken. Instead remove that span of audio entirely and join what comes immediately before it to what comes immediately after, so the remaining words run into each other naturally with no gap.
- The commentary must keep going for the whole clip — never let it go silent for an extended stretch, and especially not over the climactic moment (the kick/goal itself, or the celebration). If cutting the name leaves too little speech to fill the clip, look again at what's left rather than defaulting to padding the rest with silence: only cut audio that is plausibly the name, a nickname, or a drawn-out shout OF the name — a prolonged inarticulate shout that doesn't contain the name's actual sounds (e.g. no match to its distinctive consonants) is very likely just a cheer, not the name, and should be kept so the commentator keeps reacting through the exciting part of the clip.
- Whisper often mishears names. Read the full transcript yourself and treat any word that could be the name as the name — but weigh this against the point above: "could be the name" means it's phonetically plausible, not just that it's shouted or unclear.
- Before finalizing, check the edited audio's duration against the clip's: if it ends well short of the video, that's a sign too much was cut (or the wrong fallback was used) — fix the edit instead of padding the gap with dead air over live action.
- Agents cannot listen. Every row with commentary audio gets "يحتاج سماع" in `note`, and lead lists it in the `audio_check` sheet for the human to listen before upload.

**Sourcing the clip**
- Check the commentary language on a candidate source BEFORE building anything on it, not after — prefer an Arabic-commentary broadcast (the official club or league channel is a good first place to check) over whatever source is quickest to find.

**Difficulty**
- Same audience scale. A goal the whole country talked about (a derby winner, a World Cup goal) is 100 even when masked; a goal from a mid-table match is 300–500. Format 2 (teams) is usually easier than Format 1 for a famous match and harder for an ordinary one.

**Checks (reviewer, Pass 3)**
- Format 1: open the contact sheet — the mask is correct in every frame, full body, not just part of him — and nothing on screen names the answer. Spot-check individual frames at full resolution where players cluster, not just the contact sheet thumbnails.
- Format 2: open a frame and confirm it's genuinely black and white (no colour channel left), the two kits don't still read as different shades of grey, and kit PATTERN (stripes/hoops) isn't legible either — grayscale alone leaves pattern intact, it needs the whole-frame blur too. Separately confirm the scoreboard and any other on-screen team name/logo/crest has its own hard blur (or a cover) strong enough that it's fully illegible, not just the same light blur as the rest of the frame.
- Read the transcript of the FINAL clip (re-transcribe the output, not the original): no name, nickname or team word that should have been removed is still there.
- Listen for dead air: the edited audio should run close to the clip's full length and the commentator shouldn't go silent mid-clip or over the climactic moment (flag it for the human's "يحتاج سماع" check either way, but a visibly short edited-audio duration vs. the clip length is a build defect to send back, not just a listening item).
- Format, length and filename checks as for any clip.

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
- Judge every row by the AUDIENCE: young Saudis (see Difficulty definitions). For each row ask: "Would most young Saudi players know this?" Don't rate as if the players were specialists or the general adult public. A fact young Saudis widely know (gaming, esports, football, recent Saudi events) cannot be 500 just because older people wouldn't know it.
- Check the points match the difficulty definitions and reference examples.
- Human corrections are the strongest calibration (human, 2026-10-16). In the first review of الدوري السعودي, the human changed the points of about 45 rows — 34 of them 300/500 → 100. Before Pass 2 on any section, read that section's human calibration notes in `sections.md` and rate in line with them.
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
- Clips (if any): the file is in `media/<section>/` under exactly the name in the row, passes the format check, plays the right moment, and the question clip doesn't reveal the answer (see Video and audio rules).
- Scope (second check, after rewording): the row is still centrally about its section per Core rule C and sections.md — not a general fact that merely happens to be located in, or involve someone from, the section's subject. (For السعودية: a Saudi landmark, object, practice or person, not a general fact that happens to be on Saudi territory.)