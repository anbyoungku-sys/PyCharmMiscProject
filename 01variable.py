# 데이터 : 정보를 나타내는 값
# 사람이나 컴퓨터가 처리 할 수 있는 숫자, 문자 등 모든 형태의 정보가 데이터
# 컴퓨터가 기억하고 처리할 수 있는 값

# 변수 : 데이터를 저장하기 위해 이름을 부여한 상자
# 어떠한 값을 저장하는 장소를 기억하기 쉽게 문자 형태로 나타낸 것
# 변수에 값이 저장되는 공간을 메모리라 함
# 변수에 값을 넣으라고 선언하면 시스템상의 메모리 어딘가에 공간을 확보하고
# 그 공간의 실제 주소와 이름을 매핑(연결)함

# 이름과 나이를 저장하는 변수 선언
name = '홍길동'
age = 99

# 변수에 저장된 값을 출력하려면 print 함수 사용
print(name, age)

# 파이썬의 자료형
# 정적 타입 : 변수 선언시 자료형도 같이 선언
# String name = "홍길동"
# name = 99 (X)

# 동적 타입 : 변수 선언시 자료형은 생략, 추론 기능으로 자동 할당
#           또한, 변수에 대입하는 값에 따라 자료형이 바뀜
# name = '홍길동'
# name = '99'

# 변수의 자료형을 알아보려면 type 함수 사용
print(type(name), type(age))

name = 120
age = '철수와 영희'
print(name, age)
print(type(name), type(age))

# 회원정보 저장용 변수
# 아이디, 비밀번호, 이름, 나이, 이메일,
# 결혼여부, 보유금액, 가입일

user_id = 'abc'
password = '1234'
name = '안병구'
age = 50
email = 'anbyku@gmail.com'
is_married = False
balance = 100000
join_date = '25.11.04'

print(user_id, password, name, age, email, is_married, balance, join_date)
print(type(user_id),type(password), type(name), type(age), type(email), type(is_married), type(balance),  type(join_date))

# 변수의 자료형 - 정수, 실수, 문자, 불
# 정수형 - 소수점 이하의 값이 없는 수
# 실수형 - 소수점 이하의 값이 있는 수
# 문자 - 글자, 단어, 문장 같은 텍스트 데이터를 의미
# 불 - 참/거짓으로 표현 가능한 값

