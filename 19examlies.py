# # 21 반복 추가
# #--------------------------------수업--------------------------------
# # 입력
# while True:
#     married = input('결혼 여부를 입력해 주세요 (Y:결혼/N:미혼): ').lower()
#     salary = int(input('연봉을 입력해 주세요(만원 단위): '))
#
#     rate = 0  # 세율 초기화
#
#     match married:
#         case 'n':
#             rate = 10 if salary <= 3000 else 25
#         case 'y':
#             rate = 10 if salary <= 6000 else 25
#         case _:
#             print('입력 오류! Y 또는 N을 입력해 주세요.')
#             continue
#
#     # 세금 계산
#     tax = salary * (rate / 100)
#
#     # 출력
#     print(f'''
#     적용 세율: {rate}%
#     납부해야 할 세금은 {tax:.1f}만원입니다.
#     ''')
#
#     # 계속 여부 확인
#     cont = input('계속하겠습니까? (Y/N): ').lower()
#     if cont == 'n':
#         print("프로그램을 종료합니다.")
#         break

# #------------------------------- 내가 --------------------------------
#
# # 2차 수정
# # 입력
# married = input('결혼 여부를 입력해 주세요 (Y:결혼/N:미혼): ').lower()
# salary = int(input('연봉 입력해 주세요(만원단위): '))
# rate = 0
# tax = 0
#
# # 계산식
# while True:
#     if married == 'y':
#         rate = 25
#         if salary <= 6000: rate = 10
#         break
#     elif married == 'n':
#         rate = 25
#         if salary <= 3000: rate = 10
#         break
#     else:
#         print("잘못된 입력입니다.")
#         tax_rate = 0  # 잘못된 입력 시 세율 0 처리
#
# if married == 'y': married_text = '결혼'
# else: married_text = '미혼'
#
# tax = salary * (rate / 100)
# tax = salary * (rate / 250)
#
# input('계속하겠습니까? (y/n)').lower()
# if cont == 'n': break
#
# # 출력
# result = f'''
# -------- 세금 계산 결과 ------------
# 결혼 여부: {married_text}
# 연봉: {salary} 만원
# 적용 세율: {rate}%
# ---------------------------------
# 납부해야 할 세금은 {tax:.0f}만원입니다.
# '''
#
# print(result)

# #--------------------  23 중첩  --------------------------------------
# #-----------------------수업------수업--------------------------------
# import random
#
# lotto = str(random.randint(123, 789))
# mykey = input('복권 숫자 3자리를 입력하세요 (예:123): ')
# mykey = str(int(mykey)) # 입력값을 정수로 변환 후 문자열로 다시 변환하여 혹시 모를 앞의 0을 제거하고, str로 만들어 비교 가능하게 함
#
# match = 0  # 일치수식
# for i in range(3):
#     for j in range(3):
#         if lotto[i] == mykey[j]: match += 1
#
# # 상금 계산 (예시)
# prize = 0
# if match == 3: prize = '100만원' # 3개 일치 시 100만원
# elif match == 2: prize = '10만원' # 2개 일치 시 10만원
# elif match == 1: prize = '만원' # 1개 일치 시 1만원
#
# result = f'''
# 당첨번호: {lotto}
# 당신의 복권 번호: {mykey}
# 일치한 숫자 갯수: {match}
# 당첨 금액: {prize}원
# '''
#
# print(result)

# #-------------------------------- 내 가 --------------------------------

# import random
#
# lotto = str(random.randint(123, 789))
# mykey = input('복권 숫자 3자리를 입력하세요 (예:123): ')
# mykey = str(int(mykey))
#
# i = 0
# match = 0
# while i < len(lotto):
#     j = 0
#     while j < len(mykey):
#         if lotto[i] == mykey[j]:
#             match += 1
#             break # 일치하는 번호를 찾았으면 다음 로또 번호로 넘어감
#         j += 1
#     i += 1
#
# # 상금 계산 (예시)
# prize = "'꽝' 다음기회를!!!"
# if match == 3: prize = '100만원' # 3개 일치 시 100만원
# elif match == 2: prize = '10만원' # 2개 일치 시 10만원
# elif match == 1: prize = '만원' # 1개 일치 시 1만원
#
# result = f'''
# 당첨번호: {lotto}
# 당신의 복권 번호: {mykey}
# 일치한 숫자 갯수: {match}
# 당 첨357 : {prize}
# '''
#
# print(result)

