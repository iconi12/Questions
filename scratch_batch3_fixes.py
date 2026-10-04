# -*- coding: utf-8 -*-
import csv

path = r"C:\Users\Admin\Quest\staging\السعودية.csv"

with open(path, "r", newline="", encoding="utf-8-sig") as f:
    rows = list(csv.reader(f))

header = rows[0]
data = rows[1:]

def row_at(file_line):
    return data[file_line - 2]

# sanity anchors
assert row_at(112)[2] == "999"
assert row_at(114)[7] == "11-20 نوفمبر 2021"
assert row_at(119)[7] == "4 يونيو 1913"
assert row_at(120)[2] == "1920"
assert row_at(121)[7] == "استسلم 31 أكتوبر 1921"
assert row_at(122)[7] == "7 يناير 1926"
assert row_at(127)[1] == "ما الاسم الذي عُرفت به المؤسسة العامة للبترول والمعادن السعودية، التي تأسست عام 1962م؟"
assert row_at(129)[2] == "درب زبيدة"
assert row_at(130)[2] == "ميناء الملك عبدالعزيز"

# row 112: 999 is not the only correct answer -- anchor to the unified number instead
r = row_at(112)
r[1] = "ما الرقم الموحد للطوارئ في السعودية؟"
r[2] = "911"
r[7] = "وحّد الطوارئ العامة منذ 2017"
r[6] = "pending"

# row 114: note-only fix (actual inaugural dates were 6-15 December 2021, not November)
row_at(114)[7] = "6-15 ديسمبر 2021 (جدة التاريخية)"

# row 119: note-only addition (accepted fuller name)
row_at(119)[7] = "4 يونيو 1913؛ يُقبل أيضاً: معركة ضم الأحساء"

# row 120: ambiguous year (depends on what counts as "عسير") -- anchor to the commander instead
r = row_at(120)
r[1] = "من هو القائد السعودي الذي تقدم بقواته واستولى على أبها، عاصمة عسير، عام 1920م؟"
r[2] = "عبدالعزيز بن مساعد بن جلوي"
r[7] = "بعد معركة حجلا"
r[6] = "pending"

# row 121: note-only fix (fall of Hail was 2 November 1921, not 31 October)
row_at(121)[7] = "سقطت حائل في 2 نوفمبر 1921 (29 صفر 1340هـ)"

# row 122: note-only fix (bay'ah was 8 January 1926, not 7 January)
row_at(122)[7] = "8 يناير 1926 (24 جمادى الآخرة 1344هـ)"

# row 127: question spelled out "البترول والمعادن" which is literally what بترومين contracts -- ask by function instead
r = row_at(127)
r[1] = "ما الاسم الذي عُرفت به الهيئة الحكومية السعودية التي أُنشئت عام 1962م لتولي أنشطة التعدين وتسويق المشتقات النفطية خارج نطاق عمليات أرامكو؟"
assert r[2] == "بترومين"
r[6] = "pending"

with open(path, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("fixes applied, row 129 (درب زبيدة) still present -- removed in next step")
