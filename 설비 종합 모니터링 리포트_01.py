# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"


# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)

print("========================================")
print("        설비 종합 모니터링 리포트")
print("========================================")
count_danger = 0
count_care = 0
count_normal = 0

danger_list = []

for i, (설비명, 온도, 진동) in enumerate(sensors, start=1):
    if 온도 > 90 or 진동 > 5.0:
        상태, 이모지 = "위험", "🚨"
        count_danger += 1
        danger_list.append(설비명)
    elif 온도 >= 80 or 진동 >= 3.0:
        상태, 이모지 = "주의", "⚠️"
        count_care += 1
    else:
        상태, 이모지 = "정상", "✅"
        count_normal += 1
    print(f"{i}. {설비명} | 온도 {온도}℃ | 진동 {진동}mm/s | {상태} {이모지}")

danger_list.sort()
print("----------------------------------------")
print(f"총 설비: {len(sensors)}대")

# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)

print(f"정상: {count_normal} / 주의: {count_care} / 위험: {count_danger}")

# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)

unnormal = round(
    (count_danger + count_care) / (count_care + count_danger + count_normal) * 100, 1
)
print(f"이상 설비 비율: {unnormal}%")

# TODO 4. 전체 평균 온도 출력 (round)

total_temp = 0

for i in range(len(sensors)):
    total_temp += sensors[i][1]
print(f"평균 온도: {round(total_temp / len(sensors), 1)}℃")


# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)

max_temp = sensors[0][1]
max_i = 0

for i in range(len(sensors)):
    if sensors[i][1] > max_temp:
        max_temp = sensors[i][1]
        max_i = i

print(f"최고 온도 설비: {sensors[max_i][0]} ({max_temp}℃)")

# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())

print(f"위험 설비 목록: {danger_list}")
print("========================================")

# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"
