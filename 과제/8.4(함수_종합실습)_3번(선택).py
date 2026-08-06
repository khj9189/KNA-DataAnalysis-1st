# ① 값을 받아 계산해 return하는 함수를 정의
# ② 계산 결과를 받아 판정해 출력하는 함수를 정의
# ③ 첫 함수의 반환값을 변수에 담아 둘째 함수에 전달
# ④ 실행해 입력-처리-출력 흐름이 이어지는지 확인
# 예상 결과 평균 85.0 → 정상


def calculate(values):
    return sum(values) / len(values)


def judge(avg):
    if avg > 80:
        print("정상입니다.")
    else:
        print("비정상입니다.")


sensor_data = [80, 85, 90]
agv = calculate(sensor_data)
judge(agv)
