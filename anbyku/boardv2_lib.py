counts = 1

menus = f'''
---------------------
  게시판 프로그램 V1
---------------------
1. 새글쓰기 
2. 게시글 목록
3. 게시글 본문보기
4. 게시글 수정
5. 글 삭제
0. 종료
---------------------
필요하신 번호를 선택해 주세요 : '''

header1 = '''
======== 게시글 목록 ===========
번호 | 제목 | 작성자 | 작성일 | 조회
------------------------------
'''

def input_board():
    global counts
    # '25'~'27' 줄은 주석 또는 한국어 설명으로, 코드에 포함하지 않았습니다.
    # 1개의 사용자 정의 신규
    # 전역변수 함수 내 수정
    counts += 1
    title = input('글제목 : ')
    userid = input('작성자 : ')
    contents = input('본문 : ')

    board = [counts, title, userid, contents, 0, '2025-11-14 17:47:35']

    return board


def write_board(boards):
    # '35' 줄은 주석 또는 한국어 설명으로, 코드에 포함하지 않았습니다.
    # 2개의 사용자 정의 신규
    board = input_board()
    boards.append(board)

    print('\n글이 등록되었습니다!')


def list_board(boards):
    # '41' 줄은 주석 또는 한국어 설명으로, 코드에 포함하지 않았습니다.
    # 2개의 사용자 정의 신규
    result = ''

    for bd in boards:
        result += f'{bd[0]} {bd[1]} {bd[2]} {bd[3][:10]} {bd[5]}\n'

    print(f'{header1}\n{result}')

def view_board(boards):
    bno = (input('조회할 글번호를입력하세요.'))
    result = '해당 게시물이 존재하지 않습니다.'

    for bd in boards:
        if bd[0] == bno:
            result = '\n======= 본문 내용 =======\n'
            result += f'글번호 : {bd[0]}\n'
            result += f'제목 : {bd[1]}\n'
            result += f'작성자 : {bd[2]}\n'
            result += f'조회수 : {bd[3]}\n'
            result += f'작성일 : {bd[5]}\n'
            result += f'본문 : {bd[4]}\n'

    print(result)

def modfy_board(boards):
    bno = (input('수정할 글번호를입력하세요.'))
    result = '해당 게시물이 존재하지 않습니다.'

    for bd in boards:
        if bd[0] == bno:
            new_title = input(f'새 제목 ({bd[1]}) : ()')
            new_contents = input(f'새 제목 ({bd[3]}) : ()')
            bd[1] = new_title
            bd[3] = new_contents
            result = '🥳해당 게시물을 삭제했습니다.'

            print(result)

    print(result)


def remove_board(boards):
    bno = (input('삭제할 글번호를입력하세요.'))
    result = '해당 게시물이 존재하지 않습니다.'

    for bd in boards:
        if bd[0] == bno:
            boards.remove(bd)
            result = '🥳해당 게시물을 삭제했습니다.'

    print(result)

