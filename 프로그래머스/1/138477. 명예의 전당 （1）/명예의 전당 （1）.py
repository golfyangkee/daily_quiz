def solution(k, score):
    hall_of_fame = []  # 명예의 전당 리스트
    result = []  # 매일 발표되는 최하위 점수를 저장할 리스트
    
    for s in score:
        # 새로운 점수를 명예의 전당 리스트에 추가
        hall_of_fame.append(s)
        
        # 명예의 전당에는 최대 k개의 점수만 유지
        if len(hall_of_fame) > k:
            hall_of_fame.remove(min(hall_of_fame))
        
        # 매일 명예의 전당의 최하위 점수를 기록
        result.append(min(hall_of_fame))
    
    return result