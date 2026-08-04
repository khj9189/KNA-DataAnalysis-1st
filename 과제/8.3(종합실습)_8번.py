# ①센서 측정값 딕셔너리와 임계값 딕셔너리 저장
# ②values로 전체 평균 구하기
# ③items 순회로 임계값 초과 센서를 셋에 모으기
# ④셋을 정렬해 출력

sensor = {"진동": 10, "강도": 8}
limit = {"진동": 9, "강도": 10}


average = sum(sensor.values()) / len(sensor)
print(average)


over_limit = set()
for name, value in sensor.items():
    if value > limit[name]:
        over_limit.add(name)


print(sorted(over_limit))
