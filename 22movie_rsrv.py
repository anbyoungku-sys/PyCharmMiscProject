# 여화관 좌석 예약 실습 문제
# 5행 5열 (총 25석) 영화관 좌석이 있습니다. 각 좌석은 처음에 모두 빈 자리('O')로 표시됩니다.
# 사용자는 좌석 행 과 열을 입력하여 좌석을 예약할 수 있습니다.
# 예약된 좌석은 'X'로 표시되며, 이미 예약된 좌석은 예약은 불가 메시지를 출력합니다.

# 기본 요구 사항
# 1. 좌석 초기화 - 5X5 2차원 리스트 생성, 모든 좌석 'O'
# 2. 예약 기능
#   사용자로부터 행(A~E)과 열(1~5) 입력 받기
#   이미 예약된 좌석이면 "이미 예약된 좌석입니다." 출력
#   정상 예약 시 'X'로 표시
# 3. 좌석 배치 출력
#   현재 예약 상태를 2차원 좌석표 형태로 출력
#   열번호는 위쪽, 행 번호는 좌측
# 4. 반복 예약
#   "q" 입력 시 프로그램 종료

# 영화관 좌석 예약 프로그램 (시퀀스 자료형 활용)

# 좌석 초기화 (리스트 시퀀스로 5행 5열 만들기)

#------------------- 수 업 -------------------
# 좌석 초기화
# seats = [['O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O']]

seats = []

for i in range(5):
    row = []
    for j in range(5):
        row.append('O')
    seats.append(row)

# 좌석 현황 출력 후
result = '   1  2  3  4  5\n'
for j in range(5):
    result += f'{chr(65+j):3s}'
    for i in range(5):
        result += f'{seats[j][i]:3s}'
    result += '\n'
print(result)



# 예약 여부 입력 받음
rsrv_row = input('좌석을 예약하시겠어요? 행(A~E): ').upper()
rsrv_col = input('좌석을 예약하시겠어요? 열(1~5): ')


# 좌성 예약 처리
posx = ord(rsrv_row) - 65
posy = int(rsrv_col) - 1
seats[posx][posy] = 'X'

# 예약 완료
result = '   1  2  3  4  5\n'
for j in range(5):
    result += f'{chr(65+j):3s}'
    for i in range(5):
        result += f'{seats[j][i]:3s}'
    result += '\n'
print(f'\n{result}')

# 처리 완료 메세지 출력
print(f'{rsrv_row}{rsrv_col} 좌석이 예약되었습니다.')

















#----------------내가 만들어봄-----------------
# seats = [
#     ['O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O']
# ]  # 2차원 리스트 시퀀스
#
# rows = ['A', 'B', 'C', 'D', 'E']  # 행 이름 시퀀스
#
# while True:
#     # 화면 출력부 ------------------------------
#     print("\n- 영화관 좌석 예약 -")
#     print("   1  2  3  4  5")
#     for i, row_label in enumerate(rows):
#         print(f"{row_label} ", end=" ")
#         for seat in seats[i]:
#             print(seat, end="  ")
#         print()
#
#     # 사용자 입력부 ----------------------------
#     row = input("\n예약할 좌석의 행(A~E, 종료:q): ").upper()
#     if row == 'Q':
#         print("예약을 종료합니다.")
#         break
#
#     col = input("예약할 좌석의 열(1~5): ")
#
#     # 입력값 검증 ------------------------------
#     if row not in rows or not col.isdigit() or not (1 <= int(col) <= 5):
#         msg = "잘못된 입력입니다. 다시 시도해주세요."
#     else:
#         r = rows.index(row)
#         c = int(col) - 1
#
#         # 좌석 예약 처리 ----------------------
#         if seats[r][c] == 'X':
#             msg = f"좌석 {row}{col}은 이미 예약되어 있습니다. 다른 좌석을 선택하세요."
#         else:
#             seats[r][c] = 'X'
#             msg = f"좌석 {row}{col} 예약이 완료되었습니다!"
#     # ----------------------------------------
#
#     # 결과 출력 (모든 print를 여기에 모음)
#     print(msg)





















# 좌석 초기 화면
# header = f'''
# - 영화관 좌석 예약 -
#   1  2  3  4  5
# A O  O  O  O  O
# B O  O  O  O  O
# C O  O  O  O  O
# D O  O  O  O  O
# E O  O  O  O  O
# '''
# print(header)   # 좌석 초기 보시
#
# seats = [
#     [O, O, O, O, O]
#     [O, O, O, O, O]
#     [O, O, O, O, O]
#     [O, O, O, O, O]
#     [O, O, O, O, O]
# ]
#
# # 입력 예시
# row = input('몇 번 좌성을 예약하기겠어요? 행(A~E) 입력 :  ').upper()
# col = input('몇 번 좌성을 예약하기겠어요? 행(1~5) 입력 :  ')
#
# # 좌석 예약 안내
# print('좌석 -', row,col,'- 예약완료') # 예약 완료 표시







