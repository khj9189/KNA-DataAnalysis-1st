# 실습 2.
print("=== 실습2. ===")
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요\n")
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.read()
    print(lines)
# w로 쓰게 되면 내용이 저장이 안된다. 그렇기에 계속 기록을 하고 싶다면 a로 적어야 한다.
