def solution(hp):
    a=5 # 장군개미 공격력
    b=3 # 병정개미 공격력
    c=1 # 일개미 공격력
    a_n=hp//a       # 장군개미 개수
    b_n=(hp%a)//b   # 병정개미 개수
    c_n=(hp%a)%b    # 일개미 개수
    answer = a_n+b_n+c_n
    return answer