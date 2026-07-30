# 기존 배열의 모든 요소에 3을 곱한 값을 가진 새 리스트를 생성

temps = [1, 5, 2, 7, 4, 8, 10, 3]

doubled = []

for t in temps:
    doubled.append(t * 3)

print(doubled)

# 조건에 맞는 값으로 새 리스트 만들기

# temps = [1, 5, 2, 7, 4, 8, 10, 3]

high = []
low = []

for t in temps:
    if t < 5:
        low.append(t)
    else:
        high.append(t)

print("high:", high)
print("low:", low)
print(low.sort())
