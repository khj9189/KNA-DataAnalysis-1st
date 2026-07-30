# 실습 1.

temps = [32, 35, 31, 33, 29, 27, 20, 19]

new_temps = []

for i in temps:
    if i > 30:
        new_temps.append(i)
print(new_temps, len(new_temps))
print(" ")

print("새로운 리스트:", new_temps, "\n" "원본 리스트:", temps)
