def solution(num, k):
    answer = 0
    num_str=str(num)
    k_str=str(k)
    if k_str in num_str:
        answer=num_str.index(k_str)+1
    else:
        answer=-1
    return answer