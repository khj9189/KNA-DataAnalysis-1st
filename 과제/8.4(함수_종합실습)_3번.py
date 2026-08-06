# ① 매개변수 두 개를 가진 함수를 정의
# ② 호출할 때 매개변수 이름을 지정해 값을 전달
# ③ 키워드로 전달하면 순서를 바꿔도 같은 결과인지 확인
# ④ 위치 인자와 키워드 인자를 섞을 때는 위치가 먼저임을 확인


def sensor_data(motor, temperature):
    print(f"{motor} {temperature}")


# 위치인자는 그냥 순서대로 값을 넣어주는 방식을 의미
# 키워드인자는 매개변수이름=값 이런 형태를 의미
sensor_data(motor="모터", temperature=78)
sensor_data(temperature=92, motor="펌프")
sensor_data("모터", temperature=78)
