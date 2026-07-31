# =====================================================================
# 종합 실습 2. 실시간 측정값 입력 시스템
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

# 이 실습은 사용자한테 입력받는 거라 미리 주는 데이터 없음
# while로 계속 입력받다가 q 입력하면 종료 > 통계 출력

LIMIT = 100  # 임계값 (100 초과 시 즉시 경고)

# TODO 1. while로 "측정값: " 계속 입력받기, q면 break
#         (입력값은 숫자 아니면 q 라고 가정)
#         값은 리스트에 .append() 로 모으기

num = 0
count = 0
total_count = 0
count_list = []
max_num = 0
min_num = 0
list_sum = 0
list_avg = 0
order = 0
print("측정값을 입력하세요. 종료하려면 q 입력.")

while True:
    a = input("측정값: ")
    total_count += 1

    if a != "q" and a == "":
        if a != "":
            num = float(a)
            count_list.append(num)
            if num > LIMIT:
                count += 1
                print(f"🚨 임계값(100) 초과! 현재까지 초과 {count}회")
    else:
        if a == "q":
            if total_count == 1:
                print("입력된 측정값이 없습니다.")
                break
            elif total_count >= 2:
                print("총 입력 개수:", len(count_list))
                max_num = count_list[0]
                for i in range(len(count_list)):
                    if max_num < count_list[i]:
                        max_num = count_list[i]
                    else:
                        max_num = max_num
                min_num = count_list[0]
                for i in range(len(count_list)):
                    if min_num > count_list[i]:
                        min_num = count_list[i]
                    else:
                        min_num = min_num
                print("최댓값:", max_num, "/" "최솟값:", min_num)
                for num in count_list:
                    list_sum += num
                    list_avg = list_sum / len(count_list)
                print("평균값:", round(list_avg, 2))
                if count <= len(count_list):
                    print("임계값 초과 개수:", count)
                for i in range(len(count_list)):
                    if list_avg < count_list[i]:
                        order += 1
                print("평균 초과 개수:", order)
                count_list.sort(reverse=True)
                print("상위 3개 값:", count_list[:3])
        break

print("----------------------------------------")


# TODO 2. 입력값이 LIMIT 초과하면 즉시 경고 + 지금까지 초과 횟수 출력


# TODO 3. q로 끝난 뒤:
#   - 입력값이 하나도 없으면 "입력된 측정값이 없습니다." 출력하고 끝
#   - 값이 있으면 아래 출력
#       · 총 입력 개수 (len)
#       · 최댓값 / 최솟값 (반복문으로 직접 찾기)
#       · 평균값 (round, 소수 둘째 자리)
#       · 임계값 초과 개수
#       · 평균보다 큰 값의 개수  > 평균 먼저 구한 뒤 리스트 다시 돌기
#       · 상위 3개 값 (.sort(reverse=True) 후 슬라이싱 [:3])


# 도전) q 대신 그냥 Enter(빈 입력 "") 치면 무시하고 다시 받기
