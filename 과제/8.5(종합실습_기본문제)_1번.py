# ① import 모듈명으로 통째로 가져와 모듈명.기능() 으로 사용
# ② from 모듈 import 기능 으로 일부만 가져와 모듈명 없이 사용
# ③ import 모듈 as 별명 으로 별명.기능() 으로 사용
# ④ 세 방식의 출력이 같은지 확인
# 예상 결과
# 세 방식 모두 4.0 5 출력

# 1.
import math

result = math.sqrt(16)
print(result)

# 2.
from math import sqrt

result = math.sqrt(16)
print(result)

# 3.
import math as mt

result = mt.sqrt(16)
print(result)
