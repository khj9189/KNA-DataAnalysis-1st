# 실습 3.
print("=== 실습 3 ===")

sensors = {
    "진동모터": 78,
    "회전모터": 80,
    "감속모터": 75,
}

total = 0

items = list(sensors.items())
max_name, max_value = items[0]
for name, value in sensors.items():
    total += value
    if value > max_value:
        max_name = name
        max_value = value

agv = total / len(sensors)

print(f"평균: {agv:.1f}")
print(f"최댓값 센서: {max_name} {max_value}")
