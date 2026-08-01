# =====================================================================
# 종합 실습 3. 교대조 센서 경고 로그 분석
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================
print("```")
print("=== 교대조 센서 경고 로그 분석 ===")
morning = ["TZ_11", "TZ_13", "TZ_11", "TZ_15", "TZ_13", "TZ_11", "TZ_11", "TZ_17"]
afternoon = ["TZ_13", "TZ_15", "TZ_13", "TZ_19", "TZ_15", "TZ_21", "TZ_13", "TZ_15"]
morning_and_afternoon = []
count_list = []
# TODO 1. 오전조 / 오후조 각각 고유 센서 종류 수 + 정렬된 목록 출력
#         (set 으로 중복 제거 > sorted 로 정렬)
morning_edit = set(morning)
print("오전조 고유 센서 4종:", sorted(morning_edit))
afternoon_edit = set(afternoon)
print("오후조 고유 센서 4종: ", sorted(afternoon_edit))
print("----------------------------------------")
# TODO 2. 교집합 (두 조 모두에서 경고 난 센서) 정렬해서 출력  ( & )
print("양 교대조 공통 경고 센서:", sorted(morning_edit & afternoon_edit))

# TODO 3. 차집합 (오전 전용 / 오후 전용) 각각 정렬해서 출력  ( - )
#         방향에 따라 결과 다른 것 유의
print("오전조 전용: ", sorted(morning_edit - afternoon_edit))
print("오후조 전용: ", sorted(afternoon_edit - morning_edit))

# TODO 4. 합집합 (전체 경고 센서) 종류 수 + 정렬된 목록 출력  ( | )


print("전체 경고 센서 6종:", sorted(morning_edit | afternoon_edit))

print("----------------------------------------")

# TODO 5. 센서마다 (오전 횟수 + 오후 횟수) 구해서
#         (횟수, 센서명) 튜플 리스트 만들고 횟수 많은 순 정렬
#         "N위: 센서명 - X회" 형태로 출력
#         힌트) morning.count("TZ_13") / sorted(리스트, reverse=True)
print("경고 발생 횟수 순위:")
for i in range(len(morning)):
    morning_and_afternoon.append(morning[i])

for i in range(len(afternoon)):
    morning_and_afternoon.append(afternoon[i])

sensor_list = []
count_list = []

for sensor in morning_edit | afternoon_edit:
    sensor_list.append(sensor)
    count_list.append(morning_and_afternoon.count(sensor))

tuple_list = []
for i in range(len(sensor_list)):
    tuple_list.append((count_list[i], sensor_list[i]))

tuple_list = sorted(tuple_list, reverse=True)


for i in range(len(tuple_list)):
    cnt, sensor = tuple_list[i]

    print(f"{i+1}위: {sensor} - {cnt}회")


# TODO 6. 가장 경고 많았던 센서 콕 집어서 "우선 점검 필요" 출력
print(f"최다 경고 센서: {tuple_list[0][1]} ({tuple_list[0][0]}회) → 우선 점검 필요")
print("```")
# 도전) 총 3회 이상인 센서만 "집중 관리 대상" 리스트로 만들어 정렬 출력

important_sensor = []

for i in range(len(tuple_list)):
    if tuple_list[i][0] >= 3:
        important_sensor.append(tuple_list[i][1])
print("집중 관리 대상:", sorted(important_sensor))
