def say_hello():
    print("안녕하세요")


say_hello()

# 인삿말 출력 함수 친근 버전


def say_hello_ned():
    print("안녕하세요, Ned")


def say_hello_tuna():
    print("안녕하세요, Tuna")


say_hello_ned()
say_hello_tuna()

# 인사할 대상이 많아진다고 위 함수들을 더 만드는건 좀 아니다.
# 해결책은 하나의 함수에서 저 다양성을 대응해주는 것
# 그것이 바로 함수의 매개변수 활용


def say_hi(name):
    print(f"반갑습니다. {name}")


say_hi("NED")
say_hi("Tuna")


# 예제코드: 특정 장비 이름을 알려주면 해당 장비의 체크를 시작 알림
def check(name):
    print(f"{name} 장비의 점검을 시작합니다.")


check("압축기 A")
check("펌프 B")

# 매개변수가 2개 이상인 예제 - 덧셈
print("=== 매개변수가 2개 이상인 예제 - 덧셈 ===")


def calc_sum():
    number_1 = 1
    number_2 = 2
    total = number_1 + number_2
    print(f"{number_1} + {number_2} = {total}")


calc_sum()


def calc_sum(number_1, number_2):
    total = number_1 + number_2
    print(f"{number_1} + {number_2} = {total}")


calc_sum(1, 2)


# 매개변수 2개 이상인 예제 - 장비 이름과 온도 정보 출력
def report(name, temp):
    # name = "압축기A"
    # temp = "75.3"
    print(f"{name}의 온도는 {temp}도 입니다.")


report("압축기A", 75.3)
report("펌프B", 85.2)

# 엉뚱하게 호출한 경우
report(75.3, "보일러C")

# 첫 번째 매개변수는 무조건 name이 되고,
# 두 번째 매개변수는 무조건 temp가 되니까 원하지 않는 결과가 나올 수 있다.

# 매개변수가 부족하거나 더 있는 경우
# report("압축기A", 75.3, "가동중") # TypeError: report() takes 2 positional arguments but 3 were given -> 값이 더 들어간 경우
# report("펌프B") # TypeError: report() missing 1 required positional argument: 'temp' -> 값이 덜 들어간 경우우

# 키워드 인자
print("=== 키워드 인자 ===")


def report_keywords(name, temp):
    print(f"{name}의 온도는 {temp}도 입니다.")


# 키워드 인자 없이 호출
report_keywords("압축기A", 75.3)
print("# 이 경우는 문제가 발생한다")
report_keywords(37.4, "펌프A")  # 이 경우는 문제가 발생한다

# 키워드 인자 사용해 호출 => 순서 바꿔 호출해 생기는 문제 근본 차단
report_keywords(name="압축기A", temp=75.3)
report_keywords(temp=37.4, name="펌프A")

# 반환값
print("=== 반환값 ===")


def add(a, b):
    total = a + b
    return total  # return을 만나는 순간 함수가 끝나게 된다. total만 남게 된다.
    print("1 + 1 =2")


# def add(a, b):
#     return a+b  # return을 만나는 순간 함수가 끝나게 된다. total만 남게 된다.


result = add(1, 2)
print(f"1 + 2 = {result}")

result = add(1, 2)
# 여러번 같은 결과 호출해야한다면 차라리 변수에 담아서 쓰기
print(result + 1)
print(result + 2)
print(result + 3)


# 평균 내는 함수 만들기
def calc_average(a, b):
    return (a + b) / 2


agv = calc_average(75.3, 88.0)
print(f"평균온도: {agv}")

print("wwrwrwrw")


# 여러 값을 한 번에 반환하기
# 다음의 함수는 배열을 받아서 최소값과 최대값을 동시에 return한다.
def calc_min_max(values):
    minimum = min(values)  # 배열 안의 최소값을 찾아 minimum에 담기
    maximum = max(values)  # 배열 안의 최대값을 찾아 maximum에 담기
    return minimum, maximum


target_list = [1, 2, 3, 4, 5, 6]
result = calc_min_max(target_list)

print(result)  # 튜플인 것을 확인


# 반환값을 언패킹으로 받기
# 함수의 결과를 받는 순간에
# 결과 튜플의 내용을 풀어서 개별 변수에 담아 사용하기
result_min, result_max = calc_min_max(target_list)

print("최소값" + str(result_min))
print("최대값" + str(result_max))

# return 값이 없는 함수를 호출해놓고
# 결과를 어디에 담겼다고 하면 담기는 값은 none이 된다.


def say_greet():
    print("만나서 반갑습니다.")
    return


greet = say_greet()
print(greet)  # none
