# 시퀸스 자료형
# 값들이 일정한 순서를 가지고 나열된 형태의 자료구조
# 여러 데이터를 순서대로 저장하고, 인덱스로 접근할 수 있음
# 연산기능 : 인덱싱, 슬라이싱, 반복, 길이, 멤버쉽 연산
# 리스트, 튜플, 문자열
#
# 자료구조
# 데이터를 효율적으로 저장하고, 관리, 활용하기 위한 방법, 구조
# 데이터는 어떻게 저장하고, 어떻게 꺼내고,
# 지우고, 검색하는 것이 좋을까에 대해 연구하는 설계하는 학문
#
# 리스트
# 동일한 자료형(type)의 여러개 데이터를
# 하나의 변수에 순서대로 저장할 수 있는 자료 구조
# 리스트는 []로 표현하고, 각 요소는 (,)로 구분

# #lunches = ['라면', '김밥', '뚝불', '돈까즈', '자장면']
# lunches = ['라면', '김밥', '뚝불', '돈까즈', '자장면']
# print(lunches)
#
# # 인덱싱
# print(lunches[0],lunches[2],lunches[4])
#
# # 슬라이싱
# print(lunches[0:3],lunches[2],lunches[4])
#
# # 요소 변경
# lunches[2] = '뚝배기 불고기'
# print(lunches)
#
# # 추가하기 : append-맨뒤에추가, insert-원하는위치에추가
# lunches.append('짬뽕')
# print(lunches)
#
# lunches.insert(1,'떡볶이')
# print(lunches)
#
# # 삭제하기 : pop, remove, del, clear
# lunches.pop(3)
# print(lunches)
#
# lunches.pop()
# print(lunches)
#
# lunches.remove('김밥')
# print(lunches)
#
# lunches.clear()
# print(lunches)
#
# # 중첩 리스트 - 2차원 리스트
# persons = [
#     ['혜교','123-1234-1234','abc@abc.com'],
#     ['지현','456-4567-4567','aaa@aaa.com'],
#     ['동일','456-4567-4567','ccc@ccc.com'],
#     ['상일','456-4567-4567','aaa@ddd.com'],
#     ['지구','456-4567-4567','ddd@ccc.com'],
#     ['생각','456-4567-4567','aaa@aaa.com']
# ]
#
# print(persons)
# print(persons[0])
# print(persons[1])
# print(persons[0][0],persons[0][1])
# print(persons[1][0],persons[1][2])


# 반복문으로 persons 내용 출력
#
# for i in range(2):
#     for j in range(3):
#         print(persons[i],[j], end=' ')
#
#     print(persons)

# 항상된 for문 : for-each문으로 persons 내용출력

# for persons in persons:
#     print(persons)

# for persons in persons:
#     for info in persons:
#         print(info, end=' ')
#     print()

# for-each문 + 언팩킹 unpacking
# for name, phone, email in persons:
#     print(phone, email, name)

# 리스트 기타 함수
persons = [
    ['혜교','123-1234-1234','abc@abc.com'],
    ['지현','456-4567-4567','aaa@aaa.com'],
    ['동일','456-4567-4567','ccc@ccc.com'],
    ['상일','456-4567-4567','aaa@ddd.com'],
    ['지구','456-4567-4567','ddd@ccc.com'],
    ['생각','456-4567-4567','aaa@aaa.com']
]

persons1 = sorted(persons)  # 새 리스트 생성
print(persons1)

