# 도화지 크기 정의
paper_size = 100
# 도화지를 0으로 초기화 (100x100)
canvas = [[0] * paper_size for _ in range(paper_size)]

# 색종이 수 입력
n = int(input())

# 색종이 붙이기
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):  # 가로 10칸
        for j in range(y, y + 10):  # 세로 10칸
            canvas[i][j] = 1  # 색종이가 붙은 영역을 1로 표시

# 색칠된 면적 계산
area = sum(row.count(1) for row in canvas)
print(area)