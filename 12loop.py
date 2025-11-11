# 반복문
# 정해진 횟수나 조건에 따라
# 특정 코드를 반복적으로 실행하도록 만든 문장

# 만일. Hello, World 출력

# # 1번 출력
# Print('Hello, World')
#
# # 3번 출력
# Print('Hello, World')
# Print('Hello, World')
# Print('Hello, World')

# 만일, 100번 출력한다면- 무한 복붙
# 단, 반복시 출력해야 하는 문구가 바뀌면? - 다시 수정 - 번거로움
# 효율적인 반복 실행을 위해 반복을 사용함!

# ex) 1~10까지 출력
# print(1, end=', ')
# print(2, end=', ')
# print(3, end=', ')
# print(4, end=', ')
# print(5, end=', ')
# print(6, end=', ')
# print(7, end=', ')
# print(8, end=', ')
# print(9, end=', ')
# print(10)

# for반복
# 정해진 횟수만큼 코드를 반복실행
# for 반복변수 in range(시작값, 종료값-1, 증감값):
#   반복실행할문장

# # range 함수 사용하기 : 정수 시퀸스 생성
# print(range(1, 10))
# print(list(range(1, 11))) # range 객체를 리스트로 변환
#
# # ex) 1~10까지 출력
# for i in range(1, 10+1):
#     print(i,end=', ')
# print() # end = '' 초기화용 코드
#
# # ex) Hello, World 5번 출력
# for i in range(1, 5+1):
#     print(i, 'Hello, World')

# ex) 3의 배수지만, 2의 배수가 아닌 정수 출력
# 누적합도 계산해서 출력
tot = 0

for i in range(3, 101, 3):
    print(i, end=', ')
    if i % 2 != 0:
        tot += i  # 조건에 맞는 숫자를 누적합에 더함
print()
print(tot)



# 무한 반복 함수 itertools, iter
i = 1
# 첫 번째 무한 반복 (내장 함수 iter 사용)
for _ in iter(int, 1):
    #if i == 9999999: break  # 주석 처리된 중단 조건
    print(i, end=' ')
    i += 1
print()

import itertools

# 두 번째 무한 반복 (itertools.count 사용)
for i in itertools.count():
    if i == 9999999: break
    print(i, end=' ')
print()
