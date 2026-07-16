# # 실습 1.

# a = "PUMP_A"
# b = "정상"
# c = 1200
# d = "2026-07-16"

# # a,b,d는 이미 문자열이어서 + 연산자와 연결할 때 문제가 없지만
# # c는 int이기에 +연산자와 연결해주기 위해서는 str으로 감싸줘야 한다.
# cord = "설비:" + a + "\n상태:" + b + "\n가동:" + str(c) + "\n점검:" + d
# print(cord)


# # 실습2.

# a = "temp_sensor"

# print(a[:4])

# # 실습 3.

# a = "temp_sensor"

# print(a[5:])

# 실습 4.

# a = "sensor_01"
# print(a[-2:])

# 실습 5.

# a = "PYTHON"
# print(a[::2])

# 실습 6.

a = "PYTHON"
print(a[::-1])
