def solution(n):
    answer = 0
    for i in range(2,n+1): # 1과 자기자신 외가 생기면 소수가 아니다.
        result=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                result=False
                break # 이거 안 넣으면 너무 오래 걸림
        if result:
            answer+=1
    return answer