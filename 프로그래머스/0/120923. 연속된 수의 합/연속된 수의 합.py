def solution(num, total):
    answer = []
    if total%num == 0:
        m = total/num
        a = (num-1)/2
        for i in range(0, num):
            answer.append(m-a+i)
    else:
        m = total//num # 3
        a = num//2 # 2
        for i in range(1, num+1):
            answer.append(m-a+i)
    return answer