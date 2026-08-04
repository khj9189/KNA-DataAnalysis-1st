# error의 종류
# 1. 실행중에 오류: learn time error -> 작동 중단됨
# 2. 논리적 오류 - 작동은 되는데 결과적으로 문제가 있어 고쳐야함
# 3. 우리는 함수 이름에 걸맞는 동작만 잘 되도록 만들어야 합니다.


# 간단한 인사메시지 보여주기 함수 만들기
# 콜론으로 끝나는 줄의 뜻은 "이 다음 줄부터 들여쓴 내용은 한 묶음"
def say_hello():  # 이 부분이 수정되며 함수가 바뀌게 된다.
    print("안녕하세요")


say_hello()  # 출력할 때는 정한 함수 이름 뒤에 ()까지 붙이면 작동하게 된다.


# 함수 안에서 벌어지는 일들을 만들어봅시다.


def show_number():
    my_number = 44
    print(f"my_number : {my_number}")  # 스코프에 해당한다.


show_number()  # 44

# 여기서도 my_number 값을 정해봅시다.
# 아랫줄의 my_number는 show_numver 함수 안의 my_number와 다른 존재
my_number = 24  # 함수 안에 들어가지 않았기에 24로 숫자가 바뀌지는 않는다.

show_number()  # 44

# 그래서 함수 안의 my_number 데이터가 영향을 끼치는 범위를 전문용어로 스코프라고 부른다.

# 함수는 호출되기 전에 만들어져야합니다.

# show_title()-> 함수가 만들어지기 전에 선언하면 name 에러가 발생한다.


def show_title():
    print("함수 배우기")


show_title()


# 2번 실행하면 2번 실행된다.
def print_line():
    print("=" * 20)


print_line()
print_line()

# 매번 함수가 호출되면 그 안의 코드는 매번 새롭게 시작된다.


def show_counter():
    count = 0
    count += 1
    print(count)
    # 이 함수가 종료되면 count를 포함한 이 함수 안의 데이터는 모두 사라짐


show_counter()


# 각 함수 이름은 이름의 걸맞는 역할만 해줘야 한다.


def show_student():
    print("학생1: 짱구")
    print("학생2: 철수")
    print("학생3: 훈이")
    # print("선생님: 채송화") # 출력은 되지만 좋은 함수는 아니다.


def show_teacher():
    print("선생님: 채송화")


show_student()
show_teacher()


# 그렇다면 매번 함수를 만들어야 하는가? -> 함수 안에 함수를 만들어서 해결한다.
def show_classroom():
    show_student()
    show_teacher()


show_classroom()

# 해당 부분의 코드가 문제 없지만 다른 부분과 예상치 못한 영향을 주고 받는다면? => 사이트 이펙트

# 코드 중복과 함수화
print("=== 코드 중복과 함수화 ===")

print("압축기A 온도 확인 중")
print("결과를 확인합니다.")
print("펌프1 온도 확인 중")
print("결과를 확인합니다.")

# 이와 같은 식의 코드를 여기저기 복붙하면 언젠가 사람의 실수로 사고가 생길 수 있다.


# 실습 2.
def start_check():
    print("점검을 시작합니다.")
    print("안정 장비를 확인하세요")
    print("기록을 준비하세요")


start_check()
start_check()

print("=== 함수 호출 결과 예측하기 ===")


def say_hi():
    print("안녕하세요")


say_hi()
say_hi()
