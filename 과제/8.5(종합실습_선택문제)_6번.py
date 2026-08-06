# 단계
# ① os를 import하고 listdir로 폴더 목록을 구하기
# ② for-if로 .csv로 끝나는 이름만 빈 리스트에 모으기
# ③ 모은 csv마다 path.join으로 전체 경로를 만들기
# ④ 골라낸 csv 목록을 출력
# 예상 결과
# [CSV] 목록 (csv 파일만)

import os

csv_list = []

folder_list = os.listdir()
for folder in folder_list:
    if folder.endswith(".csv"):
        csv_list.append(folder)
path_list = []
for csv in csv_list:
    path_list.append(os.path.join(os.getcwd(), csv))
print(path_list)
