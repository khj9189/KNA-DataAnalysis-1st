# ===============================================================

# 실습 1.

# ans = 7
# guess = 0

# while guess != ans:
#     guess = int(input("guess: "))
#     if guess != ans:
#         print("목표값이 아니다")
# print("정답입니다.")


# ans = 7
# guess = 0

# while guess != ans:
#     guess = int(input("guess: "))
# print("정답입니다.")


# 연습문제 1.

# 1~50중 하나의 숫자를 정답으로 저장
# 사용자의 입력값 기준으로 정답이 up인지 down인지 출력
# 정답이 나오면 정답이고, 게임이 종료되었다고 출력한다

# ans = 14
# guess = 0

# while True:
#     guess = int(input("1~50 중 예측값 입력:"))
#     if guess == ans:
#         print("정답입니다.")
#         break
#     elif guess > ans:
#         print("down")
#     else:
#         print("up")
# print("게임이 종료되었습니다.")

# 연습문제 2.

# sum = 0

# while True:
#     num = int(input("값 입력:"))
#     if num > 5:
#         sum += num
#         print(f"참, 합계: {sum}")
#     elif num < 5:
#         if num < 5:
#             num = 0
#             sum += num
#             print(f"거짓, 합계: {sum} ")

# sum = 0

# while True:
#     num = int(input("값 입력:"))
#     if num > 5:
#         sum += num
#         print(f"참, 합계: {sum}")
#     else:
#         print(f"거짓, 합계: {sum}")


# 실습 2.

# found = False

# n = int(input("횟수: "))

# for i in range(n):
#     num = int(input("측정값: "))
#     if num > 80:
#         found = True
#         break

# if found:
#     print("발견")
# else:
#     print("없음")
