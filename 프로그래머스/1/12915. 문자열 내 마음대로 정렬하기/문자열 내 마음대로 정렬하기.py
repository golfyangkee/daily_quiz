def solution(strings, n):
    answer = []
    answer = sorted(strings,key= lambda string: (string[n], string) )
    # lambda x: (x[n], x)
    # 첫번째는 x[n]으로 정렬하고 같으면 x자체로 비교해서 정렬하라
    return answer