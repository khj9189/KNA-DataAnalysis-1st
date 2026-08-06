# 실습 3.
print("=== 실습3. ===")
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("반가워요\n")
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.read()
    print(lines)
# 뒤에를 w로 쓰게 되면 기존 것들이 없어진다.
