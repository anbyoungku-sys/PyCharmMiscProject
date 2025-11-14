# # 21 - 함수로 재작성 : computeTax
# #--------------------------------수업--------------------------------
# from anbyku.examples_libv1 import compute_tax
#
# while True:
#     salary = int(input('연봉을 입력하세요(만원 단위): '))
#     isMarried = input('결혼 여부를 입력하세요 (y:결혼, n:미혼)?').lower()
#
#     rate, tax = compute_tax(isMarried, salary)
#
#     result = f'''
#     적용세율 : {rate}%
#     납부해야 할 세금은 {tax}만원입니다
#     '''
#
#     print(result)  # 결과를 출력합니다.
#
#     cont = input('계속하시겠습니까? (y/n)').lower()  # 계속할지 여부를 사용자에게 묻습니다.
#     if cont == 'n':
#         break  # 'n'을 입력하면 루프를 종료합니다.
#





#
#
# # 23 - 함수로 재작성 : lotto999
# import random
# from anbyku.examples_libv1 import count_matches
# from anbyku.examples_libv1 import get_prize
#
# lotto = str(random.randint(123, 789))
# mykey = input('복권 숫자 3자리를 입력하세요 (예:123): ')
#
#
# match = count_matches(mykey, lotto)
# prize = get_prize(match)
#
#
# result = f'''
# 당첨번호 : {lotto}
# 당신의 복권번호 : {mykey}
# 일치한 숫자 개수 : {match}
# 당첨 금액 : {prize}원
# '''
#
# print(result)


# # 24 - 함수로 재작성 : gugudan
# from anbyku.examples_libv1 import generate_gugudan
#
# dan = int(input('출력할 구구단 단수를 입력하세요(1-9): '))
#
# result = generate_gugudan(dan)
#
# print(result)
#


# 32 - 함수로 재작성 : checkJumin
import random

from anbyku.examples_libv1 import check_Jumin

jumin = '751113-1332927'

code, wght, sum, isvalid =check_Jumin(jumin)
print(code, wght, sum, isvalid)

