# 딕셔너리로 정확하게 역할까지 부여하기

# 딕셔너리 안에는 1:1 대응으로 연결되어야 한다.
data_class_dict = {"반장": "태구", "부반장": "수진", "당번": "영준"}

# 센서로부터 얻는 예시 데이터로 딕셔너리를 만들어보기
sensors = {"센서이름": "보일러", "모터온도": 78, "진동": 0.5}
print(sensors)
print(type(sensors))

empty = {}
print(type(empty))

# 키 값을 가져와서 value를 출력할 수 있다.
print(sensors["모터온도"])
print(sensors["진동"])

# 기존에 있던 key의 값을 변경하기
sensors["센서이름"] = "펌프"  # 센서이름 값 변경
print(sensors)
sensors["진동"] = 0.7  # 진동값이 변경된다.

# 기존에 없던 key 값을 추가
sensors["펌프압력"] = 95
sensors["유량"] = 42
print(sensors)

# 더 이상 필요없는 key와 그 value를 삭제 -> 조합 전체가 삭제된다.
del sensors["펌프압력"]
del sensors["모터온도"]
print(sensors)

# get으로 없는 키 가져오기(get 유무의 차이)
print(sensors["센서이름"])
print(sensors.get("센서이름"))

# print(sensors["모터온도"]) # 더 이상 벗는 key를 호출하면 에러 발생
print(sensors.get("모터온도"))  # 없는 key를 호출하면 None 반환

# motor_degree에 숫자가 안담기면 에러 발생
motor_degree = sensors.get(
    "모터온도", 0
)  # 근데 get으로 default값을 0으로 설정하면 에러가 발생하지 않는다. (없으면 0 반환)
# 이미 위에서 지웠기 때문에 none이 반환되어 숫자가 아니기에 10을 더하면 에러가 발생
next_degree = motor_degree + 10
print(next_degree)

# 값이 있는지 여부 확인
is_mortor_degree_key = "모터온도" in sensors
print(is_mortor_degree_key)  # False

if is_mortor_degree_key:
    print("그런 키 있어요")
else:
    print("그런 키 없어요")

# 위 코드는 이렇게 보통 쓰인다.
if "모터온도" in sensors:
    print("그런 키 있어요")
else:
    print("그런 키 없어요")

# 딕셔니리 키가 될 수 있는것 -> 문자열, 숫자, 튜플 (리스트는 불가)

# keys와 values로 키, 값만 꺼내기
print(sensors.keys())  # 딕셔내리 안에 key들을 가져온 것
print(sensors.values())  # 딕셔내리 안에 value들을 가져온 것

# len을 통해 몇 개의 key-value들이 있는지 살펴보기
print(len(sensors))

if len(sensors) < 5:
    print("내용이 부족해요")

for key, value in sensors.items():
    print(key)
    print(value)

# 위와 같이 사용하기 보다는, 의미있는 이름을 사용한다.
for name, value in sensors.items():
    print(name)
    print(value)

# 추가 예시:
# 나라 이름들로 정리해봅시다.
# 유럽: 스페인(ESP), 프랑스(FRA), 독일(GER), 스위스(SUI), 네덜란드(NED)
# 아시아: 한국(KOR), 일본(JPN), 중국(CHN), 사우디(SAUI), 이란(IRN)
# 남미: 아르헨티나(ARG), 브라질(BRA), 칠레(CHI), 콜롬비아(COL), 우루과이(URU)

korea = {"국가명": "대한민국", "약칭": "KOR"}
japan = {"국가명": "일본", "약칭": "JPN"}
asia = [korea, japan]
print(asia)

print("=== 과제 ===")
# 유럽 나라들을 하나의 리스트로 모아봅시다.
europe = [
    {"국가명": "스페인", "약칭": "ESP"},
    {"국가명": "프랑스", "약칭": "FRA"},
    {"국가명": "독일", "약칭": "GER"},
    {"국가명": "스위스", "약칭": "SUI"},
    {"국가명": "네덜란드", "약칭": "NED"},
]

# 값을 한 번에 출력하는 경우:
# for i in range(len(europe)):
#     print(europe[i])

# .items를 사용해서 출력하는 경우:
# for i in range(len(europe)):
#     for key, value in europe[i].items():
#         print(f"{key}: {value}")

# for문을 만들어서 순회하면서 출력하기
for country in europe:
    # print(country.get("국가명"))
    for key, value in country.items():
        print(f"{key} {value}")


# for country in europe:
#     print(country.get("국가", "국가 없음"))


print("=== 순회하며 임계값과 비교하기 ===")
# 다음 두 딕셔너리는 같은 key들을 가지고 있습니다.
# 실제 데이터
values = {"모터온도": 95, "압력": 80}
# 임계치 데이터
limits = {"모터온도": 90, "압력": 90}

for name, value in values.items():
    # print(f"{name} : {value}")

    if value > limits.get(
        name, 0
    ):  # limits 딕셔너리에서 name에 해당하는 key의 value를 가져오고, 없으면 0을 반환
        print(name, "경고")


print("=== update ===")
sensors = {"모터온도": 78, "진동": 0.5}
new_data = {
    "모터온도": 80,
    "유량": 42,
}  # 기존에 모터온도가 있었으므로 값만 바꿔주고 새로 들어온 값만 추가해주는 방식으로 진행된다.
sensors.update(
    new_data
)  # update를 통해 새로운 데이터를 추가하거나 기존 데이터를 갱신할 수 있다.
print(sensors)  # {'모터온도': 80, '진동': 0.5, '유량': 42}


# zip으로 키들의 배열과 value들의 배열을 묶어서 새로운 딕셔너리를 만들 수 있습니다.
print("=== zip ===")

names = ["모터온도", "진동", "압력"]
values = [78, 0.5, 95]
sensors = dict(zip(names, values))
print(sensors)
