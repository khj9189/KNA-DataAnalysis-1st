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
