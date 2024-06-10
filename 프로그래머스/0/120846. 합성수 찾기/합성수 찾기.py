def solution(n):
    answer = []
    for com in range(1, n+1): # n 이하의 숫자 로
        com_copy = com  # n 이하의 숫자 원본 유지
        count = [] # 약수 개수 리스트 초기화
        for num in range(1, com+1): # 약수 구해보기
            if com_copy%num == 0:
                count.append(num)
        if len(count) >=3:
            answer.append(com)
    return len(answer)