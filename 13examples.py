# # 23 복권 - 반복문으로 재작성
# import random
#
# match = 0
# prize = 0
#
# lotto = str(random.randint(123, 789)) # 난수 생성
# mykey_input = input('복권 숫자 3자리를 입력하세요 (예:123): ')
#
# try:
#     mykey = str(int(mykey_input))
# except ValueError:
#     print("잘못된 입력입니다. 프로그램을 종료합니다.")
#     exit()
# for i in range(3):
#      if lotto[i] in mykey:
#         match += 1
#
# # 3. 상금 계산
# if match == 3:
#     prize = 1000000 # 3개 일치 시 100만원
# elif match == 2:
#     prize = 100000 # 2개 일치 시 10만원
# elif match == 1:
#     prize = 10000 # 1개 일치 시 1만원
#
# result = f'''
# 당첨번호: {lotto}
# 당신의 복권 번호: {mykey}
# 일치한 숫자 갯수: {match}
# 당첨 금액: {prize}원
# '''
#
# print(result)

#------------------------------------------------------
# # 24 구구단 - 반복문으로 재작성
# dan = int(input('출력할 구구단 단수를 입력하세요(1-9): '))
#
# if 1 <= dan <= 9:
#     result = f'=== {dan}단 ===\n'
#     for i in range(1, 10):
#         result += f'{dan} x {i} = {dan * i}\n'
# else:
#     result = '잘못 입력하셨습니다.'
#
# print(result)
#
#
#

# #------------------------------------------------------
# # 26 숫자 맞추기 - 반복문 추가
# import random
# result = ''
# number = random.randint(1, 100) # a: 와 b: 를 제거했습니다.
#
#
# for _ in range(1, 25+1):
#     mynum = int(input('1-100사이 숫자를 하나 입력하세요: '))
#     result = '빙고! 숫자를 맞췄습니다.'
#     if mynum < number: result = '추측한 숫자가 작아요.'
#     elif mynum > number: result = '추측한 숫자가 커요.'
#     elif number == mynum: break
#     print(result)
#
# print(f'{number} : {result}')

#------------------------------------------------------
# 30 구구단 테이블 - 반복문으로 재작성

result1 = f'''
          Multiplication Table
    1   2   3   4   5   6   7   8   9
---------------------------------------
'''
print(result1)

for i in range(1, 9+1):
    result = f'{i} | {i * 1:3d} {i * 2:3d} {i * 3:3d} {i * 4:3d} {i * 5:3d} {i * 6:3d}' \
              f'{i * 7:3d} {i * 8:3d} {i * 9:3d}\n' \

print(result)




# #------------------------------------------------------
# # 32 주민번호 검사 - 반복문으로 재작성
# jumin = '751113-1332927'
# sum = 0
#
# # 계산식
# wght = 2
# for i in range(0, 5+1):
#     sum += int(jumin[i]) * (wght+i)
#
# for i in range(7, 8+1):
#     print(jumin[i], wght + (i - 1), end=', ')
#     sum += int(jumin[i]) * (wght + (i - 1))
#
# for i in range(9, 12+1):
#     print(jumin[i], wght + (i - 9), end=', ')
#     sum += int(jumin[i]) * (wght + (i - 9))
#
# # 출력
# print(sum)

# #c,d
# checker = 11 - sum % 11
# print(checker, str(checker)[-1] == jumin[13])