# #-----------------------------------------------------------------------
# import random
#
# number = random.randint(1, 100) # a: 와 b: 를 제거했습니다.
#
# while True:
#     mynum = int(input('1-100 사이 숫자를 하나 입력하세요: '))
#
#     if mynum > number:
#         print('추측한 숫자가 커요.')
#     elif mynum < number:
#         print('추측한 숫자가 작아요.')
#     else:
#         print('빙고! 정답입니다!')
#         break  # 정답이면 반복 종료
#
# print(f'정답은 {number}입니다.')


# #---------------------------  30  중첩 --------------------------------
# #--------------------------------수  업--------------------------------
# result = f'''
#           Multiplication Table
#       1   2   3   4   5   6   7   8   9
# ---------------------------------------
# '''
#
# for i in range(1, 9+1):
#     result += f'{i} |'
#     for j in range(1, 9+1):
#         result += f'{i * j:4d}'
#     result += '\n'
#
# print(result)


# #------------------------------- 내가  --------------------------------

# result = f'''
#         Multiplication Table
#        1   2   3   4   5   6   7   8   9
#   --------------------------------------
# '''
#
# i = 1
# while i <= 9:
#     result += f'{i:3d}|'
#     j = 1
#     while j <= 9:
#         result += f'{i*j:4d}'
#         j += 1
#     result += '\n'
#     i += 1
#
# print(result)

#----------------------------- 31 중첩 ------------------------------
# #--------------------------------수업--------------------------------
# cardnum = input('6자리 카드 번호를 입력하세요: ')
# cardtype = '식별안됨'
# cardbank = '식별안됨'
#
# if len(cardnum) == 6:
#     match cardnum[0]:
#         case '3':
#             cardtype = 'JCB카드'
#             match cardnum[1:]:
#                 case '56317': cardbank = 'NH농협카드'
#                 case '56901': cardbank = '신한카드'
#                 case '56912': cardbank = 'KB국민카드'
#                 case _: cardbank = '은행정보는 등록되지 않았습니다.'
#         case '4':
#             cardtype = '비자카드'
#             match cardnum[1:]:
#                 case '04825': cardbank = '비씨카드'
#                 case '38676': cardbank = '신한카드'
#                 case '57973': cardbank = '국민은행'
#                 case _: cardbank = '은행정보는 등록되지 않았습니다.'
#         case '5':
#             cardtype = '마스타카드'
#             match cardnum[1:]:
#                 case '15594': cardbank = '신한카드'
#                 case '24353': cardbank = '외환카드'
#                 case '40926': cardbank = '국민은행'
#                 case _: cardbank = '은행정보는 등록되지 않았습니다.'
#
# else:
#     cardtype, cardbank = '올바른 카드번호가 아닙니다.', '식별안됨'
#
#     cardtype = '올바른 카드번호가 아닙니다.'
#     cardbank = '식별안됨'
#
# result = f'''
# 카드 종류 및 은행: {cardtype} - {cardbank}
# '''
# print(result)



# #-------------------------------- 내가 --------------------------------




