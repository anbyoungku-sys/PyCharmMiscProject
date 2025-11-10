# 10 각 부울 표현식에 대한 값을 계산하세요. 파이썬은 단축식 평가(short-circuit evaluation)를 사용한다는 점에 주의하세요.

#a. True and False and True or True
print(True and False and True or True)
#b. True or True and True and False
print(True or True and True and False)
#c. (True and False) or (True and not False) or (False and not False)
print((True and False) or (True and not False) or (False and not False))
#d. (2 < 3) or (5 > 2) and not (4 == 4) or 9 != 4
print((2 < 3) or (5 > 2) and not (4 == 4) or 9 != 4)
#e. 6 == 9 or 5 < 6 and 8 < 4 or 4 > 3
print(6 == 9 or 5 < 6 and 8 < 4 or 4 > 3)

# 11 다음 중 유효한 표현식을 찾고, 그 결과 값의 데이터 유형을 서술하세요.
#a. 27 / 13 + 4
print(27 / 13 + 4)
# b. 27 / 13 + 4.0
print(27 / 13 + 4.0)
# c. 42.7 % 3 + 18
print(42.7 % 3 + 18)
# d. (3 < 4) and 5 / 8
print((3 < 4) and 5 / 8)
# e. 23 / 5 + 23 / 5.0
print(23 / 5 + 23 / 5.0)
#f. 2.0 + 'a'
# print(2.0 + 'a')
# g. 2 + 'a'
# print(2 + 'a')
# h. 'a' + 'b'
print('a' + 'b')
# i. 'a' / 'b'
# print('a' / 'b')
# j. 'a' and not 'b'
print('a' and not 'b')
# k. ( double ) 'a' / 'b'
# print(( double ) 'a' / 'b')


# 12. 다음 문장의 실행결과는 무엇인지 서술하세요.

n = int(3.9)
print("n == " + n)

# 14. 다음 문장의 실행결과는 무엇인지 서술하세요.

print("2 + 2 = " + (2 + 2))
print("2 + 2 = " + 2 + 2)

# 24 사용자로부터 숫자(1-9)를 하나 입력 받아 구구단을 출력하는 프로그램을 작서해 보세요.
# 단, 1-9 이외의 숫자나 문자를 입력 받으면 "잘못 입력하셨습니다."라는 메시지를 출력하도록 합니다.


# 25 사용자로부터 소문자를 입력 받아 대문자로 출력하는 프로그램을 작성해 보세요.
# 단, 소문자 이위의 숫자나 문자를 입력 받으면 "잘못 입력하셨습니다."라는 메세지를 출력하도록 합니다.
# 문자 입력 - input()  이용

# 30 - 구구단 테이블

# 36 - 시간 계산