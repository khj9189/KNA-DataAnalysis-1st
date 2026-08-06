# 단계
# ① os 모듈을 import
# ② getcwd로 현재 작업 폴더를 확인
# ③ listdir로 폴더 안 목록을 변수에 담기
# ④ for로 목록을 하나씩 출력하고 csv만 골라 출력
# 예상 결과
# 현재 경로 / 폴더 안 파일들 / .csv 파일만

import os

current_working_directory = os.getcwd()
print(current_working_directory)

file_list = os.listdir()
print(file_list)

for file_name in file_list:
    print(file_name)
