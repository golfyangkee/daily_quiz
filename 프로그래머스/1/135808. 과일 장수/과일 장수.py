def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    
    for i in range(0,len(score), m):
        if len(score[i:i+m])==m: # 남은 과일의 수가 m개인 경우에만 박스 만듦
            answer+=min(score[i:i+m])*m
            # answer+=score[i]하면 최대 점수가 아니라 최소 점수로 만들어지니까
    return answer

'''
def solution(k, m, score):
    score.sort(reverse=True)  # 점수를 내림차순으로 정렬 (높은 점수부터 상자를 채우기 위해)
    
    total_score = 0
    
    # score 리스트에서 m개씩 그룹으로 묶고, 각 그룹의 최저점수 * m을 더해줍니다.
    for i in range(0, len(score), m):
        if len(score[i:i+m]) == m:  # 남은 과일이 m개인 경우에만 상자를 만들 수 있음
            total_score += min(score[i:i+m]) * m  # 각 그룹의 최소 점수 * m
    
    return total_score
'''