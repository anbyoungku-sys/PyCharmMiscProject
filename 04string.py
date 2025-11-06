# 문자열 다루기

# 문자열  포매팅 1 - % 사용하기전
print('holle, world~!!')
print('holle, Python~!!')

say = 'world'
print('holle, ' + say + '~!!')
say = 'Python'
print('holle, ' + say + '~!!')

# 문자열  포매팅 1 - %
print('holle, %s~!!' % say)
name, weigt, age = '홍길도', 55.5, 35
print('이름 : %s, 몸무게 : %.1fkg, 나이 : %d' %(name, weigt, age))

# 문자열  포매팅 2 - .format
print('holle, {0}~!!' .format(say))
print('이름 : {0}, 몸무게 : {1:.2f}kg, 나이 : {2}' .format(name, weigt, age))

# 문자열  포매팅 3 - f포매팅 (3.6이상, 추천!)
print(f'holle, {say}~!!')
print(f'이름 : {name}, 몸무게 : {weigt:.2f}kg, 나이 : {age}')




# 문자열 비교 - 문자열 풀 pool
# 동일한 문자열 값을 한번만 저장하고 필요시 재사용하는 매커니즘
# 즉 같은 문자열을메모리에 여러번 생성하지 않음 - 메모리 절약

say1 = ' Hello, World!!'
say2 = ' Hello, World!!'
print(say1 == say2)
print(id(say1), id(say2))

say3 = ' Hello, World!!'
print(say1 == say3)
print(id(say1), id(say3))

say4 = say1[:] #슬라이싱을 통한 문자열 복사
#  say4 = "", [say1]
print(say1 == say4)
print(id(say1), id(say4))



# 시퀸스 자료형
# 값들이 순서대로 나열되어 있고
# 이 값을 인덱스(위치)로 접근할 수 있는 자료형
# 단, 위치는 0부터 차례대로 부여되어 있음
# 인덱싱, 슬라이싱, 순회 연산이 공통으로 제공
# 문자열, 리스트, 튜플

# 인덱싱indexing
# 시퀸스 안에 있는 개별 요소를 하나씩 꺼내는 방법
# 그 번호를 이용해서 요소에 접근 할 수 있음
# 변수명[인덱스]

str1 = ' Hello, World!!'
print(str1[0], str1[5], str1[10])
#print(str1[99]) # 인덱스 범위를 벗어남 - 오류는 없음
print(str1[5], str1[-5])

# 인덱스를 이용해서 요소 바꾸기
# 문자열 시퀸스는 불변 객체이기 때문에
# 한번 만들어지면, 개별 요소(내용)는 변경 불가
#str1[0] = 'A' # 수정불가 - 대입연산 불가

print('수정전 :', id(str1))
str1 = str1 + "and greeting"
print('수정후 :', id(str1))

# 문자열 슬라이싱slicing
# 시퀸스형 자료에서 구간을 잘라내는 연산
# 시퀸스[시작:끝-1:간격]
str1 = ' Hello, World!!'
print(str1[0], str1[1], str1[2], str1[3], str1[4], sep = '')
print(str1[0:5], str1[7:13], str1[7:15])
#     Hell         World      world!! 문자열만 출력
print(str1[:5], str1[7:13], str1[7:])

# ex) 주민번호를 이용해서 성별을 출력하는 코드
jumin = '123456-1234567'

#sex = jumin[:7]
result = '남자' if (jumin[7] == '1') else '여자'

print(jumin, result)

# 시퀸스 길이 연산
# len(시퀸스) - 요소의 갯수 출력
print(str1, len(str1))

