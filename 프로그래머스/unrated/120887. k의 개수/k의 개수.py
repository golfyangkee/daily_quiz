def solution(i, j, k):
    answer=0
    for num in range(i,j+1):
        str_num=str(num)
        str_k=str(k)
        if str_k in str_num:
            print(str_num)
            answer += 1*str_num.count(str_k)
    return answer