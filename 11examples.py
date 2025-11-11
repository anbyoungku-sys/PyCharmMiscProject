#21
# # 변수 지정
# salary = 0          #연봉 입력
# married = ''        #결혼 여부 입력
# tax_rate = 0.0      #세율 결정용
# tax = 0.0           #계산된 세금
#
# # 입력
# married = input('결혼 여부를 입력해 주세요 (Y:결혼/N:미혼): ').lower()
# salary = int(input('연봉 입력해 주세요(만원단위): '))
# tex = 0
# rate = 0
#
# # 계산식
# if married == 'y':  # 결혼한 경우
#     if salary <= 6000:
#         tax = tax_rate * 0.1
#     else:
#         tax = tax_rate * 0.25
# elif married == 'n':  # 미혼인 경우
#     if salary <= 3000:
#         tax = tax_rate * 0.1
#     else:
#         tax = tax_rate * 0.25
# else:
#     print("잘못된 입력입니다.")
#     tax_rate = 0  # 잘못된 입력 시 세율 0 처리
# #
# # 출력
# print(f'적용 세율: {tax_rate * 100:.0f}%')
# print(f'납부해야 할 세금은 {tax:.1f}만 원입니다.')

# # 2차 수정
# # 입력
# married = input('결혼 여부를 입력해 주세요 (Y:결혼/N:미혼): ').lower()
# salary = int(input('연봉 입력해 주세요(만원단위): '))
# tex = 0
# rate = 0
#
# # 계산식
# if married == 'y':  # 결혼한 경우
#     rate = 25
#     if salary <= 6000:
#         rate = 10
# elif married == 'n':  # 미혼인 경우
#     rate = 25
#     if salary <= 3000:
#         rate  =10
# else:
#     print("잘못된 입력입니다.")
#     tax_rate = 0  # 잘못된 입력 시 세율 0 처리
#
# tax = salary * (rate / 100)
# tax = salary * (rate / 250)
#
# # 출력
# result f'''
# 적용 세율: {rate}%
# 납부해야 할 세금은 {tax} 만원입니다.
# '''


#------------------------------------------------------
#23
# match += 1   # match = match + 1
# if num3 == key1 or num3 == key2 or num3 == key3:
#    match += 1   # match = match + 1

import random

# 문자열 슬라이싱을 위해 문자열형으로 변환
lotto = str(random.randint(123, 789)) # 난수 생성
# 문자열 슬라이싱을 위해 문자열형으로 입력 받음
mykey = input('복권 숫자 3자리를 입력하세요 (예:123): ')
mykey = str(int(mykey)) # 입력값을 정수로 변환 후 문자열로 다시 변환하여 혹시 모를 앞의 0을 제거하고, str로 만들어 비교 가능하게 함

# 테스트를 위한 값 (실제 실행 시 위 input 사용)
# lotto = str(357) # 난수로 생성한 3자리 숫자
# mykey = str(735) # 사용자가 입력한 3자리 숫자

match = 0  # 일치수식
if lotto[0] == mykey[0] or lotto[0] == mykey[1] or lotto[0] == mykey[2]:
    match = match + 1 # match =+ 1은 잘못된 구문, match = match + 1로 수정
if lotto[1] == mykey[0] or lotto[1] == mykey[1] or lotto[1] == mykey[2]:
    match = match + 1
if lotto[2] == mykey[0] or lotto[2] == mykey[1] or lotto[2] == mykey[2]:
    match = match + 1

# 상금 계산 (예시)
prize = 0
if match == 3: prize = 1000000 # 3개 일치 시 100만원
elif match == 2: prize = 100000 # 2개 일치 시 10만원
elif match == 1: prize = 10000 # 1개 일치 시 1만원

result = f'''
당첨번호: {lotto}
당신의 복권 번호: {mykey}
일치한 숫자 갯수: {match}
당첨 금액: {prize}원
'''

print(result)


#-------------------------------------------------------------------------
#26
# 변수 지정
import random

# 1-100 사이의 임의의 숫자 생성
number = random.randint(1, 100) # a: 와 b: 를 제거했습니다.
#
mynum = int(input('1-100사이 숫자를 하나 입력하세요: '))
#
result = '' # result 변수를 미리 초기화

if mynum == number: # 입력값과 생성된 숫자가 같을 때
    result = '빙고! 숫자를 맞췄습니다.'
elif mynum < number: # 입력값이 생성된 숫자보다 작을 때 (mynum < number 로 변경)
    result = '추측한 숫자가 작아요.'
else: # 입력값이 생성된 숫자보다 클 때 (mynum > number 로 변경, elif number > mynum 대신 else 사용)
    result = '추측한 숫자가 커요.'

