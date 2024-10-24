def solution(participant, completion):
    p_d = {}
    c_d = {}
    for i in participant:
        if i in p_d:
            p_d[i] +=1
        else:
            p_d[i] =1
    for j in completion:
        if j in p_d:
            p_d[j] -= 1
    
    for k in p_d:
        if p_d[k] !=0:
            return k

'''
효율성 테스트에서 시간 초과로 실패한 것
def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    return participant[0]

이유 검색 결과
remove() 는 리스트에 끝까지 봐야 해서
in 도 끝까지 봐야해서 그렇다고 함
-----------------------

효율성 테스트 시간 초과로 실패한 것 2
def solution(participant, completion):
    p_d = {}
    c_d = {}
    for i in participant:
        p_d[i] = participant.count(i)
    for j in completion:
        c_d[j] = completion.count(j)
    for k in p_d:
        if k not in c_d:
            return k
        if p_d[k] != c_d[k]:
            return k
            
실패 이유: count 함수도 n 번을 시도 해야 해서
'''