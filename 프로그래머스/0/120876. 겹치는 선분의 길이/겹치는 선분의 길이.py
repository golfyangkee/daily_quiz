def solution(lines):
    arr = [0] * 201  # -100 ~ 100을 인덱스 0 ~ 200으로 대응

    for line in lines:
        start, end = line
        for i in range(start, end):  # 끝 점은 포함하지 않음
            arr[i + 100] += 1  # +100으로 인덱스 보정

    # 겹치는 구간(2개 이상인 구간)의 개수 세기
    return sum(1 for x in arr if x >= 2)