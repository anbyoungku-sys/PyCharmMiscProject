import csv
import logging as log
import traceback as tb
from datetime import datetime

stu_no = 1   # CSV에서 불러오면 자동 갱신됨

# ========== 로깅 설정 ==========
log_filename = f"sungjuk_{datetime.now().strftime('%Y-%m-%d')}.log"
log.basicConfig(level=log.DEBUG, filename=log_filename, encoding='utf8',
                format='%(asctime)s - %(levelname)s - %(message)s')

menus = '''
-------------------
 성적처리 프로그램 V8
-------------------
1. 성적데이터 입력
2. 성적데이터 전체조회
3. 성적데이터 상세조회
4. 성적데이터 수정
5. 성적데이터 삭제
0. 프로그램 종료
-------------------
작업을 선택하세요 : '''

header1 = '''
번호  이름    국어    영어    수학
=============================
'''

header2 = '''
번호  이름   국어   영어   수학   총점   평균   학점
=============================================
'''

fname = 'sungjuk.csv'


# ===================== 점수 입력 =====================
def input_sungjuk():
    """
    사용자로부터 학생의 이름과 점수를 입력받아 원시 성적 데이터를 생성한다.

    Returns
    -------
    tuple
        (학생번호, 이름, 국어점수, 영어점수, 수학점수)
    """
    global stu_no
    name = input('이름을 입력하세요 : ')

    def get_score(subject):
        """
        특정 과목 점수를 입력받아 0~100 범위의 정수인지 검사하고 반환한다.

        Parameters
        ----------
        subject : str
            점수를 입력받을 과목명(국어, 영어, 수학)

        Returns
        -------
        int
            검증 완료된 과목 점수
        """
        while True:
            try:
                raw = input(f'{subject} 점수를 입력하세요 : ')
                score = int(raw)
                (0 <= score <= 100) or (_ for _ in ()).throw(ValueError("점수 범위 오류"))
                return score
            except Exception as ex:
                print(f'⚠ {subject} 점수는 0~100 정수만 가능합니다!')
                log.error(f'{subject} 입력 오류 → {ex}')
                log.error(''.join(tb.format_exception(type(ex), ex, ex.__traceback__)))

    kor = get_score("국어")
    eng = get_score("영어")
    mat = get_score("수학")

    no = stu_no
    stu_no += 1

    return no, name, kor, eng, mat


# ===================== 계산 =====================
def compute_sungjuk(no, name, kor, eng, mat):
    """
    총점, 평균, 학점을 계산하여 완전한 성적 데이터를 생성한다.

    Parameters
    ----------
    no : int
        학생 번호
    name : str
        학생 이름
    kor, eng, mat : int
        국어, 영어, 수학 점수

    Returns
    -------
    list
        [번호, 이름, 국어, 영어, 수학, 총점, 평균, 학점]
    """
    tot = kor + eng + mat
    avg = tot / 3
    grd = ('A' if avg >= 90 else
           'B' if avg >= 80 else
           'C' if avg >= 70 else
           'D' if avg >= 60 else 'F')

    return [no, name, kor, eng, mat, tot, avg, grd]


# ===================== 추가 =====================
def add_sungjuk(sj, sungjuks):
    """
    새로운 성적 데이터를 리스트에 추가한다.

    Parameters
    ----------
    sj : list
        성적 데이터 한 건
    sungjuks : list
        전체 성적 데이터 리스트
    """
    sungjuks.append(sj)
    log.info(f"새 성적 데이터 추가: {sj}")


# ===================== 전체조회 =====================
def readall_sungjuk(sungjuks):
    """
    모든 성적 데이터를 요약 형태로 출력한다.

    Parameters
    ----------
    sungjuks : list
        전체 성적 데이터 리스트
    """
    result = ''
    for no, name, kor, eng, mat, tot, avg, grd in sungjuks:
        result += f'{no:3d} {name:5s} {kor:4d} {eng:4d} {mat:4d}\n'

    print(f'{header1}{result}')
    log.info("전체 조회 실행")


