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


# 문자열 슬라이싱

#






