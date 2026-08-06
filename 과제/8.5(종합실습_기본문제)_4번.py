# 단계
# ① os를 import
# ② path.join으로 폴더와 파일 이름을 이어 경로를 만들기
# ③ path.exists로 그 경로가 있는지 참·거짓 확인
# ④ if로 있으면·없으면 다른 메시지 출력
# 예상 결과
# True 또는 False / 파일 있음 또는 파일 없음

import os

path = os.path.join("과제", "8.3(종합실습)_2번.py")
if os.path.exists(path):
    print("True")
else:
    print("False")