# ===================== 상세조회 =====================
def readone_sungjuk(sungjuks):
    """
    특정 학생 번호로 상세 성적을 조회하고 출력한다.

    Parameters
    ----------
    sungjuks : list
        전체 성적 데이터 리스트
    """
    try:
        no = int(input('조회할 학생 번호는? : '))
        found = False

        for sj in sungjuks:
            if sj[0] == no:
                _, name, kor, eng, mat, tot, avg, grd = sj
                print(f'{header2}{no:3d} {name:5s} {kor:4d} {eng:4d} {mat:4d} {tot:4d} {avg:6.2f} {grd:4s}')
                found = True
                log.info(f"상세 조회 성공 → {no}")
                break

        if not found:
            raise LookupError("해당 번호 없음")

    except Exception as ex:
        print("⚠ 해당 학생번호를 찾을 수 없습니다!")
        log.error(f"상세 조회 오류: {ex}")
        log.error(''.join(tb.format_exception(type(ex), ex, ex.__traceback__)))


# ===================== 수정 =====================
def modify_sungjuk(sungjuks):
    """
    특정 학생 번호의 성적을 새로 입력받아 수정한다.

    Parameters
    ----------
    sungjuks : list
        전체 성적 데이터 리스트
    """
    try:
        no = int(input('수정할 학생 번호는? : '))
        found = False

        for i in range(len(sungjuks)):
            if sungjuks[i][0] == no:
                _, name, kor, eng, mat, _, _, _ = sungjuks[i]

                new_kor = int(input(f'새 국어점수 ({kor}) : '))
                new_eng = int(input(f'새 영어점수 ({eng}) : '))
                new_mat = int(input(f'새 수학점수 ({mat}) : '))

                sungjuks[i] = compute_sungjuk(no, name, new_kor, new_eng, new_mat)
                print("성적 수정 완료!")
                log.info(f"수정 완료 → {sungjuks[i]}")
                found = True
                break

        if not found:
            raise LookupError("수정 대상 없음")

    except Exception as ex:
        print("⚠ 성적 수정 중 오류 발생!")
        log.error(f"수정 오류 → {ex}")
        log.error(''.join(tb.format_exception(type(ex), ex, ex.__traceback__)))


# ===================== 삭제 =====================
def remove_sungjuk(sungjuks):
    """
    특정 학생 번호의 성적 데이터를 삭제한다.

    Parameters
    ----------
    sungjuks : list
        전체 성적 데이터 리스트
    """
    try:
        no = int(input('삭제할 학생 번호는? : '))
        found = False

        for i in range(len(sungjuks)):
            if sungjuks[i][0] == no:
                del sungjuks[i]
                print("성적 삭제 완료!")
                log.info(f"삭제 완료 → {no}")
                found = True
                break

        if not found:
            raise LookupError("삭제 대상 없음")

    except Exception as ex:
        print("⚠ 성적 삭제 중 오류 발생!")
        log.error(f"삭제 오류 → {ex}")
        log.error(''.join(tb.format_exception(type(ex), ex, ex.__traceback__)))


# ===================== CSV 읽기 =====================
def load_sungjuk():
    """
    CSV 파일에서 성적 데이터를 읽어 리스트로 반환한다.
    파일이 없으면 빈 리스트를 반환한다.

    Returns
    -------
    list
        CSV에서 읽어온 전체 성적 데이터
    """
    global stu_no
    sungjuks = []

    try:
        with open(fname, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for items in reader:
                no = int(items[0])
                name = items[1]
                kor = int(items[2])
                eng = int(items[3])
                mat = int(items[4])
                tot = int(items[5])
                avg = float(items[6])
                grd = items[7]
                sungjuks.append([no, name, kor, eng, mat, tot, avg, grd])

        # 새 학생번호 = 가장 큰 번호 + 1
        if sungjuks:
            stu_no = max(sj[0] for sj in sungjuks) + 1

        log.info("CSV 로드 완료")

    except FileNotFoundError:
        log.warning("CSV 파일 없음 → 새로 생성 예정")

    except Exception as ex:
        print("⚠ CSV 파일 로드 중 오류!")
        log.error(f"CSV 로드 오류: {ex}")
        log.error(''.join(tb.format_exception(type(ex), ex, ex.__traceback__)))

    return sungjuks


# ===================== CSV 저장 =====================
def write_sungjuk(sungjuks):
    """
    성적 데이터를 CSV 파일로 저장한다.

    Parameters
    ----------
    sungjuks : list
        전체 성적 데이터 리스트
    """
    try:
        with open(fname, "w", encoding="utf-8") as f:
            for sj in sungjuks:
                f.write(",".join(map(str, sj)) + "\n")

        log.info("CSV 저장 완료")

    except Exception as ex:
        print("⚠ CSV 저장 중 오류!")
        log.error(f"CSV 저장 오류 → {ex}")
        log.error(''.join(tb.format_exception(type(ex), ex, ex.__traceback__)))
