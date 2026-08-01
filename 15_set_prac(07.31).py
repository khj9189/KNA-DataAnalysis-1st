# 실습 1.
print("=== 실습 1. ===")
ID = ["WQR_01", "WQR_01", "WQR_01", "WQR_01", "WQR_06", "WQR_06", "WQR_03", "WQR_05"]
unique = set(ID)

print(sorted(unique))
print(len(unique))

# 실습 2.
print("=== 실습 2. ===")
logs_1 = {"모터온도", "베어링진동", "펌프압력"}
logs_2 = {"모터온도", "베어링진동", "펌프압력", "베어링 압력", "모터압력", "펌프진동"}

print(logs_1.union(logs_2))
print(logs_2.intersection(logs_2))
print(logs_2.difference(logs_1))


# 실습 6.
print("=== 실습 6. ===")
logs_t = {"09", "08", "01"}
logs_y = {"09", "07", "02", "01"}

print("신규이상:", logs_t - logs_y)
print("지속이상:", logs_y.intersection(logs_t))
