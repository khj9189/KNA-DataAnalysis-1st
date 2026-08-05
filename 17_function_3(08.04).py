# 기본값 인자
# name과 value는 호출할 때 매개변수를 지정해줘야 하지만, unit은 언급안해주면 "도(C)"라는 기본값으로 정의된다.
def report(name, value, unit="도(C)"):
    print(f"{name} : {value}{unit}")


report("압축기", 75.3, "도(C)")
report("압축기", 75.3)
report("압축기", 75.3, "도(F)")


# 기본값 덮어쓰기
# 결과가 bool인 타입을 따지는 경우 변수 이름이 보통 is로 시작한다.
def is_over_limit(value, limit=90):
    if value > limit:  # 위험 맞음
        return True
    # 그 밖에는 위험 아님
    return False  # if문을 돌지 않는다면 그냥 바로 return False로 이동한다.


# print(f"위험한가요? {is_over_limit(95, 90)}")
# print(f"위험한가요? {is_over_limit(105, 90)}")

print(f"위험한가요? {is_over_limit(95)}")  # 90으로 고정된 경우
print(
    f"위험한가요? {is_over_limit(105)}"
)  # 어쩌다 다른 기준이 필요할 떄만 기준으로 함께 전달해주면 된다.
print(
    f"위험한가요? {is_over_limit(85, limit = 80)}"
)  # limit 값을 밑에서 지정하면 그 값에 따라 계산이 된다.

# 실습1.
print("=== 실습 1. ===")
# ①def 괄호안매개변수에=로기본값을지정
# ②인자를생략하고호출해기본값이쓰이는지확인
# ③인자를넣어호출해기본값을덮어쓰는지확인
# ④필수매개변수는앞, 기본값매개변수는뒤순서규칙확인

# 앞선 예제 코드들이 잘 돌아가는지 확인하면 된다.

# ==========================================================
# 지역변수와 범위 -> 코드의 어디서부터 어디까지가 살아있을까
print("=== 지역변수와 범위 ===")

outer = 100


def change_outer():
    # 함수내부에서 처음 언급되면서 새롭게 만들어진 내부의 outer이고 (지역변수)
    # 함수가 종료되면 메모리에서 사라진다.
    # 함수 바깥의 같은 이름의 존재에는 전혀 영향을 안준다.
    outer = 50


change_outer()
print(outer)

# ==========================================================
print("=== 실습2. ===")
# ①함수안에서새변수를만들어사용
# ②함수를호출해함수안에서는그변수가동작하는지확인
# ③함수밖에서같은변수를출력해오류가나는지확인
# ④함수안변수는함수가끝나면사라지는지역변수임을정리
# 위에 코드 보기

# ==========================================================
print("=== 함수의 기본 예제 & 복습 ===")


def say_hello():
    pass  # 아무것도 안하는 코드


def say_hi():
    print("안녕하세요")


# 함수는 선언된 후에 호출되어야 한다.
say_hi()


# 매개변수를 사용하면 더 다양한 일을 할 수 있습니다.
def show_hello():
    name = "NED"
    print(f"안녕하세요, {name}")


show_hello()


# 매개변수는 여러 값을 받을 수 있고
def show_hi(name, message):
    # message = "안녕하세요"
    print(f"{message}, {name}")


show_hi("NED", "안녕하세요")


# 매개변수에는 따로 안알려주면 기본값을 적용할 수도 있습니다.
def show_greeting(name, message="안녕하세요"):
    # message = "안녕하세요"
    print(f"{message}, {name}")


show_greeting("NED")
show_greeting("jack", message="hello")
