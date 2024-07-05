def solution(arr):
    answer = 1
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=arr[j][i]:
                answer=0
    return answer

    # return int(arr == list(map(list, zip(*arr))))
    # 해석
    # * 연산자는 arr의 요소를 풀어줍니다. [5, 192, 33] [192, 72, 95] [33, 95, 999]
    # zip(*arr)는 2차원 배열 arr을 전치 행렬로 변환합니다. 이는 각 행(row)에서 동일한 인덱스에 있는 요소들을 결합하여 새로운 튜플을 만듭니다.
    # zip(*arr)로 생성된 튜플들을 map 함수와 list 함수를 사용하여 리스트로 변환
    # list(map(list, zip(*arr)))는 이러한 리스트들을 하나의 리스트로 묶어줍니다. 즉, 전치된 행렬을 리스트 형태로 반환합니다.
    # int() True는 1, False는 0으로 변환