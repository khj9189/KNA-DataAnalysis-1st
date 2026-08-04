# ①한 줄에 "센서명,측정값" 형태인 행 문자열들을 리스트로 저장
# ②for로 각 행을 쉼표로 split해 이름과 값으로 나누기
# ③이름을 키, 값을 숫자로 바꿔 딕셔너리에 추가

sensors = ["진동모터,78", "회전모터,80", "감속모터,75"]

sensors_list = []
new_dic = {}

for sensor in sensors:
    sensors_list.append(sensor.split(","))
    for i in range(len(sensors_list)):
        new_dic[sensors_list[i][0]] = int(sensors_list[i][1])
print(new_dic)

# for i in sensors:
#     name = i.split(",")
#     new_dic[name[0]] = int(name[1])
# print(new_dic)
