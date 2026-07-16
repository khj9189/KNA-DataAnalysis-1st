# 실습1.

a = 17
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**b)

# 실습2.

a = 1
b = 2
c = 3

print((a + b + c) / 3)
print(c**2)
print(a * b * c)


# 실습 3.

print("a" == "a")  # True
print("a" != "a")  # False
print(15 > 10)  # True
print(15 < 10)  # False
print(15 >= 10)  # True
print(15 <= 10)  # False

# 실습 4.

temp = 85
temp_ok = 60 <= temp and temp <= 90
print(temp_ok)

prs = 5
prs_ok = 3 <= prs and prs <= 7
print(prs_ok)

print(temp_ok and prs_ok)


# 실습 5.

stock = 100
print(stock)

stock += 50
print(stock)

stock -= 30
print(stock)

stock += 5
print(stock)


# 설비 6.
# 주의: 불량률 같은 백분위 수에는 100을 추가로 곱해준다.

total = 500
defect = 23
defect_rate = (defect / total) * 100
print(defect_rate)

operate = 21
total_OperateHour = 24
operate_rate = (operate / total_OperateHour) * 100
print(operate_rate)


# 설비 7.

total_min = 500

hour = total_min // 60
min = total_min % 60
print(f"{hour}시간 {min}분")
