def greeting(married, salary):
    match married:
        case 'n':  # 미혼
            rate = 10 if salary <= 3000 else 25
        case 'y':  # 기혼
            rate = 10 if salary <= 6000 else 25
        case _:    # 잘못된 입력
            print('입력 오류! Y 또는 N을 입력해 주세요.')
            return None
    return rate