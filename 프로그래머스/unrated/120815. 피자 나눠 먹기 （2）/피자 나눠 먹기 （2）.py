def solution(n):
    answer = 0
    # num 피자 개수
    # 6*num=n의 배수인 num이 가장 작은 수
    # num은 6*n을 넘을 수 없다.
    for num in range(1,6*n+1):
        if (6*num)%n==0:
            answer=num
            break
            
    # 다른 풀이
    # answer = 1
    # while 6 * answer % n:
    #     answer += 1
    return answer