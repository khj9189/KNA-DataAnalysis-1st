# ====================================================================
print("=== csv.reader 구조 ===")

import os
import sys
import csv

csv_path = os.path.join("data", "result.csv")
with open(csv_path, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])

# ====================================================================
print("=== csv.DictReader ===")

csv_path = os.path.join("data", "08_press.csv")

# 위 경로의 파일을 찾지 못하면 종료
if not os.path.exists(csv_path):
    print("파일 찾았습니다.")
    sys.exit(1)  # 비정상 종료시 보통 0이 아닌 값(예 1)에 전달
print("파일이 있습니다.")

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["설비ID"], row.get("시각"))
