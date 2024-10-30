# 내가 처음으로 푼 것
def solution(n, lost, reserve):
    answer = 0
    r = {}
    
    # 체육복 현황
    for i in range(1,n+1):
        r[i]=1 # 일단 다 하나씩 가지고 있다 가정
        if i in reserve:
            r[i]+=1 # 여벌 있으면 +
        if i in lost:
            r[i]-=1 # lost에 번호 있으면 -
            
    # 체육복 빌려주기
    for i in range(1, n + 1):
        if r[i] == 0:  # 체육복이 없는 학생이라면
            # 앞 번호 학생이 체육복이 2개인 경우
            if i - 1 >= 1 and r[i - 1] == 2:
                r[i - 1] -= 1
                r[i] += 1
            # 뒷 번호 학생이 체육복이 2개인 경우
            elif i + 1 <= n and r[i + 1] == 2:
                r[i + 1] -= 1
                r[i] += 1
                
    # 체육복이 1개 이상인 학생 수 세기
    answer = sum(1 for i in r if r[i] >= 1)
    return answer