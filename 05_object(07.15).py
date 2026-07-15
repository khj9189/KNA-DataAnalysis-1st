# int - 정수형

count = 3
age = 20
tall = 173

# 소수점 없이 딱 떨어지는 수

# 0과 음수도 정수에 포함됨

temp = -30
zero = 0

# ====================================

# float(실수): 소수점이 붙은 숫자
# 5.0처럼 딱 떨어지는 수이지만 소수점이 있다면 무조건 float이다.

tired = 99.99999
height = 17.2

# ====================================

# str(문자열): 따옴표에 감싸져 있는 모든 값

hello = "안녕하세요"
emoji = "😀"
empty = ""  # 따옴표만 있고 아무것도 작성되지 않아도 str (빈 문자열열)
fake_num = "12345"
fake_num2 = "5.0"
# 따옴표가  ""와 ''둘다 사용할 수 있는 이유는 문자열 안에 따옴표가 필요한 경우가 있기 때문, 이럴 경우 사용하지 않는 따옴표로 쌍을 맞춰 가장 바깥에 감싸줘야 함
illit = "It's me"

# ====================================

# bool(불리언): True, False 두 가지 값만 가질 수 있는 자료형
# 첫 글자는 대문자, 따옴표 없이 작성

ok = True
no = False

# 비교할 경우 bool로 출력력
print(100 < 5)
print(5 == 5)


# ====================================
print("=== type() ===")
# type() -  자료형 확인
# type(확인하고자 하는 것) > 입력한 것의 자료형을 알려줌

print(type(5))  # 그냥 type(5)라고 작성하면 print가 없어서 결과가 안나온다.
print(type("센서A"))  # <class str> 출력
print(type(True))  # bool
print(type(3 > 2))  # bool
# 1. print 함수의 내부를 확인
# 2. print 함수에 또 함수가 있는 것을 확인하고 type 함수의 내부를 확인
# 3. type 함수의 내부에 연산자가 있는 것을 확인하고 연산 진행
# 4. 3>2의 연산 결과는 True이기 때문에 type(True)로 바뀜
# 5. type(true)의 결과인 class, bool이 print로 인해 터미널에서 출력

print(3, type(3))  # 3, <class, int> 로 출력됨

num = 123
fake_num = "123"
str = "문자열"
ok = True

print(num, type(num))

# 가독성을 개선한 경우
print(num, ">>>", type(num))
print("num:", type(num))
