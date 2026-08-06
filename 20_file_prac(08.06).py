# 실습 1.
print("=== 실습1. ===")
f = open("sample.txt", "r", encoding="utf-8")
lines = f.read()
print(lines)
f.seek(0)
lines_by_lines = f.readlines()
print(lines_by_lines)
f.close()

# 실습 1. 추가
print("=== 실습1. 추가 ===")
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.read()
    print(lines)
    f.seek(0)
    lines_by_lines = f.readlines()
    print(lines_by_lines)


# 실습 2.
print("=== 실습2. ===")
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요\n")
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.read()
    print(lines)
# w로 쓰게 되면 내용이 저장이 안된다. 그렇기에 계속 기록을 하고 싶다면 a로 적어야 한다.

# 실습 3.
print("=== 실습3. ===")
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("반가워요\n")
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.read()
    print(lines)
# 뒤에를 w로 쓰게 되면 기존 것들이 없어진다.
