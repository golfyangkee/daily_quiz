def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(num in ['0', '5'] for num in str(i)):
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)
    return answer
# all() 함수 이용 안에 내용으 참이면 True 반환