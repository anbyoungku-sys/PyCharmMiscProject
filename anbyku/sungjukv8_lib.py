# 성적 처리프로그램 V8용 모듈

import csv
import logging as log

counts = 0  # 학생번호 부여용 변수

menus = f'''
-------------------
 성적처리 프로그램 V8
-------------------
1. 성적데이터 입력
2. 성적데이터 조회
3. 성적데이터 상세조회
4. 성적데이터 수정
5. 성적데이터 삭제
0. 프로그램 종료
-------------------
작업을 선택하세요 : '''

header1 = '''
이름    국어    영어    수학
========================
'''

header2 = '''
이름   국어   영어   수학   총점   평균   학점
========================================
'''

fname = 'sungjuk.csv'


def sungjuk_logging():
    """
    로깅 환경을 초기 설정한다.

    로그 파일(sungjukv8.log)을 생성하거나 기존 파일에 이어서 기록하며,
    INFO 레벨 이상의 로그를 기록하도록 설정한다.
    모든 로그 메시지는 UTF-8로 저장되며, 다음 정보를 포함한다:

    - 로그 발생 시각
    - 로그 레벨(INFO, ERROR 등)
    - 메시지 내용

    이 함수는 반드시 프로그램 시작 시 가장 먼저 호출되어야 한다.
    """

    log.basicConfig(
        filename='sungjukv8.log',
        level=log.INFO, encoding='utf-8',
        format='%(asctime)s %(levelname)s --- %(message)s'
    )


def input_sungjuk():
    """
    사용자에게 학생의 이름, 국어, 영어, 수학 점수를 입력받는다.

    입력된 데이터는 계산 전의 '원본 성적 데이터'이며,
    점수 입력이 숫자가 아니거나 오류가 발생할 경우 기본값(0)으로 대체된다.

    Returns
    -------
    tuple
        (name, kor, eng, mat)
        - name (str): 학생 이름
        - kor (int): 국어 점수
        - eng (int): 영어 점수
        - mat (int): 수학 점수

    Notes
    -----
    - 점수는 정수 형태로 입력받는다.
    - 잘못된 입력이 들어오면 오류 메시지를 출력하고 0점 처리된다.
    """

    log.info('input_sungjuk 호출됨!')
    try:
        name = input(f'이름을 입력하세요 : ')
        kor = int(input(f'국어 점수를 입력하세요 : '))
        eng = int(input(f'영어 점수를 입력하세요 : '))
        mat = int(input(f'수학 점수를 입력하세요 : '))
    except ValueError:
        print('점수는 숫자만 입력가능합니다!!')
        log.error('점수는 숫자만 입력가능합니다!!')
        name, kor, eng, mat = '0', 0, 0, 0

    return name, kor, eng, mat


def compute_sungjuk(name, kor, eng, mat):
    """
    입력받은 성적 데이터를 바탕으로 총점, 평균, 학점을 계산한다.

    Parameters
    ----------
    name : str
        학생 이름
    kor : int
        국어 점수
    eng : int
        영어 점수
    mat : int
        수학 점수

    Returns
    -------
    list
        [name, kor, eng, mat, tot, avg, grd] 형태의 리스트
        - name (str): 학생 이름
        - kor, eng, mat (int): 개별 점수
        - tot (int): 총점
        - avg (float): 평균
        - grd (str): 학점(A, B, C, D, F)

    Notes
    -----
    학점 기준
    - 90 이상: A     - 80 이상: B     - 70 이상: C     - 60 이상: D
    - 그 외: F
    """

    tot = kor + eng + mat
    avg = tot / 3
    grd = ('A' if (avg >= 90) else
           'B' if (avg >= 80) else
           'C' if (avg >= 70) else
           'D' if (avg >= 60) else 'F')

    log.info('compute_sungjuk 호출됨!')
    return [name, kor, eng, mat, tot, avg, grd]


