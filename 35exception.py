# 예외exception#
# 프로그램이 실행되는 도중에 예상치 못한 문제가 발생해서
# 정상적인 흐름이 깨지는 상황
# 즉, 프로그램이 하려던 일을 갑자기 제대로 할 수 없을때 발생하는 사건

# print('프로그램 시작1!')
# print(int(input('숫자를 하나 입력하세요!(1) ')))
# print('프로그램 끝1!')
#
# print('프로그램 시작2!')
# print(int(input('숫자를 하나 입력하세요!(2) '))) # 숫자 대신 문자를 입력하면?
# print('프로그램 끝2!')


# 예외처리
# 프로그램에서 오류가 발생하다라도 비정상인 종료없이
# 안정적으로 흐름을 유지하고, 문제를 올바르게 처리하도록 하는 것
# 프로그램의 비정상 종료 방지
# 오류 상황에 대한 적절한 대응 제공
# 오류 원인 파악 로깅 용이-문제해결, 디버깅 수월
# 파이썬에서는 try-excetr구문으로 예외처리 구현

# print('프로그램 시작3!')
# try:
#     print(int(input('숫자를 하나 입력하세요!(3) '))) # 숫자 대신 문자를 입력하면?
# except:
#     print()
# print('프로그램 끝3!')


# print('프로그램 시작4!')
# try:
#     num = int(input('숫자를 하나 입력하세요!'))
#     print(f'입력 숫자:{num}') # 숫자 대신 문자를 입력하면?
# except:
#     print('숫자만')
# print('프로그램 끝4!')

# print('프로그램 시작5!')
# try:
#     with open('abc123.xyz', 'r') as f:
#         data = f.read()
#     print(data)
# except:
#     print('파일을 찾을 수 없습니다!!!')
# print(data)
# print('프로그램 끝5!')


# 여러예외처리
# 하나의 try 블록 내에서 발생할 수 있는 다양한 종류의 예외를
# 적절히 구분해 처리하는 방법
# 1) 하나의 except에서 여러 예외를 묶어 처리
# 2) 여러 except블록으로 나눠 각각 처리
# 3) 하나의 except에서 여러 예외를 묶어 처리
# 1) try-except블록 처리

# print('프로그램 시작6!')
# try:
#     x = int(input('숫자를 입력 : '))
#     result = 10 / x
#     print(f'결과 : {result}')
# except:
#     print('오류 발생!!!')
# print('프로그램 끝6!')


# print('프로그램 시작6!')
# try:
#     x = int(input('숫자를 입력 : '))
#     result = 10 / x
#     print(f'결과 : {result}')
# except ValueError:
#     print('숫자만 입력!!!')
# except ZeroDivisionError:
#     print('0으로 나눌수 없습니다!!!')
# print('프로그램 끝6!')

# 예외처리를 위한 에러 종류
# 입력: ValueError, TypeError, NameError
# 인덱스 : IndexError, KeyError
# 계산 : ZeroDivisionError, OverflowError
# 파일 : FileNotFoundError, IOError
# 임포트 : ImportError

# 애외 발생시 로그 확인하기
# Exception : 파이썬에서 모든 예외의 기본이 되는 최상의 클래스
# 프로그램 실행 중에 발생하는 오류를 표현하는 Error 객체의 부무
# 파이썬에서 발생하는 대부분의 오류가 상속받는 기본 예외 클래스
import sys
import traceback as tb

try:
    10 / 0
except Exception as ex:
    print(f'오류! - {ex}')    # 오류 메시지
    print(f'Error! - {type(ex)}')    # Error 객체 종류
    err, val, trace = sys.exc_info()
    # tb.print_tb(trace)
    # 리스트에 저장된 각각의 내용을 ' '로 합쳐서  exmsg 변수에 저장
    exmsg = ' '.join(tb.format_exception(err, val, trace))
    print(exmsg)









