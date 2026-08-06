# ① 센서값 목록을 매개변수로 받는 함수를 정의
# ② min·max·합÷개수로 최소·최대·평균을 계산
# ③ 세 값을 쉼표로 함께 return
# ④ 돌려받은 값을 세 변수로 언패킹해 출력


def calc_min_max_avg(values):
    minimum = min(values)
    maximum = max(values)
    agv = round(sum(values) / len(sensor_data_list), 2)
    return minimum, maximum, agv


sensor_data_list = [78, 83, 92]
result = calc_min_max_avg(sensor_data_list)
print(result)
