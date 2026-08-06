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
