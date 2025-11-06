# 8
print(3 * 5 + 2 ** 2 / 8)
print(True or False and 3 < 4 or not(5 == 7))
print(True or (3 + 5 and 6) >= 2)
# print(not True > 'A') 잘못된 표현식
# print(7 % 4 + 3 // 6 * 'Z')
# print('D' * 1 + 'I' * 1 + 'M' * 2 / 3)
print(5.0 // 3 + 3 / 3)
print(53 % 21 < 45 / 18)
print((4 - 6) or True and False or False and (2 > 3))

# 9 다음의 자바 문장에 잘못된 부분이 있는지 알아보고, 만약 올바르다면 출력결과를, 그렇지 않다면 그 이유를 서술하세요.

print("May 13, 1988 fell on day number ")
print(((13 + (13 * 3 - 1) / 5
        + 1988 + 1988 / 4 + 1988 % 100 / 4
        + 1988 % 400 - 2 * (1988 / 100)) % 7 + 7) % 7);
# zeller의 공식 : 1998년 3월 13일의 요일 계산
# q:일, m:월, k:연도(뒷두자리), j:연돈(앞두자리)

print("Check out this line  ")
# print(//hello there " + '9' + 7) 문자열이 나오다가 7숫자가 나와서 안되서 형변환이 필요
# print('H' + 'I' + " is " + 1 + "more example")        형변환필요
# print('H' + 6.5 + 'I' + " is " + 1 + "more example")  형변환필요
print("Print both of us", "Me too")
print("Reverse " + 'I' + 'T')
#print("Nonot Here is" + 1 + "more example")        형변환필요
#print("Here is " + 10*10)) // that’s 100 ;         괄호가 짝이 안맞음
#print("Not x is " + True) // that’s True.          형변환필요
print()
# print;                                            괄호가 없어 수식이 안맞음
# print("How about this one" ++ '?' + 'Huh?')       연산자 +이 두개


# 22 윤년(leap year)
# 1년은 365일이지만, 실제는 365.24일
# 이러한 오차를 보정하기 위해
# 4년에 한번씩 2월에 29일까지 지정 (평년에는 28일)
# 판정기준
# a:현제연도가 4로 나누어 떨어지지만, 100으로는 나눠 떨어지지 않음
# b:현제 연도가 400으로 나눠 떨어지면 윤년

#year = 2025
#year = int(input('원하시는 년도를 넣어 주세요: '))
#result = '윤년'  if((year % 4 == 0) and (year % 4 == 0) or (year % 400 == 0)) else '평년'
#print(result)

# 파이썬 표준라이브러리를 사용하면 편하게 코그 작성 가능
#import calender

#print(calender.islerp(2024))
#print(calender.islerp(2025))

# 35 - 거스름돈 계산
# 지불할 금액 : 32100
# 지불한 금액 : 50000
# 거스름 금액 : 17900

# Income = int(input('지불할 금액은 : '))
# expenses = int(input('지불한 금액은 : '))
# charge = expenses - Income
#
# print('거스름돈:', charge)
#
# n50000 = int(charge / 50000)
# print('50000원: ', int(n50000), '개')
# charge = charge - (50000 * n50000)
#
# n10000 = int(charge / 10000)
# print('10000원: ', int(n10000), '개')
# charge = charge - (10000 * n10000)
#
# n5000 = charge / 5000
# print('5000원: ', int(n5000), '개')
# charge = charge - (5000 * n5000)
#
# n1000 = charge / 1000
# print('1000원: ', int(n1000), '개')
# charge = charge - (1000 * n1000)
#
# n500 = charge / 500
# print('500원: ', int(n500), '개')
# charge = charge - (500 * n500)
#
# n1000 = charge / 100
# print('100원: ', int(n100), '개')
# charge = charge - (100 * n100)
#
#
# n50 = charge / 50
# print('50원: ', int(n50), '개')
# charge = charge - (500 * n50)
#
# n10 = charge / 10
# print('10원: ', int(n10), '개')
# charge = charge - (10 * n10)

# ---------------

product = 32100
pay = 50000
charge = pay - product

print(f'물건가격 : {product}, 지불금액 : {pay}, '
      f'거스름돈 : {charge}')

# 잔돈 계산
n50000 = charge // 50000
charge = charge % 50000

n10000 = charge // 10000
charge = charge % 10000

n5000 = charge // 5000
charge = charge % 5000

n1000 = charge // 1000
charge = charge % 1000

n500 = charge // 500
charge = charge % 500

n100 = charge // 100
charge = charge % 100

n50 = charge // 50
charge = charge % 50

n10 = charge // 10
charge = charge % 10

# 계산 결과 출력
# print(f'거스름돈 총액 : {(pay - product0)} 원')
# print(f'50000원: {n50000} 개')
# print(f'10000원: {n10000} 개')
# print(f'5000원: {n5000} 개')
# print(f'1000원: {n1000} 개')
# print(f'500원: {n500} 개')
# print(f'100원: {n100} 개')
# print(f'50원: {n50} 개')
# print(f'10원: {n10} 개')

pfmt = f'''
거스름돈 총액 : {(pay - product)} 원
50000원: {n50000} 개
10000원: {n10000} 개
5000원: {n5000} 개
1000원: {n1000} 개
500원: {n500} 개
100원: {n100} 개
50원: {n50} 개
10원: {n10} 개
'''
print(pfmt)