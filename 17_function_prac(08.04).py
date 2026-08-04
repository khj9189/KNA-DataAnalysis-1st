# 실습 1.


def start_checking():
    print("점검을 시작합니다.")


start_checking()
start_checking()


# 실습 2.
def start_check():
    print("점검을 시작합니다.")
    print("안정 장비를 확인하세요")
    print("기록을 준비하세요")


start_check()
start_check()


# 실습 3.
# ①함수를정의만하면실행되지않음을확인
# ②호출줄에서함수안으로들어갔다나오는흐름따라가기
# ③여러번호출할때출력이몇번나올지먼저예측
# ④실행해예측과맞는지확인


def say_hi():
    print("안녕하세요")


say_hi()
say_hi()


# 실습 4.
# ①구분선을출력하는함수를정의
# ②점검안내여러줄을출력하는함수를정의
# ③두함수를설비마다순서대로호출
# ④실행해각설비마다같은안내가반복되는지확인


def print_line():
    # print("--------------------")
    print("-" * 20)  # 이렇게 하면 더 정확하게 나온다.


def print_check():
    print("점검 안내 출력")


# 장비1에 대한 함수 호출
# print_line()
# print_check()

# 장비2에 대한 함수 호출
# print_line()
# print_check()


# 함수에 함수를 넣는 방식 진행
def print_function():
    print_line()
    print_check()


print_function()


# 지금까지 배운 내용을 활용해서 함수 만들기 예제
print("=== 예제 ===")

import random

groups = ["에스파", "하트2하트", "리센느", "태연", "엔믹스"]

# 랜덤뽑기
my_group = random.choice(groups)
print(my_group)


def get_random_group():
    groups = [
        {"이름": "에스파", "리더": "카리나"},
        {"이름": "엔믹스", "리더": "해원"},
        {"이름": "리센느", "리더": "원이"},
    ]
    my_group = random.choice(groups)

    return my_group.get("이름"), my_group.get("리더")


group_name, group_leader = get_random_group()
print(f"{group_name}의 리더는 {group_leader}입니다.")


# 가봤거나 가보고 싶은 여행지 정보를 모아보기 - 5개 이상
# 함수를 호출하면 랜덤으로 뽑기 - 해당 여행지의 국가이름과 수도
# 환영합니다. ooo 나라의 수도 000 입니다! 출력

import random


def get_random_counrty():
    groups = [
        {"나라": "스위스", "수도": "베르디"},
        {"나라": "스페인", "수도": "마드리드"},
        {"나라": "헝가리", "수도": "부다페스트"},
        {"나라": "프랑스", "수도": "파리"},
        {"나라": "영국", "수도": "런던"},
    ]

    my_country = random.choice(groups)

    return my_country.get("나라"), my_country.get("수도")


group_name, group_capital = get_random_counrty()
print(f"{group_name}의 수도는 {group_capital}")
