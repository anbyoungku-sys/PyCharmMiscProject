# while
# 조건이 참일동아 반복을 실행하는 문장
# 주로 언제 끝날지 모르는 경우 반복에 사용

# while 조건 :
#   반복실행할문장
#
# for i in range(1, 5+1):
#     print(i, 'Hello, World')
#
# i = 1               # 초기화
# while i <= 5:       # 반복 조건식
#     print(i, 'Hello, World')
#     i += 1       # 증감식

# # ex) 3의 배수지만, 2의 배수가 아닌 정수 출력
# # 누적합도 계산해서 출력
# i = 1
# sum = 0
# while i <= 100:
#     if i % 3 == 0 and i % 2 != 0:
#         sum += i
#         print(i, end = ' ')
#     i += 1
#
# print(sum)

# i = 3
# sum = 0
# while i <= 100:
#     if i % 2 != 0:
#         sum += i
#         print(i, end = ' ')
#     i += 3
#
# print(sum)


# 만일, 조건식이 언제나 참이라면? - 무한루프
#
# i = 1
# sum = 0
# while True:
#     print(i, end = ' ')
#     i += 1

# for문은 유한한 반복을염두에 두고 설계
# 그래도, 무한루프를 만들고 싶다면 iter함수 사용

i = 1
for _ in iter(int, 1):
    if i == 99: break
    print(i, end='')
    i += 1
print()

import iterools

for i in iterools.count():
    if i ==99: break
    print(i, end='')

print()

