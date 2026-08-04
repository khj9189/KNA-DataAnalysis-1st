# 필수 : 실습문제 2~5 중 2개 이상 제출
# 선택 : 실습문제 6~8 중 1개 이상 제출

# 실습 1.
print("=== 실습 1 ===")

# 1. 센서명을 키, 측정값을 값으로 딕셔너리 저장
sensors = {"모터온도": 78, "진동값": 0.5}

# 2. 키로 값을 꺼내고 새 키로 추가·기존 키로 수정
print(sensors.get("진동값", 0))  # 값 더 안전하게 꺼내기
print(sensors["진동값"])  # 값 꺼내기

sensors["압력"] = 95  # 없던 키를 언급하면 추가
sensors["진동값"] = 0.3  # 있던 키를 언급하면 수정

print(sensors)

# 3. get으로 없는 키를 기본값으로 조회, in으로 키 존재 확인
print(sensors.get("면적", -1))  # 면적 key는 존재하지 않아서 -1로 대체

print("진동값" in sensors)  # 존재하는 key
print("면적" in sensors)  # 존재하지 않는 key

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


# 실습 6.
print("=== 실습 6 ===")

sensors = {
    "진동모터": {"측정값": 78, "상태": "경고"},
    "회전모터": {"측정값": 80, "상태": "정상"},
}

print(sensors["진동모터"]["측정값"])

for name, value in sensors.items():
    if value["상태"] == "경고":
        print(f"{name} 점검 필요 ")
