def solution(N, stages):
    answer = [] # 단 제출
    result= {} # 딕셔너리로 값을 정리하려고 한다.
    
    # 1부터 N까지 각 단계에 대한 실패율을 계산해야 하니 다 봐야 한다.
    # 해당 작업을 통해 stages의 숫자들이 뒤죽박죽이여도 1단계부터 차례대로 정리된다.
    for i in range(1,N+1):
        
        cnt = stages.count(i) # 리스트의 각 요소의 개수를 센다. 
        
        if len(stages) > 0: # stages 안의 요소를 줄일거라 0이 되면 끝내려고
            
            result[i]=cnt/len(stages) # 각 실패율을 담는다.
            
            stages = [s for s in stages if s > i] 
            # 무조건 x/N이 아니라 그 단계를 성공한 사람은 제외해야 하니까 
            # 2번 스테이지의 경우 [2,1,2,2] 즉 4명 중이니까 계산에 사용하고
            # 그 이후 단계들로만 계산하게끔 stages 를 변경한다.
            
        else:
            # 남은 stages 가 없으면 
            # 해당 stage를 못 넘은 사람이 없으니까 계산할 필요도 없이 0ㅇ로 처리한다.
            result[i] = 0
    
    answer = sorted(result, key= lambda x : result[x],reverse=True)
    # lambda 함수에 대해 잠깐 설명하면
    # key는 정렬 기준을 말하는건데
    # result의 x(keys)의 값 즉 values들의 값에 따라 x를 리턴하라는 말이다.
    return answer