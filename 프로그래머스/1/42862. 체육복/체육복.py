'''
# 이해해보기
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost] # 체육복 개수 2개인 학생
    _lost = [l for l in lost if l not in reserve] # 체육복 개수 0개인 학생
    for r in _reserve: # 즉 2개 여유분 있는 친구들
        # 앞 뒤 숫자 구하기
        f = r - 1
        b = r + 1
        # 잃어버렸더라도 앞 뒤가 친구가 여유가 있으니까 잃어버린게 아니다.
        if f in _lost: # 로스트에 f가 있으면
            _lost.remove(f) # 로스트에서 f 없애기
        elif b in _lost: # 로스트에 b가 있으면 
            _lost.remove(b) # 로스트에서 b 없애기
    return n - len(_lost) # 진짜로 앞 뒤로도 구할 수 없는 친구들의 수를 뺀다.
'''
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