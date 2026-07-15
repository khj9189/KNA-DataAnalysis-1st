# 변수는 값에 붙이는 이름- 이름표는 그대로, 안의 값만 바뀜

# print(temp) -> NameError: name 'temp' is not defined

temp = 25
print(temp)  # 위로 올라가서 가장 가까운 값을 가져온다.

temp = 30
print(temp)

print("temp")

# 영문자, 숫자, 밑줄만 사용, 띄어쓰기 불가, 중간 공백 불가, 숫자로 시작 불가
# if, for, true같은 예약어는 사용 불가, 함수 이름을 덮어 쓰면 불편하다, 자동으로 색이 입혀진 단어는 이름으로 사용하지 말 것


# 변수 선언 방법
# 변수이름 = 값
# 오른쪽 값을 왼쪽 이름에 "저장"하라는 코드

temp = 36  # 숫자로 저장하고 싶다면 따옴표 금지지
name = "센서 A"  # 글자는 무조건 따옴표로 감싸기

print(temp)
print("temp")

#  =은 "같다"가 아니라 "저장"하는 것
#  비교는 ==을 사용

# ================================

print("=== 변수 사용 활용 ===")

x = 5
# 변수를 "재할당"할 때 변수 기존 자신의 값을 활용할 수 있음
# 변수에 할당할 때 오른쪽을 먼저 계산한 뒤 x에 값을 재할당
x = x + 5
print(x)

# y = y+5 # 오류 발생. y가 선언되지 않았기에

# ==================================

print("=== 재할당 ===")

print("재할당하기 전 temp:", temp)
temp = 15  # 위에서 할당했던 36이라는 값을 15로 재할당(수정정)
Temp = 150  # temp와 다른 변수로 동작
print("temp:", temp, "Temp:", Temp)

# 재할당은 지금까지 실행된 코드 중 가장 마지막으로 저장된 값이 불려옴
# print(score) NameError 발생
score = 10
print(score)
score = 20
score = 30
print(score)

# ==================================

print("=== 값 복사 ===")

a = 10
b = a  # b변수에는 10이 저장(저장할 때의 그 군간의 a값을 b에 복사)
a = 100  # a의 변수를 재할당해도
print(b)  # 10 b 변수의 값은 10이 그대로 유지됨

# ==================================

print("=== 여러 변수 한 번에 선언 및 할당 ===")

# 형식: 변수1, 변수2,....  = 값1, 값2, ..... <변수와 값이 갯수가 같아야 함>

width, height = 10, 20  # width 에는 10 height에는 20이 할당됨

print("width:", width, "height:", height)

# 변수 3개 값 2개인 경우 -> value error가 발생한다.
# x,y,z = 10, 20

# ==================================

print("=== 주석으로 변수 설명 ===")

temp = 25  # temp 25는 온도(섭씨)
count = 3  # 센서 개수
# temp  = 10000000
print(temp)  # 25 -> 주석처리된 값은 사용되지 않음

# 값을 추적하며 확인하는 습관 -> print로 코드를 작동시키기 전에 예상된 값이 알맞게 나오는지 확인하며 진행할 것

# 실습

print("=== 실습 ===")
temp = 25
print(temp)

name = "센서A"
print(name)

print("=== 실습2 ===")
temp = 30
print(temp)

temperature = 30
print(temperature)

print("=== 실습3 ===")
my_number = 29
print(my_number)
mood = "HAPPY"
print(mood)

print("=== 실습4 ===")
age = 26
label = "나이"
print(label)
print(age)


print("=== 실습5 ===")
x = 10
print(x)

x = x + 5
print(x)

x = x * 2
print(x)

print("=== 실습6 ===")
a = 100
b = a
a = 999
print(a)
print(b)

print("=== 실습7 ===")
# print(temp)
temp = 25
print(temp)
score = 90
# print(Score)
print(score)

print("=== 실습8 ===")
temp = 25  # 온도(섭씨)
count = 3  # 센서 개수
# temp = 100
print(temp)

print("=== 실습9 ===")
x = 5
x = 10
x = x + 1
print(x)  # 11

print("=== 실습10 ===")
name = "센서A"
temp = 25
print("설비")
print(name)
print(temp)

print("=== 실습11 ===")

a = 25
b = 3
device_temp = 25
sensor_count = 3
print(device_temp)
print(sensor_count)


print("=== 실습12 ===")
x, y, z = 1, 2, 3
width, height = 4, 3
print(width)
print(height)