# #-----------------------------------------------------------
# # 성적 처리프로그램
# # 성적 처리프로그램 V4
# # 학생의 이름, 국어, 영어, 수학, 점수를 키보드로 입력 받아
# # 총점, 평균, 학점을처리한 뒤 결과 출력
# # 성적처리의 CRUD를 메뉴식으로 구현
#
# menus = f'''
# ---------------------
# 성적처리 프로그램 V4
# ---------------------
# 1. 성적데이터 입력
# 2. 성적데이터 조회
# 3. 성적데이터 상세조회
# 4. 성적데이터 수정
# 5. 성적데이터 삭제
# 0. 프로그램 종료
# ---------------------
# 작업을 선택하세요 : '''
# # menus = '''...'''
#
# for i in range(1,100+1):
#     job = input(menus)
#
#     # if job == '1': print('성적데이터 입력을 진행합니다.')
#     # elif job == '2': print('성적데이터 조회를 진행합니다.')
#     # elif job == '3': print('성적데이터 상세조회를 진행합니다.')
#     # elif job == '4': print('성적데이터 수정을 진행합니다.')
#     # elif job == '5': print('성적데이터 삭제를 진행합니다.')
#     # elif job == '0':
#     #     print('성적프로그램을 종료합니다.')
#     #     break
#     # else: print('번호를 잘못입력하셨습니다.')
#
#     match job:
#         case '1': print('성적데이터 입력을 진행합니다.')
#         case '2': print('성적데이터 조회을 진행합니다.')
#         case '3': print('성적데이터 상세조회를 진합니다.')
#         case '4': print('성적데이터 수정을 진행합니다.')
#         case '5': print('성적데이터 삭제을 진행합니다.')
#         case '0':
#             print('성적프로그램을 종료합니다.')
#             break
#         case _: print('번호를 잘못입력하셨습니다.'
#                       '다시 제대로 입력해 주세요: '




