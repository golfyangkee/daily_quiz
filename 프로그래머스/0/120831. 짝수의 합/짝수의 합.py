def solution(n):
    answer1 = 0
    for i in range(1,n+1):
        if i%2==0:
            answer1 +=i
   
    # sum 함수로 풀기
    return sum([i for i in range(2,n+1, 2)])

    