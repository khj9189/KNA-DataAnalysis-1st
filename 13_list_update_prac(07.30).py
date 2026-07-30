# 실습 1.

# temps = [32, 35, 31, 33, 29, 27, 20, 19]

# new_temps = []

# for i in temps:
#     if i > 30:
#         new_temps.append(i)
# print(new_temps, len(new_temps))
# print(" ")

# print("새로운 리스트:", new_temps, "\n" "원본 리스트:", temps)


# 실습 5.
# temps = [32, 35, 31, 33, 29, 27, 20, 19]
# new_temps = []
# new_temp = 0

# for i in temps:
#     new_temps.append(round(i * 1.8 + 32, 2))
# print(new_temps)

# round로는 리스트 전체를 한 번에 소수점을 제거할 수 없다 그렇기에 미리 round를 적용해서
# 리스트에 들어갈 때 소수점을 없애고 넣어준다.
# 리스트이름.append(넣을값)

# 실습 6.

# temps = [32, 35, 31, 33, 29, 27, 20, 19]
# sum_temps = 0
# count = 0
# new_temps = []
# sum_new_temps = 0
# new_count = 0

# for i in temps:
#     sum_temps += i
#     count += 1
#     avg = sum_temps / count
# print(f"전체 평균: {avg}")

# for i in temps:
#     if i > 30:
#         new_temps.append(i)
#         sum_new_temps += i
#         new_count += 1
#         new_avg = sum_new_temps / new_count

# print("고온 개수:", len(new_temps), "\n" "고온평균:", new_avg)

temps = [32, 35, 31, 33, 29, 27, 20, 19]

sum_temps = 0
for i in temps:
    sum_temps += i
avg = sum_temps / len(temps)
print(f"전체 평균: {avg}")

new_temps = []
sum_new_temps = 0
for i in temps:
    if i > 30:
        new_temps.append(i)
        sum_new_temps += i
new_avg = sum_new_temps / len(new_temps)

print("고온 개수:", len(new_temps), "\n" "고온평균:", new_avg)
