# ① 센서값 목록을 받아 평균을 return하는 함수를 정의
# ② 평균과 기준값(기본값 있음)을 받아 상태를 판정해 return하는 함수를 정의
# ③ 두 함수를 순서대로 연결해 목록에서 상태까지 구하기
# ④ 실행해 흐름과 결과를 확인

# 예상 결과 85.0 정상


def get_average(values):
    return round(sum(values) / len(values), 2)


def judge_status(avg, standard=80):
    if avg >= standard:
        return "정상"
    else:
        return "비정상"


sensor_data_list = [80, 85, 90]
avg = get_average(sensor_data_list)
status = judge_status(avg)
print(avg, status)
