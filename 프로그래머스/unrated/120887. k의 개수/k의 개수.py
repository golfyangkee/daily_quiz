def solution(i, j, k):
    answer=0
    for num in range(i,j+1):
        str_num=str(num)
        str_k=str(k)
        if str_k in str_num:
            print(str_num)
            answer += 1*str_num.count(str_k)
            
    # 다른풀이1
    # return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))
    
    # 다른풀이2
    # answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer