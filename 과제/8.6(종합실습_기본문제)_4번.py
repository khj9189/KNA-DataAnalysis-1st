# 실습 4.

import csv
import os
import sys

csv_path = os.path.join("data", "08_press.csv")

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
