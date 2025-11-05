            # 성적 처리프로그램 V1
            # 이름, 국어, 영어, 수학, 점수를 변수로 설정하고
            # 총점, 평균, 학점을처리한 뒤 결과 출력
            # 단, 학점은 삼항연산자를 이용해서 계산한다.
            # 변수 = 참일때 값 if 조건식 else 거짓일때 값

            # 입력
            # 이름, 국어, 영어, 수학, 점수를 변수로 설정

            # 성적 처리
            # 총점, 평균, 학점을처리한 뒤 결과 출력

            # 결과 처리
            # 이름, 국어, 영어, 수학, 점수, 평균, 학점 출력

# 입력
name = '김민수'
kor = 99
eng = 99
mas = 98
tol = 0
evl = 0.0
result = 0.0

# 성적처리
tol = (kor + eng + mas)
evl = (tol / 3)

result = ('A' if (evl >= 90) else 'B'
        if (evl >= 80) else 'C'
        if (evl >= 70) else 'D'
        if (evl >= 60) else 'F')

# result = 'A' if (evl >= 90) else 'B'
# result = 'A' if (evl >= 90) else 'B'
# result = 'A' if (evl >= 90) else 'B'

# 결과처리
print('===== 성적 결과 =====')
print(f'이름 : {name}')
print(f'국어 : {kor}')
print(f'수학 : {eng}')
print(f'총점 : {tol}')
print(f'평균 : {evl:.2f}')
print(f'학점 : {result}')












