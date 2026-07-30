# 실습 1.

# age = int(input())

# if age >= 19:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")

# 연습문제 1.

# 숫자 맞추기 게임

# 정답을 50으로 지정, 사용자에게 입력값을 받기 -> 사용자 입력값이 정답과 동일하다면 정답입니다.

# ans = 50

# input으로 입력받은 것들은 모두 문자열이므로 int 를 통해 정수형태로 바꿔줘야 한다.

# q = int(input())
# if q == 50:
#     print("정답입니다.")
# else:
#     print("틀렸습니다.")

# print("게임이 종료되었습니다.")

# 실습 2.

# temp = int(input("측정온도:"))

# if temp > 80:
#     print("위험")
# elif 80 >= temp > 60:
#     print("주의")
# else:
#     print("정상")


# 연습문제2.

# color = input("신호등 색:")

# if color == "초록색":
#     print("건너세요")
# else:
#     if color == "빨간색":
#         print("기다리세요")
#     else:
#         print("다시 입력하세요")

#### Python은 들여쓰기(indent) 레벨로 짝을 정해요. else는 자기와 같은 들여쓰기 레벨에 있는 바로 위의 if와만 묶입니다.

# 연습문제3.
# 정상 체온 범위: 36.2 ~ 36.9

# user_a = float(input("체온을 입력해주세요:"))

# if user_a >= 36.2 and user_a <= 36.9:
#     print("정상체온입니다.")
# else:
#     if user_a > 36.9:
#         print("열이 나고 있습니다.")
#     else:
#         print("저체온입니다.")
# print("체온 판단 완료")


# 연습문제 4.
# user_a = float(input("체온을 입력해주세요:"))

# if user_a < 36.2 or user_a > 36.9: # if 문안에서는 중첩을 여러번 수행할 수 있다. 그러나 권장하는 방법은 아니다.
#     if user_a > 36.9:
#         print("열이나고 있습니다.")
#     else:
#         print("저체온증입니다.")
# else:
#     print("정상체온입니다. ")

# print("체온 판단 완료")


# 실습2. 설비 온도 상태 판정하기

# temp = int(input("온도:"))

# if temp > 80:
#     print("위험")
# elif temp > 60:
#     print("주의")
# else:
#     print("정상")


# 실습 3.

# ID = "posco"
# PW = "1234"

# ID_input = input("ID를 입력하세요:")
# PW_input = input("PW를 입력하세요:")

# if ID_input == ID and PW_input == PW:
#     print("로그인 성공")
# else:
#     print("로그인 실패")


# 실습 5. 세값으로설비종합상태판정하기(도전)

# temp = float(input("온도:"))
# vib = float(input("진동:"))
# elc = float(input("전류:"))

# if temp > 80 or vib > 4.0:
#     print("위험: 즉시 정지")
# elif elc > 60 and temp > 70:
#     print("주의: 부하 점검")
# elif vib > 2.5:
#     print("주의: 진동 관찰")
# else:
#     print("정상")
