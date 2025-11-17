# 게시판 앱 V1
#
# ------------------------ 수 업 -------------------------
#
#
#
#
from anbyku.boardv1_lib import menus
from anbyku.boardv1_lib import input_board
from anbyku.boardv1_lib import write_board
from anbyku.boardv1_lib import list_board
from anbyku.boardv1_lib import view_board
from anbyku.boardv1_lib import modfy_board
from anbyku.boardv1_lib import remove_board

boards = []

while True:
    job = input(menus)

    match job:
        case '1':
            write_board(boards)

        case '2':
            list_board(boards)


        case '3':
            view_board(boards)

        case '4':
            modfy_board(boards)

        case '5':
            remove_board(boards)

        # case '0':
        # case _: print('잘못되었습니다.')
        #











































#
#
# #------------------------------------------------------------------
# # 메뉴
# menus1 = f'''
# ---------------------
# 게시판 프로그램
# ---------------------
# 1. 새글 입력
# 2. 글 목록
# 3. 본문 보기
# 4. 글 수정
# 5. 글 삭제
# 0. 종료
# ---------------------
# 필요하신 번호를 선택해 주세요 : '''
#
#
# menus2 = f'''
#  본문 글쓰기
# '''
#
#
# # 입력
# while True:
#     job = input(menus1)
#
#     board = []
#
#     match job: # 새글을 쓰시겠습니다.
#         case '1':
#             print(menus2)
#
#             views = 0
#
#             bno = int(input('번호 : '))
#             title = input('제 목 : ')
#             name = input('작성자 : ')
#             content = input('본 문 : ')
#
#
#             # 현재 시간을 자동 입력 (YYYY-MM-DD HH:MM:SS 형식)
#             reg_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#
#             # 입력 받은 본문 내용 저장: reg_date 필드 추가
#             temp = [bno, title, name, content, views, reg_date]
#             board.append(temp)
#
#                         # 입력 받은 본문 내용 저장
#             temp = [bno, title, name, content, views]
#             board.append(temp)
#
#             print("새로운 글이 저장되었습니다!\n")
#
#
#         # ★ 저장된 글을 바로 출력 ★
#             print("==== 저장된 글 ====")
#             print(f'''
#             글번호 : {bno}
#             제 목 : {title}
#             작성자 : {name}
#             본 문 : {content}
#             조회수 : {views}
#             작성일 : {reg_date}
#             ''')
#
#
#
# # 저장된 글을 목록으로 보기
#         case '2':
#             print("\n======= 글 목록 =======")
#
#             if not board:
#                 print("⚠ 저장된 글이 없습니다.\n")
#                 continue
#
#             # 글 목록 출력
#             for bno, title, name, content, views, reg_date in board:
#                 print(f"[{bno}] {title} | 작성자: {name} | 조회수: {views} | 작성일: {reg_date}")
#
#             print()
#
#         case '0':
#             print("게시판 프로그램을 종료합니다.")
#             break
#
#         case _:
#             print("⚠ 올바른 번호를 선택하세요!\n")
#
#
