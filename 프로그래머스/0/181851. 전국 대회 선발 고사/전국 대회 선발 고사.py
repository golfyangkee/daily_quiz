def solution(rank, attendance):
    n = len(rank)
    answer =0
    r_a = []

    for i in range(n):
        if attendance[i]:
            r_a.append([rank[i], i])
#    print(r_a) 	[[7, 1], [2, 2], [5, 3], [4, 4]]
    r_a.sort(key = lambda v : v[0])
# r_a를 정렬하는데, 이때 정렬 기준으로 각 요소의 첫 번째 원소(v[0])를 사용한다는 것을 의미
    return 10000 * r_a[0][1] + 100 * r_a[1][1] + r_a[2][1]
# arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])