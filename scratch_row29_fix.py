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
assert row_at(29)[1] == "في أي شهر هجري يُقام موسم الحج سنوياً في مكة المكرمة؟"
assert row_at(38)[6] == "pending"
assert row_at(52)[6] == "pending"
assert row_at(58)[6] == "pending"

# rows 38, 52, 58 cleared all 3 passes -> approved
for ln in (38, 52, 58):
    row_at(ln)[6] = "approved"

# row 29: replaced per reviewer's suggestion (off-scope Hajj-month question swapped
# for a genuinely Saudi-specific national-title fact)
r = row_at(29)
r[1] = "ما اللقب الرسمي الذي يحمله ملك المملكة العربية السعودية منذ عهد الملك فهد؟"
r[2] = "خادم الحرمين الشريفين"
r[3] = "100"
r[6] = "pending"
r[7] = ""

with open(path, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

from collections import Counter
approved = [r for r in data if r[6] == "approved"]
print("total approved:", len(approved), dict(Counter(r[3] for r in approved)))
print("row29:", row_at(29))
