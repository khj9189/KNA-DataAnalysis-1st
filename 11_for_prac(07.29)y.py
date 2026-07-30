# 실습 1.

# N = int(input("정수:"))

# for i in range(1, N + 1):
#     print(i)

# for j in range(2, N + 1, 2):
#     print(j)

# for k in range(N, 0, -1):
#     print(k)

# 연습문제 1.

# 3,6,9를 포함한 숫자만 출력하기

# n = int(input("369시작: "))

# for i in range(1, n + 1):
#     if i % 3 == 0:
#         print(i)
#     elif i % 6 == 0:
#         print(i)
#     elif i % 9 == 0:
#         print(i)


# 실습 3.

# num = int(input("사용자 입력값:"))

# for i in range(1, num):
#     if i % 3 == 0:
#         print(i)

# 실습 4.

# for i in range(1, 10):
#     if i % 2 == 0:
#         print(f"--- {i}단 ---")
#         for j in range(1, 10):
#             mul = i * j
#             print(f"{i} x {j} = {mul}")


# 실습 1.

# temps = [25, 32, 28, 35, 19]

# for i in temps:
#     if i >= 30:
#         print(f"고온: {i}")
#     else:
#         print(f"저온: {i}")


# 실습 2.

# opr = [8, 6, 10, 9, 11, 12, 13]

# for i in opr:
#     if i >= 5 and i <= 10:
#         print(i)


# 실습 3.
# temps = [25, 32, 28, 36, 27, 31, 24]
# total = 0
# count = 0
# for t in temps:
#     if t > 30:
#         total += t
#         count += 1
# print("고온 평균:", total / count)


temps = [25, 32, 28, 36, 27, 31, 24]
sum = 0
num = []

for i in temps:
    if i > 30:
        sum += i
        num.append(i)
        avg = sum / len(num)
print("합:", sum, "개수:", len(num), "고온평균:", avg)
