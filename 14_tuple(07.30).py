# tuple: 값을 묶어주는 역할
# () 소괄호 안에 쉼표로 나누어서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에는 , 를 붙여야 튜플로 인식을 한다.
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형이다.


# 튜플의 기준:

sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = (
    "모터온도",
    78,
)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'int'>

sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = ()
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>


# 괄호는 튜플인지 아닌지를 결정하지 않는다 (그냥 묶어주는 역할/가독성용).
# 진짜 기준은 쉼표(,)의 존재 여부다.
# - 값이 2개 이상이면: 값 사이에 쉼표만 있으면 튜플 (끝에 있어도 없어도 무방)
# - 값이 1개면: 반드시 쉼표가 있어야 튜플로 인식 (없으면 그냥 원래 자료형)

# 요소 갯수
# 요소 2개 이상: 쉼표가 있다면 튜플이다
# 요소가 1개이면 쉼표로 판단한다.
# 요소 0개 (빈 튜플): () 빈 괄호

# 튜플에서 많이 헷갈려하는 부분
# (1): int
# (1,): tuple

# (1,2,3,) -> 가장 마지막에 쉼표를 붙여서 튜플임을 명시

sensor = ("모터온도", 78)
print(sensor[0])

# 튜플의 슬라이싱
s = (
    "a",
    "b",
    "c",
    "d",
    "e",
)
print(s[1:4])
# 슬라이싱한 결과는 소괄호에 감싸져 있음
# 튜플은 슬라이싱해도 튜플을 유지한다.
print(type(s[1:4]))

# 튜플 언패킹
# 튜플에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한 번에 선언하기
a, b, c = "a", "b", "c"
print(a)  # 문자열 a
print(b)  # 문자열 b
print(c)  # 문자열 c

unpacking = (
    1,  # 변수 one
    2,  # 변수 two
    3,
)  # 변수 three

# unpacking = one, two, three
# one, two, three라는 알 수 없는 변수를 unpacking 변수에 할당하겠다는 의미
# 동작 x

one, two, three = unpacking
print("one:", one)
print("two:", two)
print("three:", three)
# unpacking이라는 변수에 담긴 튜플 내부의 값들을 할당 연산자 왼쪽 one, two, three 변수에 풀어서 담는다는 뜻

# 없는거를 넣으면 value error가 발생한다.
# 튜플의 unpacking은 변수의 개수와 튜플에 담긴 값의 개수가 동일해야 함


# 리스트 언패킹이 가능할까?
one, two, three, four = [11, 22, 33, 44]
print("one:", one)
print("two:", two)
print("three:", three)
print("four:", four)