def add_sungjuk(sj, sungjuks):
     """
    계산된 성적 데이터를 전체 성적 리스트에 추가한다.

    첫 번째 요소로 '학생 번호(counts)'를 자동 부여하며,
    내부적으로 counts 값을 1 증가시켜 다음 학생 번호가 중복되지 않도록 한다.

    Parameters
    ----------
    sj : list
        compute_sungjuk()에서 생성된 성적 데이터 리스트
    sungjuks : list
        전체 성적 리스트

    Returns
    -------
    None
    """

    global counts
    counts += 1
    sj.insert(0, counts)

    sungjuks.append(sj)
    log.info('add_sungjuk 호출됨!!')


def readall_sungjuk(sungjuks):
    """
    전체 학생 성적 데이터를 요약하여 출력한다.

    출력되는 항목은 다음과 같다:
    - 학생번호     - 이름     - 국어 점수     - 영어 점수     - 수학 점수

    Parameters
    ----------
    sungjuks : list
        전체 학생 성적 리스트

    Returns
    -------
    None

    Notes
    -----
    상세 정보(총점, 평균, 학점)는 출력되지 않는다.
    """

    result = ''
    for sj in sungjuks:
        result += f'{sj[0]:3d} {sj[1]:5s} {sj[2]:4d} {sj[3]:4d} {sj[4]:4d}\n'

    print(f'{header1}{result}')
    log.info('readall_sungjuk 호출됨!')


def readone_sungjuk(sungjuks):
     """
    특정 학생 번호로 성적 데이터 한 건을 상세 조회한다.

    상세 조회 시 출력 항목은 다음과 같다:
    - 학생번호    - 이름    - 국어 / 영어 / 수학 점수    - 총점    - 평균    - 학점

    Parameters
    ----------
    sungjuks : list
        전체 성적 데이터 리스트

    Returns
    -------
    None
    Raises
    ------
    ValueError
        학생 번호 입력 시 숫자가 아닌 경우 발생
    """

    result = ''

    try:
        sjno = int(input('조회할 학생 번호는?: '))

        for sj in sungjuks:
            if sjno == sj[0]:
                result += f'{sj[0]:3d} {sj[1]:5s} {sj[2]:4d} {sj[3]:4d} {sj[4]:4d} ' \
                          f'{sj[5]:4d} {sj[6]:4.2f} {sj[7]:4s}\n'

        print(f'{header2}{result}')
        log.info('readone_sungjuk 호출됨!')
    except ValueError as ex:
        print('성적 상세 조회시 숫자만 입력하세요!!')
        log.error(f'readone_sungjuk 오류발생! {type(ex)}')


def modify_sungjuk(sungjuks):
     """
    특정 학생의 성적 정보를 새로운 점수로 수정한다.

    사용자가 입력한 학생번호가 리스트에 존재하면 기존 데이터가 삭제되고
    동일한 학생번호를 유지한 상태로 새 성적 데이터가 다시 저장된다.

    Parameters
    ----------
    sungjuks : list
        성적 데이터 전체 리스트

    Returns
    -------
    None

    Raises
    ------
    ValueError
        점수 또는 학생번호 입력이 정수가 아닌 경우 발생

    Notes
    -----
    - 기존 데이터는 삭제 후 새 데이터로 대체된다.
    - 입력하지 않은 요소는 기존 값이 유지되지 않는다.
    """

    result = '해당 학생번호가 존재하지 않아요!!'

    try:
        sjno = int(input('수정할 학생 번호는? '))

        for i in range(len(sungjuks)):
            if sjno == sungjuks[i][0]:
                kor = int(input(f'새로운 국어점수는? ({sungjuks[i][2]}): '))
                eng = int(input(f'새로운 영어점수는? ({sungjuks[i][3]}): '))
                mat = int(input(f'새로운 수학점수는? ({sungjuks[i][4]}): '))

                sjone = compute_sungjuk(sungjuks[i][1], kor, eng, mat)
                sjone.insert(0, sjno)
                sungjuks[i] = sjone

                result = '성적 수정이 완료되었습니다!!'
                break

        print(result)
        log.info('modify_sungjuk 호출됨!')
    except ValueError as ex:
        print('성적 수정시 숫자만 입력하세요!!')
        log.error(f'modify_sungjuk 오류발생! {type(ex)}')