# #-----------------------------------------------------------
# # 성적 처리프로그램 V4
# # 학생의 이름, 국어, 영어, 수학, 점수를 키보드로 입력 받아
# # 총점, 평균, 학점을 처리한 뒤 결과 출력
# # 성적처리의 CRUD를 메뉴식으로 구현
#
# # 학생 정보를 저장할 리스트 (각 학생은 딕셔너리로 표현)
# students = []
#
# menus = '''
# ---------------------
# 성적처리 프로그램 V4
# ---------------------
# 1. 성적데이터 입력
# 2. 성적데이터 조회
# 3. 성적데이터 상세조회
# 4. 성적데이터 수정
# 5. 성적데이터 삭제
# 0. 프로그램 종료
# ---------------------'''
#
# # 1. 성적데이터 입력 함수
# def add_student():
#     print('\n--- 1. 성적데이터 입력 ---')
#     name = input("이름: ")
#     # 이미 존재하는 학생인지 확인 (선택 사항)
#     if any(s['이름'] == name for s in students):
#         print(f"'{name}' 학생은 이미 존재합니다. 다른 이름으로 입력하거나 수정을 이용해주세요.")
#         return
#
#     try:
#         korean_score = int(input("국어 점수: "))
#         english_score = int(input("영어 점수: "))
#         math_score = int(input("수학 점수: "))
#     except ValueError:
#         print("점수는 숫자로 입력해야 합니다. 다시 시도해주세요.")
#         return
#
#     # 총점, 평균 계산
#     total = korean_score + english_score + math_score
#     average = total / 3
#
#     # 학점 계산 (간단한 예시)
#     if average >= 90:
#         grade = 'A'
#     elif average >= 80:
#         grade = 'B'
#     elif average >= 70:
#         grade = 'C'
#     elif average >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
#
#     student = {
#         '이름': name,
#         '국어': korean_score,
#         '영어': english_score,
#         '수학': math_score,
#         '총점': total,
#         '평균': average,
#         '학점': grade
#     }
#     students.append(student)
#     print(f"✔ '{name}' 학생의 성적이 저장되었습니다.")
#
# # 2. 성적데이터 조회 함수
# def view_students():
#     print('\n--- 2. 성적데이터 조회 ---')
#     if not students:
#         print("저장된 학생 정보가 없습니다.")
#         return
#
#     print(f"{'이름':<10}{'국어':<6}{'영어':<6}{'수학':<6}{'총점':<6}{'평균':<8}{'학점':<4}")
#     print("-" * 50)
#     for student in students:
#         print(f"{student['이름']:<10}{student['국어']:<6}{student['영어']:<6}{student['수학']:<6}{student['총점']:<6}{student['평균']:.2f:<8}{student['학점']:<4}")
#     print("-" * 50)
#
# # 3. 성적데이터 상세조회 함수
# def detail_view_student():
#     print('\n--- 3. 성적데이터 상세조회 ---')
#     if not students:
#         print("저장된 학생 정보가 없습니다.")
#         return
#
#     name_to_find = input("조회할 학생의 이름을 입력하세요: ")
#     found = False
#     for student in students:
#         if student['이름'] == name_to_find:
#             print(f"\n--- '{name_to_find}' 학생 정보 ---")
#             for key, value in student.items():
#                 if key == '평균':
#                     print(f"{key}: {value:.2f}")
#                 else:
#                     print(f"{key}: {value}")
#             found = True
#             break
#     if not found:
#         print(f"'{name_to_find}' 학생을 찾을 수 없습니다.")
#
# # 4. 성적데이터 수정 함수
# def update_student():
#     print('\n--- 4. 성적데이터 수정 ---')
#     if not students:
#         print("저장된 학생 정보가 없습니다.")
#         return
#
#     name_to_update = input("수정할 학생의 이름을 입력하세요: ")
#     found_index = -1
#     for i, student in enumerate(students):
#         if student['이름'] == name_to_update:
#             found_index = i
#             break
#
#     if found_index != -1:
#         print(f"'{name_to_update}' 학생의 현재 점수: 국어 {students[found_index]['국어']}, 영어 {students[found_index]['영어']}, 수학 {students[found_index]['수학']}")
#         try:
#             new_korean = int(input("새 국어 점수: "))
#             new_english = int(input("새 영어 점수: "))
#             new_math = int(input("새 수학 점수: "))
#         except ValueError:
#             print("점수는 숫자로 입력해야 합니다. 수정이 취소됩니다.")
#             return
#
#         students[found_index]['국어'] = new_korean
#         students[found_index]['영어'] = new_english
#         students[found_index]['수학'] = new_math
#
#         # 총점, 평균, 학점 다시 계산
#         total = new_korean + new_english + new_math
#         average = total / 3
#         if average >= 90:
#             grade = 'A'
#         elif average >= 80:
#             grade = 'B'
#         elif average >= 70:
#             grade = 'C'
#         elif average >= 60:
#             grade = 'D'
#         else:
#             grade = 'F'
#
#         students[found_index]['총점'] = total
#         students[found_index]['평균'] = average
#         students[found_index]['학점'] = grade
#         print(f"✔ '{name_to_update}' 학생의 성적이 성공적으로 수정되었습니다.")
#     else:
#         print(f"'{name_to_update}' 학생을 찾을 수 없습니다.")
#
# # 5. 성적데이터 삭제 함수
# def delete_student():
#     print('\n--- 5. 성적데이터 삭제 ---')
#     if not students:
#         print("저장된 학생 정보가 없습니다.")
#         return
#
#     name_to_delete = input("삭제할 학생의 이름을 입력하세요: ")
#     initial_len = len(students)
#     students[:] = [student for student in students if student['이름'] != name_to_delete] # 리스트 컴프리헨션으로 삭제
#     # for i, student in enumerate(students):
#     #     if student['이름'] == name_to_delete:
#     #         del students[i] # 또는 students.pop(i)
#     #         break
#     if len(students) < initial_len:
#         print(f"✔ '{name_to_delete}' 학생의 성적 정보가 삭제되었습니다.")
#     else:
#         print(f"'{name_to_delete}' 학생을 찾을 수 없어 삭제할 수 없습니다.")
#
#
# # 메인 프로그램 루프
# while True:
#     print(menus)
#     job = input('작업을 선택하세요 : ') # 메뉴 문자열에 포함된 "작업을 선택하세요 :" 문구를 따로 빼냈습니다.
#
#     match job:
#         case '1':
#             add_student()
#         case '2':
#             view_students()
#         case '3':
#             detail_view_student()
#         case '4':
#             update_student()
#         case '5':
#             delete_student()
#         case '0':
#             print('\n성적프로그램을 종료합니다.')
#             break
#         case _:
#             print('\n번호를 잘못입력하셨습니다. 다시 제대로 입력해 주세요: ')
#
# #-----------------------------------------------------------
#
#
#
#
