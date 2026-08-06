# ① csv를 import
# ② with open으로 w·utf-8·newline 옵션으로 열기
# ③ csv.writer로 writer 객체를 만들기
# ④ writerow로 헤더와 각 데이터 행을 쓰기

import csv
import os
import sys

csv_path = os.path.join("data", "result.csv")
with open("csv_path", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["설비ID", "시각"])
    writer.writerow(["PRESS-01", "2022-07-12 00:00:00.019"])
