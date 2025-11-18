# 성적 처리프로그램 V6용 모듈

import csv

menus = f'''
-------------------
 성적처리 프로그램 V7
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

def input_sungjuk():
    """
    성적 데이터를 입력받는 함수

    :return:
    """

    name = input(f'이름을 입력하세요 : ')
    kor = int(input(f'국어 점수를 입력하세요 : '))
    eng = int(input(f'영어 점수를 입력하세요 : '))
    mat = int(input(f'수학 점수를 입력하세요 : '))

    return name, kor, eng, mat


def compute_sungjuk(name, kor, eng, mat):
    """
    성적 데이터에 대한 총점,평균,학점 처리

    :return:
    """
    tot = kor + eng + mat
    avg = tot / 3
    grd = ('A' if (avg >= 90) else
           'B' if (avg >= 80) else
           'C' if (avg >= 70) else
           'D' if (avg >= 60) else 'F')

    return [name, kor, eng, mat, tot, avg, grd]


def add_sungjuk(sj, sungjuks):
    """
    처리한 성적데이터를 리스트에 추가

    :return:
    """
    sungjuks.append(sj)


def readall_sungjuk(sungjuks):
    """
    저장된 성적데이터 중 이름/국어/영어/수학만 출력

    :param sungjuks:
    :return:
    """
    result = ''
    for name, kor, eng, mat, tot, avg, grd in sungjuks:
        result += f'{name:5s} {kor:4d} {eng:4d} {mat:4d}\n'

    print(f'{header1}{result}')


def readone_sungjuk(sungjuks):
    """
    이름으로 성적데이터를 조회해서 모두 출력

    :param sungjuks:
    :return:
    """
    result = ''

    namekey = input('조회할 학생 이름은?: ')

    for name, kor, eng, mat, tot, avg, grd in sungjuks:
        if namekey == name:
            result += f'{name:5s} {kor:4d} {eng:4d} {mat:4d} ' \
                   f'{tot:4d} {avg:4.2f} {grd:4s}\n'

    print(f'{header2}{result}')


def modify_sungjuk(sungjuks):
    """
    기존 성적데이터를 새로운 성적데이터로 수정하는 함수

    :param sungjuks:
    :return:
    """

    result = '해당 학생이 존재하지 않아요!!'
    namekey = input('수정할 학생 이름은?: ')

    # 수정할 학생이 존재하는지 확인
    # sungjuks[i]는 개별 성적데이터 위치를 가리키는 포인터pointer
    # sungjuks[i] = sjone 라는 코드를 이용해서
    # compute_sungjuk함수에 의해 새롭게 생성된 sj객체로 완전히 교체함
    # 즉, sungjuks[i]는 특정 학생의 성적데이터를 가리키는 인덱스
    # sungjuks[i][j]는 특정 학생 성적데이터의 특정요소를 가리키는 인덱스
    for i in range(len(sungjuks)):
        if namekey == sungjuks[i][0]:
            kor = int(input(f'새로운 국어점수는? ({sungjuks[i][1]}): '))
            eng = int(input(f'새로운 영어점수는? ({sungjuks[i][2]}): '))
            mat = int(input(f'새로운 수학점수는? ({sungjuks[i][3]}): '))

            sjone = compute_sungjuk(sungjuks[i][0], kor, eng, mat)
            sungjuks[i] = sjone

            result = '성적 수정이 완료되었습니다!!'
            break

    print(result)


def remove_sungjuk(sungjuks):
    """
    특정 학생의 성적데이터를 삭제하는 함수

    :param sungjuks:
    :return:
    """

    result = '해당 학생이 존재하지 않아요!!'
    namekey = input('삭제할 학생 이름은?: ')

    for i in range(len(sungjuks)):
        if namekey == sungjuks[i][0]:
            sungjuks.pop(i)
            result = '성적 데이터가 삭제되었습니다!!'
            break

    print(result)


def load_sungjuk():
    """ sungjuk.csv파일의 내용을 읽어서 리스트 변수에 저장 """
    sungjuks = []
    with open(fname, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for items in reader:
            sj = [items[0],items[1],items[2],items[3],
                  items[4],items[5],items[6]]
            sungjuks.append(sj)
    return sungjuks


def write_sungjuk(sungjuks):
    with open(fname, 'w', encoding='utf-8') as f:
        for sj in sungjuks:
            row = (f'{sj[0]},{sj[1]},{sj[2]},{sj[3]},'
                   f'{sj[4]},{sj[5]},{sj[6]}\n')
            f.write(row)

