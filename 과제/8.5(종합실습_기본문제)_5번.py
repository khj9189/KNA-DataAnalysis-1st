# 단계
# ① os와 datetime을 import
# ② listdir로 폴더 파일 수를 구하기
# ③ datetime.now로 현재 시각을 담기
# ④ f-string으로 파일 수와 시각을 한 문장으로 출력
# 예상 결과
# 파일 3개, 점검 시각 2026-… 형식 한 줄

import os
import datetime

file_list = os.listdir()
now = datetime.datetime.now()

print(f"파일 {len(file_list)}개, 점검 시각: {now}")
