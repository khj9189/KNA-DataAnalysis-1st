# ===============================================================
print("=== while ===")

# while은 특정 조건이 False가 될 때까지 반복해야 하는 경우 사용

# 종료 조건이 거짓이 되는 플래그를 꼭 세워야 함/특정 조건이 없기에 실행이 계속 진행된다.
# count = 1
# while count < 3:
#   print(count)

# while 문 사용 체크리스트
# 1. 반복 전 변수(시작값) 선언 여부
# 2. 반복을 하다가 언젠가 False가 될 수 있는 종료 조건을 포함하는지
# 3. 변수가 거짓 방향으로 값이 변경되는지

# count = 1 # 1번
# while count >= 1: # 2번
#   count = 0 # 반복문 안에 count 변수를 계속 0으로 재할당해서 무제한 반복복
#   print(count)
#   count += 1 # 3번

# answer = 7  # 정답: 예시
# guess = 0
# while guess != answer:
#     guess = int(input("맞혀 보세요: "))
# print("정답입니다!")

# ===============================================================
print("=== break ===")

# while True:  # 기본은 계속 반복
#     x = input("입력 (q=종료): ")
#     if x == "q":  # 종료 신호면
#         break  # 빠져나옴
#     print("입력:", x)

# 예시 1.
# 값의 누적이 15를 넘은면 중단

# input_sum = 0

# while True:
#     user_input = int(input("값을 입력하세요. 값의 누적이 15를 넘은면 중단"))
#     input_sum += user_input
#     if input_sum > 15:
#         print("누적합계:", input_sum, "입력을 종료합니다.")
#         break
# print("break를 통해 while문을 나가면 이후 코드가 실행된다.")

# 사용자 입력값을 확인만하고 저장할 필요가 없는 경우

# while True:
#     x = input("입력(종료는 q를 입력하세요):")
#     if x == "q":
#         break
#     print("입력받은 값:", x)

# n = int(input("횟수: ")) # 측정값을 입력받는 횟수를 정해주는 과정에 해당
# for i in range(n):
#   v = int(input("측정값: "))
#   if v > 80:
#     print("이상")
#     break
#   else:
#     print(v, "정상")


# ======================================

# first = int(input("1번째 입력값: "))

# # 첫 번쨰 입력값은 자동으로 최댓값이 됨(비교할 다른 값이 없기 때문)
# max_value = first

# # for문을 사용해서 사용자 입력을 4번 받고 입력받은 값 중에서 가장 큰 값을 출력

# for i in range(4):
#     v = int(input(f"{i+2}번째 입력: "))
#     # max value에는 현 시점 최댓값이 저장되어 있고
#     # v에는 방금 사용자가 입력한 값이 들어있다.
#     # max value와 v의 값을 비교해 더 큰 값을 max_value에 재할당
#     if v > max_value:
#         max_value = v
# print("최댓값: ", max_value)  # for 반복문 종료 후 최종 최댓값 출력
