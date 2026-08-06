# ① def 괄호 안에 매개변수 두 개를 쉼표로 정의
# ② 함수 안에서 두 매개변수를 함께 활용
# ③ 인자 두 개를 순서대로 전달해 호출
# ④ 인자 순서를 바꾸면 결과가 어떻게 달라지는지 확인


def sensor_data(motor, temperature):

    print(f"{motor} {temperature} 도")


sensor_data("모터", 78)
sensor_data("펌프", 92)
sensor_data(78, "펌프")
