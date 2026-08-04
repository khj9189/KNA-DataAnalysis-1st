# 실습 4.
sensor = ["진동모터", "조도센서", "온습도센서"]
value = [72, 0.5, 25]

sensors = {}

sensors = dict(zip(sensor, value))
for sensor, value in sensors.items():
    print(f"{sensor} : {value}")
