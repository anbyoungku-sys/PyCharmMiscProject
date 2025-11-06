# 성적 처리프로그램 V3
# 3명의 학생에 대해
# 이름, 국어, 영어, 수학, 점수를 키보드로 입력 받아
# 총점, 평균, 학점을처리한 뒤 결과 출력

fir = '1번째 학생 정보 입력'
fir_name = input('이름을 입력해 주세요 : ')
fir_kor = int(input('국어 점수를 입력해 주세요 : '))
fir_eng = int(input('영어 점수를 입력해 주세요 : '))
fir_mas = int(input('수학 점수를 입력해 주세요 : '))

sec = '2번째 학생 정보 입력'
sec_name = input('이름을 입력해 주세요 : ')
sec_kor = int(input('국어 점수를 입력해 주세요 : '))
sec_eng = int(input('영어 점수를 입력해 주세요 : '))
sec_mas = int(input('수학 점수를 입력해 주세요 : '))

thd = '3번째 학생 정보 입력'
thd_name = input('이름을 입력해 주세요 : ')
thd_kor = int(input('국어 점수를 입력해 주세요 : '))
thd_eng = int(input('영어 점수를 입력해 주세요 : '))
thd_mas = int(input('수학 점수를 입력해 주세요 : '))

fir_tol = (fir_kor + fir_eng + fir_mas)
fir_evl = (fir_tol / 3)

fir_result = ('A' if (fir_evl >= 90) else 'B'
        if (fir_evl >= 80) else 'C'
        if (fir_evl >= 70) else 'D'
        if (fir_evl >= 60) else 'F')

sec_tol = (sec_kor + sec_eng + sec_mas)
sec_evl = (sec_tol / 3)

sec_result = ('A' if (sec_evl >= 90) else 'B'
        if (sec_evl >= 80) else 'C'
        if (sec_evl >= 70) else 'D'
        if (sec_evl >= 60) else 'F')

thd_tol = (thd_kor + thd_eng + thd_mas)
thd_evl = (thd_tol / 3)

thd_result = ('A' if (thd_evl >= 90) else 'B'
        if (thd_evl >= 80) else 'C'
        if (thd_evl >= 70) else 'D'
        if (thd_evl >= 60) else 'F')

pfmt = f'''
         ===== 성적 결과 =====
이름  국어 영어 수학 총점 평균 학점
----------------------------------
{fir_name} {fir_kor} {fir_eng} {fir_mas} {fir_tol} {fir_evl:.2f} {fir_result}
{sec_name} {sec_kor} {sec_eng} {sec_mas} {sec_tol} {sec_evl:.2f} {sec_result}
{thd_name} {thd_kor} {thd_eng} {thd_mas} {thd_tol} {thd_evl:.2f} {thd_result}
'''
print(pfmt)


pfmt = f'''
===== 성적 결과 =====
이름 : {fir_name},{sec_name},{thd_name}
국어 : {fir_kor},{sec_kor},{thd_kor}
영어 : {fir_eng},{sec_eng},{thd_eng}
수학 : {fir_mas},{sec_mas},{thd_mas}
총점 : {fir_tol},{sec_tol},{thd_tol}
평균 : {fir_evl:.2f},{sec_evl:.2f},{thd_evl:.2f}
학점 : {fir_result},{sec_result},{thd_result}
'''
print(pfmt)



