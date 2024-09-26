def solution(number, limit, power):
    answer = 0
    
    # 약수를 구하는 방법은 제곱근을 활용하기
    for i in range(1,number+1):
        
        hap=0
        n = int(i**(0.5)) 
        # i의 제곱근에서 정수 부분만 추출 예를 들면 i가 4이면 n = 2인거고
        # i가 26 이면 n = 5 인거다.
        
        for j in range(1,n+1):
            if i%j==0:
                hap+=1 # 나눠지면 약수
                
                # 제곱근으로 나눴을 때 나눠지면서 몫이 제곱근과 다르면 +하고 
                # 제곱근과 같다면 4//2 이런 상황이니 + 안 한다.
                if j !=i//j: 
                    hap+=1
                    
        if hap > limit:
            answer+=power
        else:
            answer+=hap
    return answer
    
    ## 시간 초과 떠서 약수를 구하는 방법 변경
    # for i in range(1,number+1):
    #     hap=0 # 각 기사들의 약수의 개수를 세기 전 초기화
    #     for j in range(1,i+1): # 각 기사들의 약수 카운트해서 개수 세기
    #         if i%j==0:
    #             hap+=1
    #     if hap > limit:
    #         answer+=power
    #     else:
    #         answer+=hap
    # return answer

'''
다른 방법 찾아봄
제곱근을 while 문을 사용해서 진행 해봄
def solution(number, limit, power):
    answer = 0
    
    # 1부터 number까지의 숫자에 대해 약수 개수 구하기
    for i in range(1, number + 1):
        divisor_count = 0  # 각 숫자의 약수 개수를 저장
        
        # 1부터 i의 제곱근까지 반복하여 약수 개수 구하기
        j = 1
        while j * j <= i:  # 제곱근까지만 반복
            if i % j == 0:
                divisor_count += 1  # j는 약수
                if j != i // j:  # j와 i//j가 다른 경우에만 중복 방지
                    divisor_count += 1  # i//j도 약수
            j += 1
        
        # 약수 개수가 limit보다 크면 power를 더하고, 그렇지 않으면 약수 개수 더하기
        if divisor_count > limit:
            answer += power
        else:
            answer += divisor_count
    
    return answer
'''
