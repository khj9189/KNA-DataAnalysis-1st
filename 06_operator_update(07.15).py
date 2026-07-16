# 산술 연산자
# + - * / //(몫) %(나머지) **(거듭제곱)

print(3 + 5)  # 8
print(10 - 4)
print(4 * 5)
print(20 / 4)  # 5.0 -> 나누기는 float 주의
print(7 // 3)  # 2
print(7 % 3)  # 1
print(2**5)  # 2의 5제곱

# ====================================================

# 연산 우선 순위와 우선순위 지정
# 거듭제곱 > 곱하기/나누기/몫/나머지 동일 >  더하기/빼기

print(2 + 8 * 3)  # 곱하기 먼저 계산 후 그 결과를 2와 더한다.

print((2 + 8) * 3)

# ===================================================

# 복합연산자

result = 3 * 5
print(result)

# +=: 기존 값에서 오른쪽 값을 더한 뒤 재할당
# -=: 기존 값에서 오른쪽쪽 값을 뺸 뒤 재할당
# *=: 기존 값에서 오른쪽 값을 곱한 뒤 재할당
# /=: 기존 값에서 오른쪽 값을 나눈 뒤 재할당

result += 10  # 25
print(result)
result -= 5  # 20
print(result)
result *= 3  # 60
print(result)
result /= 2  # 30.0
print(result)


# ====================================================

# 문자열 연산
print("안녕" + "하세요")

# 안녕과 하세요 사이에 공백을 1개 넣고 싶다면
# 방법1) ,사용
print("안녕", "하세요")
# 방법2) 안녕 뒤에 공백 추가
print("안녕 " + "하세요")
# 방법3) 공백만 있는 문자열 더하기
print("안녕" + " " + "하세요")

# 문자열 곱하기
print("안녕" * 5)

# 문자열에 연산자를 사용할 경우 모두 이어져서 나온다.

# ====================================================
print("=== 비교연산자 ===")

# 미만, 초과, 이하, 이상, 같다, 다르다(!=)
# 비교 결과는 무조건 True 아니면 Fasle

print(7 < 16)  # True
print(7 > 16)
print(7 <= 16)
print(7 >= 16)
print(7 == 7)
print(7 != 7)

# 비교연산자는 문자열 비교도 가능
print("hello" == "hello")  # True
print("정상" == "정상")  # True

# 비교연산자를 사용해 문자열을 비교할 때 주의사항

# 1. 대소문자 구분
print("hello" == "Hello")  # False

# 2. 공백이 있어도 다르다고 판단
print("정상" == "정상 ")  # False

# 3. 부정연산자 !=
print("hello" != "hello")  # False (두 값이 동일한데 느낌표로 인해서 값이 반대로 출력됨)
print("hello" != "hello ")  # True
print("hello" != "Hello")  # True

# 변수로 비교연산자 사용
# "" 가 없다면 변수로 이해하고 위에서 변수에 할당 된 값을 찾는다.

num1 = 123
num2 = 456

print(num1 >= num2)  # False
# print(num1 >= "num2")
# typeError : int와 str을 비교했기 때문이다.


# 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교
# print("=== 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교 ===")
# hello = hi
# print(hello == hi)  # NameError(선언하지 않은 이름 호출했을 때)
# hi는 따옴표에 감싸져있지 않기 때문에 변수로 취급됨
# 그런데 우리는 hi 변수를 선언한 적이 없기 때문에 에러

# 질문 1) 해결방법
# print("=== 질문 1) 해결 방법 ===")
hi = "안녕"  # hello 변수에 hi 변수를 할당하기 전 hi 변수 선언
hello = hi  # print(hello) > 안녕
print("=== 변수 hello(안녕)와 변수 hi(안녕) 비교 ===")
print(hello == hi)  # True

# =================================================================================

# 논리연산자 - and, or, not
# 1. and: 둘 다 True여야 True를 반환
print(5 == 5 and 7 == 7)  # 양쪽이 모두 True기에 true를 반환
print(
    5 == 7 and 7 == 7
)  # False + True = False => 첫 번째 조건이 False이면 뒤에 조건은 확인 안 함
print(5 == 5 and 7 != 7)  # True + False = False

# 2. OR: 하나라도 True라면 True 반환 -> 앞에 있는거 먼저 본다다
print(5 == 5 or 7 == 7)  # True + True = True
print(5 == 7 or 7 == 7)  # False + True = True
print(
    5 == 5 or 7 != 7
)  # True + False = True => 첫 번째 조건이 True라면 뒤에 조건을 확인 안 함

# not: 부정연산자 -> 값을 반대로 뒤집음
print(not True)  # False가 나온다다
print(
    not 5 == 5
)  # 5 == 5를 연산하여 True를 반환 -> not True로 동작하기에 True를 뒤집어 False를 반환 -> 반환받은 False를 터미널로 출력
