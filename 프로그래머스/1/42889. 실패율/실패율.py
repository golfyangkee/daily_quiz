def solution(N, stages):
    answer = []
    result = {}
    
    # 각 스테이지에서 도전한 사람 수를 계산
    for i in range(1, N+1):
        # i번 스테이지에 도전한 사람 수
        cnt = stages.count(i)
        
        # i번 스테이지에 도전한 사람 수와 실패율을 계산
        if len(stages) > 0:
            fail_rate = cnt / len(stages)
            result[i] = fail_rate
            # 도전한 사람 수에서 실패한 사람을 제외
            stages = [s for s in stages if s > i]

        else:
            result[i] = 0
    # 실패율을 기준으로 스테이지를 정렬 (내림차순 정렬 후 스테이지 번호로 정렬)
    answer = sorted(result, key=lambda x: result[x], reverse=True)
    
    return answer