# 실습 1.
print("=== 실습 1번 ===")

tup = [("모터온도", 78)]

print(tup[0])
print(tup[0][0])
print(tup[0][1])
for 제품, 온도 in tup:
    print(제품, 온도)


s1 = ("모터온도", 78)
print(s1)
print(s1[0])
print(s1[1])
name, value = s1
print(name, value)

# 실습 2.
print("=== 실습 2번 ===")

tup_1 = [("모터온도", 77), ("모터진동", 0.2), ("모터압력", 91)]

for status, num in tup_1:
    if num > 90:
        print(status, "경고")

# 실습 3.
print("=== 실습 3번 ===")

# sensors = [
#     ("모터온도", 78, (3, 5)),
#     ("베어링진동", 0.5, (7, 2)),
#     ("펌프압력", 95, (4, 8)),
# ]

# for name, value, pos in sensors:
#     print(name, value, pos)

# for i in range(0, 2):
#     if pos[i] <= 5:
#         print(pos[i])

sensors = [
    ("모터온도", 78, (3, 5)),
    ("베어링진동", 0.5, (7, 2)),
    ("펌프압력", 95, (4, 8)),
]

for name, value, pos in sensors:
    x, y = pos
    print(name, "위치:", x, y)
    for name, value, pos in sensors:
        x, y = pos
        if x <= 5:
            print(name, "1구역")

print("=== 실습 3번 ===")

sensors = [
    ("모터온도", 78, (3, 5)),
    ("베어링진동", 0.5, (7, 2)),
    ("펌프압력", 95, (4, 8)),
]

for name, value, (x, y) in sensors:
    print(name, (x, y))
    if x <= 5:
        print(name)
