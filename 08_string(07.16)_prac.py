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

# a = "PYTHON"
# print(a[::-1])

# 실습 7.

# num = "01012345678"
# print(len(num))

# 실습 8.

# word = "a,b,c,d"
# print(word.count(","))

# 실습 9.

# csv = "sensor_log.csv"
# print(csv.startswith("sensor"))
# print(csv.endswith(".csv"))

# 실습 10.

# word = "ready"
# word1 = word.upper()
# print(word1)

# 실습 11.

# word2 = "WARNING"
# word3 = word2.lower()
# print(word3)

# 실습 12.

# name = "kim chul soo"
# print(name.title())

# 실습 13.

# a = "Fault"
# b = "FAULT"

# print(a == b)

# print(a.lower() == b.lower())

# 실습 14.

# print("ABC".isupper())
# print("abc".islower())
# print("Abc".islower())

# 실습 15.

# csv = "Sensor_LOG.CSV"

# csv_lower = csv.lower()

# print(csv_lower.startswith("sensor"))
# print(csv_lower.endswith(".csv"))
# print(csv.endswith(".csv"))

# 연습문제_1

# word = "python"

# word1 = "py" + word[2:3].upper() + "hon"

# print(word1)

# word = "python"
# print(word.eplace("t", "T"))

# print("T".join(word.split("t")))

# print(word[2].upper().join(word.split("t")))

# 실습 16.
# status = " 가동중 "
# print("[" + status.strip() + "]")

# 실습 17.

# status_1 = " 대기 "
# print("[" + status_1.lstrip() + "]" + "/" "[" + status_1.rstrip() + "]")

# 실습 18.

# status = "WARNING"
# print(status.strip().lower())

# 연습문제 체이닝_2

# str = "   Warning    "

# print("[" + str.lower() + "]")
# print("[" + str.strip().lower() + "]")

# 실습 19.

# word = "PUMP A 03"

# print(word.split())

# 실습 20.

# word = "a,b,c,d"

# print(word.split(","))


# 실습 21.
# data = ["2025", "01", "15"]
# print("-".join(data))

# 실습 22

# date = "2025/01/15"

# parts = date.split("/")
# joined = "-".join(parts)
# print(joined)

# joined = "-".join(date.split("/"))  # 순서는 괄호 안에 들어가있을수록 먼저 진행한다.
# print(joined)

# 실습 23

# word = "1, NORMAL ,25.3"

# parts = word.split(",")

# status = parts[1].strip().lower()

# print(status)


# 실습 24

# name = " PUMP_A"
# temp = 87

# print(f"설비{name},온도{temp}도")


# 실습 25

# a = 86.0
# b = 87.0
# c = 88.0

# avg = (a + b + c) / 3

# print(f"평균 {avg}")

# 실습 26.

# num = 87.456
# print(f"{num:.1f}/{num:.2f}")

# 실습 27.

word = " 5 , sensor_2 , WARNING , 0.78912 "
edit = word.strip().split(",")
sid = edit[1].strip()
status = edit[2].strip().lower()
num = float(edit[3].strip())
# 이 수식이 없다면 문자열 형태로 주어지기 때문에 숫자로 계산이 안된다.
# 그렇기에 float을 통해 문자열 값들을 숫자로 바꿔줘야 한다.

print(f"[센서{sid}]상태{status}측정값{num:.2}")
# 문자열에서 :.2 이거를 쓰는 경우 에러는 안나지만 의미가 달라진다. -> 2자리까지 나타내라는 의미가 된다.
