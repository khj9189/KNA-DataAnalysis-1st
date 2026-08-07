# =======================================
print("=== except들의 연속과 finally ===")

# text = "24.5" # 정상
# temp = float(text)  # 형변환의 과정
# print(temp * 2)
text = "영크크"  # 비정상
temp = 0

try:  # except를 요구한다.
    temp = float(text)
except ValueError:
    print("문제가 발생했습니다.")
except NameError:
    print("NameError가 발생했습니다.")
finally:
    # 오류가 있건 없건 finally의 코드를 실행하고 마무리, except가 여러개 있는 경우
    print(temp * 2)  # 성공·실패 무조건 실행
