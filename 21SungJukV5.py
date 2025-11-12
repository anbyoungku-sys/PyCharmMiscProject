# 성적 처리프로그램 V4
# 학생의 이름, 국어, 영어, 수학, 점수를 키보드로 입력 받아
# 총점, 평균, 학점을처리한 뒤 결과 출력
# 성적처리의 CRUD를 메뉴식으로 구현
# 성적데이터를 시퀀스 자료형에 저장

sungjuks = []

menus = f'''
---------------------
성적처리 프로그램 V4
---------------------
1. 성적데이터 입력
2. 성적데이터 조회
3. 성적데이터 상세조회
4. 성적데이터 수정
5. 성적데이터 삭제
0. 프로그램 종료
---------------------
작업을 선택하세요 : '''

header = f'''
 =========== 성적 결과 ===============
  이름   국어  영어  수학  총점  평균  학점
 -----------------------------------
'''
# menus = '''...'''
sungjuks = []
#for i in range(1,100+1):
while True:
    job = input(menus)

    # if job == '1': print('성적데이터 입력을 진행합니다.')
    # elif job == '2': print('성적데이터 조회를 진행합니다.')
    # elif job == '3': print('성적데이터 상세조회를 진행합니다.')
    # elif job == '4': print('성적데이터 수정을 진행합니다.')
    # elif job == '5': print('성적데이터 삭제를 진행합니다.')
    # elif job == '0':
    #     print('성적프로그램을 종료합니다.')
    #     break
    # else: print('번호를 잘못입력하셨습니다.')

    match job:
        case '1':
            name = input('이름을 입력해 주세요: ')
            kor = int(input('국어 점수를 입력해 주세요: '))
            eng = int(input('영어 점수를 입력해 주세요: '))
            mat = int(input('수학 점수를 입력해 주세요: '))

            tot = kor + eng + mat
            avg = tot / 3
            grd = ('A' if avg >= 90 else
                    'B' if avg >= 80 else
                    'C' if avg >= 70 else
                    'D' if avg >= 60 else 'F')

            sj = [name, kor, eng, mat, tot, avg, grd] # data 입력
            sungjuks.append(sj)

            print('성적데이터 입력을 진행합니다.')

            # result 문자열에 데이터 저장

        case '2':
            result = ''
            for name, kor, eng, mat, tot, avg, grd in sungjuks:
                result += (f'{name:5}{kor:4d}{eng:4d}{mat:4d}'
                          f'{tot:4d}{avg:4.1f}{grd:2}\n')

            print(f'{header} {result}')

        case '3': print('성적데이터 상세조회를 진합니다.')
        case '4': print('성적데이터 수정을 진행합니다.')
        case '5': print('성적데이터 삭제을 진행합니다.')
        case '0':
            print('성적프로그램을 종료합니다.')
            break
        case _: print('번호를 잘못입력하셨습니다.'
                      '다시 제대로 입력해 주세요: ')


