# 성적 처리프로그램 V3b
# 3명의 학생에 대해
# 이름, 국어, 영어, 수학, 점수를 키보드로 입력 받아
# 총점, 평균, 학점을처리한 뒤 결과 출력
# 반복문 사용해서 코드 깔끔하게 작성함
result = ''

for i in range(1, 3+1):
    # 입력
    name = input(f'{i}) 이름을 입력해 주세요 : ')
    kor = int(input(f'{i}) 국어 점수를 입력해 주세요 : '))
    eng = int(input(f'{i}) 영어 점수를 입력해 주세요 : '))
    mat = int(input(f'{i}) 수학 점수를 입력해 주세요 : '))
    tot = 0
    avg = 0.0
    grd = '가'

    # 성적처리
    tot = kor + eng + mat
    evg = tot / 3

    grd = ('A' if (evg >= 90) else 'B'
    if (evg >= 80) else 'C'
    if (evg >= 70) else 'D'
    if (evg >= 60) else 'F')

    result += (f'[name:{name:5}][kor:{kor:4d}][eng:{eng:4d}][mat:{mat:4d}]'
               f'[tot:{tot:4d}][evg:{evg:4.1f}][grd:{grd:4}]\n')

print(result)


