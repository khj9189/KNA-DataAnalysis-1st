# 실습 1.

# name = input("이름:")

# print("안녕하세요" + name + "님")

# 실습 2.
# # int 변환은 계산 하기전에 되어 있어야 하므로 print에서 int로 바꿔주는 것은 늦다.
# # 전에 미리 int로 정수형으로 바꿔줘야 한다.

# birth = int(input("태어난 해:"))

# age = 2026 - birth + 1

# print(age)


# 실습 3.

# con = input("거주국가: ")
# cit = input("거주도시: ")
# print(f"{con}의 {cit}에서 거주하시는군요!")

# 실습 4.

# num_1 = int(input("a: "))
# num_2 = int(input("b: "))
# print("합:", num_1 + num_2)

# 실습 5.

# temp = int(input("온도:"))

# print(temp > 80)
# print(temp >= 0)

# 실습 6.

a = int(input("점수1:"))
b = int(input("점수2:"))
c = int(input("점수3:"))

score = (a + b + c) / 3

print(score >= 60)
