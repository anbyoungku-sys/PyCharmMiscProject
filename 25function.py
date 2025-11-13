# 프로그램
# 어떤 일을 수행하도록 명령이나 절차를 정리해 놓은것-명령어들의 모음
# 입력 -> 처리 -> 출력의 과정이 정의된 명령 집합
# 일반적인개념 : 어떤 목표를 달성하기 위해 단게별로 계획을 세운 것

#함수
# 수학에서의 함수 : 입력값을 넣으면 결과값이 나오는 규칙
# f(x) = x + 3, x = 3 =>6
# 특정 작업을 수행하는 독립적인 코드 집합(블록)
# 재사용 : 한 번 정의해 놓으면 여러 곳에서 사용 가능
# 구조화 : 복잡한 프로그램을 작은 코드 단위로 나눠 관리 할 수 있음

# 매개변수 parameter
# 함수가 외부에서 값으 전달 받을때 사용할 변수
# 함수 호출시 값을 받을 자리를 의미
# 기본 매개변수

# 인수/인자 argument
# 함수 호출시 실제로 전달하는 값
# 즉, 매개변수에 전달되는 실제 데이터

# 반환값
# 함수가 실행되고 결과로 돌려주는 값
# return 라는 키워드를 이용해서 반환값을
# 함수를 호출한 곳으로 전달함
# 단, 파이썬에서는 여러개의 값을 반환값으로 전달할 수 있음

# 함수 정의 1
# def 함수이름 ():
#     함수 문장들

# 간단한 인사말 1
print("hello world")

# 간단한 인사말 2
def say_hello():
    print("hello world")

# 함수 호출
# 함수이름()
say_hello()

# 간단한 인사말 3
# 함수이름(매개변수)
#   함수 문장들
def say_hello2(msg):
    print(f'hello {msg}')

# 함수이름(인수)
say_hello2('World')
say_hello2('python')
say_hello2('java')
say_hello2('MariaDB')

# 반환값이 있는 함수
# def 함수이름 ():
#   함수 문장들
#   return 반환값

# 간단한 인사말 4
def say_hello3(msg):
    result = f'hello {msg}'
    return result

msg = say_hello3('World')
print(msg)


























