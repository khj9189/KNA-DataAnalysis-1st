# ① random 모듈을 import
# ② randint로 무작위 센서값을 만들어 출력
# ③ math 모듈로 그 값을 가공(제곱근)
# ④ 다시 실행하면 값이 달라지는지 확인
# 예상 결과
# (매번 다른) 무작위 값과 그 제곱근

import random
import math

sensor_data = random.randint(10, 100)
print(sensor_data)
result = round(math.sqrt(sensor_data), 2)
print(result)
