# 절대경로의 예: C:\Users\nedpark\바탕화면\sample\code.py
# 만약 C:\Users\nedpark\바탕화면\sample 폴더에 터미널을 연 상태에서
# code.py 코드를 실행하고 싶다면
# python code.py
# 위 code.py 언급 부분은 사실 상대경로를 의미한다.
# 그래서 절대 경로로 지정해줘도 똑같이 실행될 것이다.
# C:\Users\nedpark\바탕화면\sample\code.py
# 현재 경로에 있는 해당 파일이라는걸 더 강조하는 상대경로 지정으로 써도 된다.
# python ./code.py

# 만약에 C:\Users\nedpark\바탕화면\example 폴더 경로에서 위 코드를 실행하고 싶다면
# 절대경로 : python C:\Users\nedpark\바탕화면\sample\code.py
# 상대경로 : python ..\sample\code.py

# 표준 라이브러리의 os 모듈 활용
import os

current_working_directory = os.getcwd()
print(current_working_directory)

# 폴더 안 파일 · 폴더 이름을 리스트로 반환
file_list = os.listdir()  # 지금 내가 있는 폴더 속에 있는 파일명들을 제공해준다.
print(file_list)

for file_name in file_list:
    print(file_name)

# 파일이 존재하는지 알아보기
# 운영체제(윈도우/맥/리눅스)마다 경로를 나타내는 방법이 달라서
# 상황에 맞게 절대 문자열을 만들어주는 OS의 함수를 사용합시다.
path = os.path.join("data", "08_press.csv")

# 실제 경로문자열을 따라서 찾아가면 해당 파일이 있는지 알아봅시다: True/False
if os.path.exists(path):
    print(f"파일 있음: {path}")
