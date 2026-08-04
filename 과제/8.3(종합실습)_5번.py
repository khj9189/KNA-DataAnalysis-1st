# ①측정값 딕셔너리와 임계값 딕셔너리를 각각 저장
# ②items로 순회하며 각 센서 값이 같은 이름의 임계값을 넘는지 비교
# ③넘는 센서 이름을 빈 리스트에 모아 출력

sensor_list = []

sensors = {
    "진동모터": {"측정값": 78, "상태": "경고"},
    "회전모터": {"측정값": 80, "상태": "정상"},
}

end_line = {
    "진동모터": {"임계값": 70, "상태": "정상"},
    "회전모터": {"임계값": 90, "상태": "정상"},
}

for tool, status in sensors.items():
    for name, value in end_line.items():
        if tool == name:
            if status["측정값"] > value["임계값"]:
                sensor_list.append(tool)
print(sensor_list)
