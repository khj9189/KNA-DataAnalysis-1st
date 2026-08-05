# 수학 관련 모듈을 불러옵니다.
import math

result = math.sqrt(4)
print(result)

# ========================================================

# 수학 관련 모듈에서 sqrt 기능만 불러옵니다.
from math import sqrt

result = math.sqrt(4)

# 이젠 sqrt만 불러도 됩니다.
print(result)

# ========================================================

# math라는 모듈 이름 다 쓰기 귀찮아서 줄이기

import math as mt

result = mt.sqrt(16)
print(result)


# datetime 모듈을 가져옵니다.
# datetime의 now()는 현재의 지역 날짜와 시간을 반환한다.
import datetime as dt  # 줄여줬기에 다음부터는 줄인 글자로 사용된다.

now = dt.datetime.now()
print(now)  # 2026-08-05 11:22:04.982606

print(type(now))  # <class 'datetime.datetime'>

# ========================================================
# math 표준 라이브러리
# math에서 sqrt, ceil 두개만 사용한다면 이렇게 써도 됩니다.
import math

print(math.sqrt(9))
print(math.ceil(4.2))
print(3**2)  # math와 무관

# 위에서 가져온 math 함수들 사용 예제
from math import sqrt, ceil

print(sqrt(9))
print(ceil(4.2))

print("=" * 20)

# 표준 라이브러리의 random 모듈
import random

print(random.randint(1, 10))  # 1~10 중 무작위 정수
print(random.choice(["정상", "경고", "위험"]))  # 셋 중 무작위 (실행마다 다름)

print("=" * 20)

# 표준 라이브러리의 datetime 모듈

# datetime이라는  모듈 안의 datetime 클래스에서 지원하는 now()함수 호출
import datetime

now = datetime.datetime.now()  # 앞 datetime은 모듈, 뒤는 그 안의 도구
print(now)  # 예: 2024-03-01 09:00:00.123456

print("=" * 20)

# 모듈의 도움말 보기
# 참고만 하고 웹사이트 구글링을 이용하여 계산함

# dir(math)
# help(math.sqrt)

print("=" * 20)
