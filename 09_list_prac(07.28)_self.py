# 문제 1. 기본 인덱싱/슬라이싱
print("=== 1번 ===")
temps = [21, 22, 23, 24, 25, 26]

print(temps[0], temps[-1])
print(temps[2:4])
print(temps[::2])

# 문제 2. 값 존재 확인과 위치 찾기
print("=== 2번 ===")
machines = ["펌프", "압축기", "모터", "밸브", "압축기"]

print("밸브" in machines)

i = machines.index("모터")
print(i)

j = machines.index("압축기")
print(j)

# 문제 3. 값 추가하기
print("=== 3번 ===")
nums = [10, 20, 30]

nums.append(40)
print(nums)

nums.insert(1, 15)
print(nums)

a = [50, 60]
nums.extend(a)
print(nums)

# 문제 4. 값 추가하기
print("=== 4번 ===")
original = [1, 2, 3]

backup = original
backup.append(999)

print(original)
print(backup)

# 문제 5. 값 추가하기
print("=== 5번 ===")

data = [5, 6, 7]

result = data.append(8)

print(result)

# append, insert, extend, remove, sort 이거는 메서드는 리스트를 제자리에서만 수정만 하고
# 반환값은 없음이어서 none 이 나온다.

# 문제 6. 값 추가하기
print("=== 6번 ===")

fruits = ["딸기", "사과", "배", "포도", "수박", "망고"]

fruits.remove("배")
print(fruits)

print(fruits.pop(0))

del fruits[-1]
print(fruits)

# 문제 7. 값 추가하기
print("=== 7번 ===")

stack = [100, 200, 300]

last = stack.pop(-1)
print(last)
print(stack)

# append와 remove는 리스트를 제자리에서만 수정만 하고 반환값은 없음이어서 none이 나오기에 굳이 변수로 저장이 필요 없다.

# 문제 8. 값 추가하기
print("=== 8번 ===")
colors = ["빨강", "노랑", "초록", "파랑", "남색", "보라"]

del colors[::2]
print(colors)


# 문제 9. 순서 추적
print("=== 9번 ===")

# data = [10, 20, 30, 40]

# data.insert(1, 99)  # (1) 10, 99, 20, 30, 40
# data.append(data[0])  # (2) 10, 99, 20, 30, 40, 10
# removed = data.pop(2)  # (3) 10, 99, 30, 40, 10
# data.remove(removed)  # (4) 에러 발생 -> 20 = removed 값인데 이제 더이상 리스트에 20이 없기 때문
