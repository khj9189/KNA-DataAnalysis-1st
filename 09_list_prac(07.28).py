# 실습1.

# temps = [25, 26, 24, 27, 26]
# empty = []

# print(temps, len(temps), empty, len(empty))

# 실습 2.

# temper = [1, 2, 3, 4, 5, 6]

# print(temper[0])
# print(temper[2])
# print(temper[-1])

# 실습 3.

# product = [123, 124, 125, 126, 127, 128]

# a = product[0]
# b = product[-1]

# sum = a + b
# print(sum)

# avg = (a + b) / 2

# print(avg)

# 실습 4.

# temps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = temps[:3]
# print(temps[:3])
# print(temps[-3:])
# print(len(a))

# 실습 5.

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# first = num[:6]
# print(first)

# second = num[-6:]
# print(second)

# print(len(first), len(second))

# 실습 6.

# temp = [20, 30, 240, 50]

# print(240 in temp)

# i = temp.index(240)

# # print(i)

# temp[i] = 24

# print(temp)

# print(240 in temp)


# 실습 7.

# emp = []
# emp.append(10)
# print(emp)
# emp.insert(0, 9)
# print(emp)
# emp.extend([31, 32])
# print(emp)

# 실습 8.

# num = [25, 26, 24, 28, 27, 999]

# num.remove(999)
# print(num)

# x = num.pop(4)
# print(x)

# del num[:1]
# print(num)

# 실습 9.

temp = [0, -1, 4, 3, 9, 10]

temp.sort()
print(temp)

temp.reverse()
print(temp)

print(temp.count(10))
print(temp.index(10))
