import csv

path = r"C:\Users\Admin\Quest\staging\السعودية.csv"

with open(path, "r", newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    rows = list(reader)

header, data = rows[0], rows[1:]
assert header == ["section", "question", "answer", "points", "question_image", "answer_image", "status", "note"]
assert len(data) == 15

# Fix 1: row 14 (جزيرة فرسان الكبرى) points 500 -> 300
assert data[13][2] == "جزيرة فرسان الكبرى", data[13]
data[13][3] = "300"

# Fix 2: row 15 (جبل السودة) reword question to ask about "جبل" not "قمة"
assert data[14][2] == "جبل السودة", data[14]
data[14][1] = "ما اسم أعلى جبل في المملكة العربية السعودية؟"

# Fix 3: row 12 (يو إس إس كوينسي) replace with Wadi Al-Rummah question (Saudi-specific, 500 pts)
assert data[11][2] == "يو إس إس كوينسي", data[11]
data[11][1] = "ما اسم أطول وادٍ في المملكة العربية السعودية؟"
data[11][2] = "وادي الرمة"

with open(path, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("fixed rows 12, 14, 15")
for i, row in enumerate(data, start=1):
    print(i, row[1], "->", row[2], "(", row[3], ")")
