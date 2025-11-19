# 로깅logging
# 프로그램 실행 중 발생하는 이벤트, 상태, 오류 정보를 기록하는 것
# print()와 달리, 프로그램의 동작 기록을
# 파일이나, 콘솔등 원하는 곳에 체계적으로 남기는 기능
# 디버깅, 운영/모니터링, 감사 및 기록
# 파이썬에서는 내장 모듈인 logging 사용

import logging as log
import traceback as tb

# 로깅 설정
# level : 기록할 로드의 최소 수준 - critical > error > warning > info > debug
# filename : 로그에 기로할 파일
# format : 로그 메시지 형식()
log.basicConfig(level=log.DEBUG, filename='36logging.log', encoding='utf8',
                format= '%(asctime)s - %(levelname)s - %(message)s')

# 상황별 오깅 메세지 출력
# log.debug('디버그용 메시지')
# log.info('정보 메시지')
# log.warning('경고 메시지')
# log.error('오류 메시지')
# log.critical('치명적 오류')


# 예외 처리 로직
print('프로그램 시작6b!')

try:
    x = int(input('숫자를 하나 입력하세요 : '))
    result = 10 / x
    print(f'결과 : {result}')
except Exception as ex:
    print('오류가 발생했습니다!! 자세한 내용은 로그파일을 확인하세요!')

    log.error(f'예외 상황 발생!: {ex}')
    tbmsg = ' '.join(tb.format_exception(type(ex), ex, ex.__traceback__))
    log.error(f'스택트레이스!: {tbmsg}')
    # 아래 빈 줄은 코드의 일부는 아니지만, 이미지에 포함되어 있어 그대로 둡니다.

print('프로그램 끝6b!')