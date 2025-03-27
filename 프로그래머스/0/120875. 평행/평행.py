def solution(dots):
    def is_parallel(a, b, c, d):
        # 기울기 비교: (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1)
        return (b[1] - a[1]) * (d[0] - c[0]) == (d[1] - c[1]) * (b[0] - a[0])

    # 경우 1: dots[0]-dots[1] vs dots[2]-dots[3]
    if is_parallel(dots[0], dots[1], dots[2], dots[3]):
        return 1
    # 경우 2: dots[0]-dots[2] vs dots[1]-dots[3]
    if is_parallel(dots[0], dots[2], dots[1], dots[3]):
        return 1
    # 경우 3: dots[0]-dots[3] vs dots[1]-dots[2]
    if is_parallel(dots[0], dots[3], dots[1], dots[2]):
        return 1

    return 0