print(f'숫자 : {number}, 결과 : {result}')


#-------------------------------------------------------------------------

#31임의의 숫자 6자리를 입력하면 신용카드의 종류와 은행정보를 출력하는 프로그램을 작성하세요.
# 3 (JCB카드)
# 3563 17 - NH농협카드,
# 3569 01 - 신한카드,
# 3569 12 - KB국민카드
#
# 4 (비자카드)
# 4048 25 - 비씨카드,
# 4386 76 - 신한카드,
# 4579 73 - 국민은행
#
# 5 (마스터카드, Maestro)
# 5155 94 - 신한카드,
# 5243 53 - 외환카드,
# 5409 26 - 국민은행
# 변수 지정

# 출력
# 6자리 카드 번호를 입력하세요: 356317
# 카드 종류 및 은행 : JCB카드 - NH농협카드
#
# 6자리 카드 번호를 입력하세요:356999
# 카드 종류 : JCB카드, 은행정보는 등록되지 않았습니다.

# cad = 0     # 입력 카드 값
# bak1 = 0    # JCB카드사
# bak2 = 0    # 바자카드사
# bak3 = 0    # 마스타카드사
#
# # 입력
# cad = int(input('6자리 카드 번호를 입력하세요: '))
#
# # 계산식
# bak1 = cad // 100000
#
# if bak1 == 3:
#         match cad:
#             case 356317:
#                 grade = 'JCB카드 - NH농협카드'
#             case 356901:
#                 grade = 'JCB카드 - 신한카드'
#             case 356912:
#                 grade = 'JCB카드 - 국민카드'
#             case _:
#                 grade = 'JCB카드가 아닙니다.'
# elif bak1 == 4:
#         match cad:
#             case 404825:
#                 grade = '비자카드 - 비씨카드'
#             case 404825:
#                 grade = '비자카드 - 비씨카드'
#             case 404825:
#                 grade = '비자카드 - 비씨카드'
#             case _:
#                 grade = '비자카드 아닙니다.'
#
# elif bak1 == 5:
#     match cad:
#         case 515594:
#             grade = '마스타카드 - 외환카드'
#         case _:
#             grade = '마스타 카드가 아닙니다.'
# else:
#     grade = '카드 정보가 없습니다.'
#
# # 출력
# print(grade)
#
# -------------- 수  업 ------------------------
cardnum = input('6자리 카드 번호를 입력하세요: ')
cardtype = '식별안됨'
cardbank = '식별안됨'

if len(cardnum) == 6:
    if cardnum[:2] == '35':
        cardtype = 'JBC카드'
        if cardnum[2:] == '6317': cardbank = 'NH농협카드'
        elif cardnum[:2] == '6901': cardbank = '신한카드'
        elif cardnum[2:] == '6912': cardbank = 'KB국민카드'
        else: cardbank = '은행정보는 등록되지 않았습니다.'
    elif cardnum[0] == '4':
        cardtype = '비자카드'
        if cardnum[1:] == '04825': cardbank = '비씨카드'
        elif cardnum[1:] == '38676': cardbank = '신한카드'
        elif cardnum[1:] == '57973': cardbank = '국민은행'
        else:  cardbank = '은행정보는 등록되지 않았습니다.'
    elif cardnum[0] == '5':
        cardtype = '마스타카드'
        if cardnum[1:] == '15594': cardbank = '신한카드'
        elif cardnum[1:] == '24353': cardbank = '외환카드'
        elif cardnum[1:] == '40926': cardbank = '국민은행'
    else:  cardbank = '은행정보는 등록되지 않았습니다.'
else:
    cardtype = '올바른 카드번호가 아닙니다.'

result = f'''
카드 종류 및 은행: {cardtype} - {cardbank}
'''
print(result)


#32 주민등록번호
# 변수 지정

# 입력
# jumin = input('주민번호를 입력하세요(xxxxxx-yyyyyyyy)')
jumin = '751113-1332927'
sum = 0

# 계산식
sum += int(jumin[0]) * 2
sum += int(jumin[1]) * 3
sum += int(jumin[2]) * 4
sum += int(jumin[3]) * 5
sum += int(jumin[4]) * 6
sum += int(jumin[5]) * 7
sum += int(jumin[7]) * 8
sum += int(jumin[8]) * 9
sum += int(jumin[9]) * 2
sum += int(jumin[10]) * 3
sum += int(jumin[11]) * 4
sum += int(jumin[12]) * 5

# 출력
print(sum)

#c
remainder = sum % 11
print(remainder)

#d
checker = 11 - remainder
print(checker, str(checker)[-1] == jumin[13])