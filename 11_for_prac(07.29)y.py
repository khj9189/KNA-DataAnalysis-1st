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

for i in range(1, 10):
    if i % 2 == 0:
        print(f"--- {i}단 ---")
        for j in range(1, 10):
            mul = i * j
            print(f"{i} x {j} = {mul}")
