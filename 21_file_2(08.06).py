# ====================================================================
print("=== csv.reader 구조 ===")

import os
import sys
import csv

csv_path = os.path.join("data", "08_press.csv")

# 위 경로의 파일을 찾지 못하면 종료
if not os.path.exists(csv_path):
    print("파일 찾았습니다.")
    sys.exit(1)  # 비정상 종료시 보통 0이 아닌 값(예 1)에 전달
print("파일이 있습니다.")

with open(csv_path, "r", encoding="utf-8") as f:
    # print(f.readlines()) -> 이제 csv 전문가에게 맡긴다.
    reader = csv.reader(f)
    print(reader)  # <_csv.reader object at 0x00000247D33F2B60>

    for row in reader:
        print(row[0])  # 각 행마다 리스트로 출력됨
