# 성적 처리프로그램 V6
# 학생의 이름, 국어, 영어, 수학, 점수를 키보드로 입력 받아
# 총점, 평균, 학점을처리한 뒤 결과 출력
# 성적처리의 CRUD를 메뉴식으로 구현
# 성적데이터를 시퀀스 자료형에 저장
# 성적처리 CRUD 기능을 함수로 구조화


from anbyku.sungjukV6_lib import menus
from anbyku.sungjukV6_lib import header1
from anbyku.sungjukV6_lib import header2
from anbyku.sungjukV6_lib import input_sungjuk, compute_sungjuk, add_sungjuk
from anbyku.sungjukV6_lib import readall_sungjuk
from anbyku.sungjukV6_lib import readone_sungjuk
from anbyku.sungjukV6_lib import modify_sungjuk
from anbyku.sungjukV6_lib import remove_sungjuk

sungjuks = []

#for i in range(1,100+1):
while True:
    job = input(menus)

    match job:
        case '1':
            name, kor, eng, mat = input_sungjuk()
            sj = compute_sungjuk(name, kor, eng, mat)
            add_sungjuk(sj, sungjuks)

        case '2':
            readall_sungjuk(sungjuks)

        case '3':
            readone_sungjuk(sungjuks)

        case '4':
            modify_sungjuk(sungjuks)

        case '5':
            remove_sungjuk(sungjuks)

        case '0':
            print('성적프로그램을 종료합니다.')
            break
        case _: print('번호를 잘못입력하셨습니다.'
                      '다시 제대로 입력해 주세요: ')


