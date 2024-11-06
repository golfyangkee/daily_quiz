def solution(d, budget):
    #  오름차순으로 나열 한 후 
    # 남은 금액이 현재 금액보다 크면 주는 형식을 통해 최대한 많은 부서에 지원해 줄 수 있다.
    answer=0
    d.sort()
    for i in d:
        if i<=budget:
            answer+=1
            budget-=i
    return answer

'''
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget - i >=0:
            answer+=1
            budget-=i
    return answer
'''