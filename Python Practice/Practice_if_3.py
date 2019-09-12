# 제어문 - if문 실습_3

# 조건이 세 개 이상인 경우

# 5000원 이상 : 아웃백 / 3000원 이상 : 학식 / 1000원 이상 : 컵라면 / ㅠㅠ : 공기밥

won = int(input("돈 얼마 있어?"))

if won >= 5000:
    print("아웃백 가자")

elif won >= 3000:
    print("학식")

elif won >= 1000:
    print("컵라면")

else:
    print("공기밥")
