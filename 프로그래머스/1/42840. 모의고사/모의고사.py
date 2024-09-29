def solution(answers):
    answer = [] # 리턴할 값들
    
    # 1~3번 수포자들의 정답 패턴 입력
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    
    # 1~3번 수포자들의 맞춘 개수 입력
    score = [0,0,0]
    
    # answers의 답과 비교해서 +1 시킴, elif 가 아니라 꼭 if 로 해야 한다.
    for i in range(len(answers)):
        if answers[i] == a1[i%len(a1)]:
            score[0] +=1
        if answers[i] == a2[i%len(a2)]:
            score[1]+=1
        if answers[i] == a3[i%len(a3)]:
            score[2]+=1
            
    # 1~3번 학생 중 많이 맞춘 학생의 번호가 먼저 나오게 해서 answer에 번호 추가
    max_score = max(score)
    
    answer= [i+1 for i,s in enumerate(score) if s == max_score]
  
    return answer