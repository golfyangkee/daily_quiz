def solution(score):
    answer = []
    for i in score:
        # 점수 합
        answer.append((i[0]+i[1]))
    # 높은 순으로 정렬
    sort_hap = sorted(answer, reverse = True)
    # score의 인덱스랑 answer 인덱스는 같은 아이들
    # sort_hap 크기 순서
    rank = [sort_hap.index(i) + 1 for i in answer]
    # 인덱스가 같은 점수는 처음꺼가 나오니까 자동으로 4, 4, 6 이런식으로 나온다.
    return rank