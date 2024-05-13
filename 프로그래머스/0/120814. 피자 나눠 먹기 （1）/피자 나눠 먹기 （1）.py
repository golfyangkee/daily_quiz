def solution(n):
    # 판 수
    answer = n//7
    if n%7:
        answer+=1
    return answer