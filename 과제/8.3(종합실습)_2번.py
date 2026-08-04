# 실습 2.
print("=== 실습 2 ===")

sensors = {"모터온도": 78, "진동값": 0.5}

new_data = {
    "모터온도": 80,
    "유량": 42,
}

sensors.update(new_data)
print(sensors)

del sensors["유량"]
print(sensors)