def remove_sungjuk(sungjuks):
     """
    특정 학생 번호를 기준으로 성적 데이터를 삭제한다.

    Parameters
    ----------
    sungjuks : list
        전체 학생 성적 리스트

    Returns
    -------
    None

    Raises
    ------
    ValueError
        학생번호 입력 시 정수가 아닌 경우
    """

    result = '해당 학생번호가 존재하지 않아요!!'

    try:
        sjno = int(input('삭제할 학생 번호는? '))

        for i in range(len(sungjuks)):
            if sjno == sungjuks[i][0]:
                sungjuks.pop(i)
                result = '성적 데이터가 삭제되었습니다!!'
                break

        print(result)
        log.info('remove_sungjuk 호출됨!')
    except ValueError as ex:
        print('성적 삭제시 숫자만 입력하세요!!')
        log.error(f'remove_sungjuk 오류발생! {type(ex)}')


def load_sungjuk():
    """
    sungjuk.csv파일의 내용을 읽어서 리스트 변수에 저장
    CSV 파일(sungjuk.csv)에서 성적 데이터를 읽어 리스트 형태로 반환한다.

    파일이 존재하면 각 행의 데이터를 읽어 자료형에 맞게 변환 후 sungjuks 리스트에 저장한다.
    파일이 없으면 빈 리스트를 반환하며, 오류 로그를 남긴다.

    Returns
    -------
    list
        CSV에서 읽어온 전체 성적 데이터 리스트
        각 요소는 다음 형태를 가진다:
        [번호(int), 이름(str), 국어(int), 영어(int), 수학(int),
         총점(int), 평균(float), 학점(str)]

    Notes
    -----
    - counts 전역 변수는 CSV 파일 내 가장 마지막 학생 번호로 자동 동기화된다.
    """

    sungjuks = []
    global counts

    log.info('load_sungjuk 호출됨!')
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for items in reader:
                # print(f'items의 항목수 : {len(items)}\n')
                # 문자열로 저장된 성적데이터를 원래 자료형식에 맞게 변환작업 추가
                counts = int(items[0])  # counts변수를 최근 학생번호로 설정 (동기화)
                sj = [int(items[0]), items[1], int(items[2]), int(items[3]), int(items[4]),
                      int(items[5]), float(items[6]), items[7]]
                sungjuks.append(sj)
            log.info('성적 데이터가 성공적으로 초기화되었습니다!!')
    except FileNotFoundError as ex:
        # print('sungjuk.csv 파일이 존재하지 않아요!!')
        log.error('sungjuk.csv 파일이 존재하지 않아요!!')

    return sungjuks


def write_sungjuk(sungjuks):
    """
    전체 성적 데이터를 CSV 파일(sungjuk.csv)에 저장한다.

    Parameters
    ----------
    sungjuks : list
        저장할 전체 성적 데이터 리스트

    Returns
    -------
    None

    Raises
    ------
    Exception
        파일 저장 중 오류 발생 시 예외 처리

    Notes
    -----
    - 기존 파일은 새 데이터로 덮어쓴다.
    """
    try:
        with open(fname, 'w', encoding='utf-8') as f:
            for sj in sungjuks:
                row = (f'{sj[0]},{sj[1]},{sj[2]},{sj[3]},'
                       f'{sj[4]},{sj[5]},{sj[6]},{sj[7]}\n')
                f.write(row)
        log.info('write_sungjuk 호출됨!!')
    except Exception as ex:
        print('성적 데이터 저장시 오류 발생!! - 관리자에게 문의하세요!')
        log.error(f'write_sungjuk에서 오류발생!! {type(ex)}')
