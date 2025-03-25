def solution(board):
    n = len(board)
    danger_zone = [[0] * n for _ in range(n)]  # 위험지역 표시용

    # 8방향 (상, 하, 좌, 우, 대각선)
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰 발견
                danger_zone[i][j] = 1  # 지뢰 위치도 위험지역
                for d in range(8):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < n and 0 <= nj < n:
                        danger_zone[ni][nj] = 1  # 주변도 위험지역

    # 위험지역이 아닌 곳 세기
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if danger_zone[i][j] == 0:
                safe_count += 1

    return safe_count