def solution(answers):
    # 수포자들의 답 패턴
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 수포자별로 맞춘 문제 수를 기록할 리스트
    scores = [0, 0, 0]
    
    # 정답과 패턴을 비교하여 맞춘 문제 수 계산
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            scores[2] += 1
    
    # 가장 높은 점수를 찾고, 그 점수와 같은 사람을 모두 찾아 반환
    max_score = max(scores)
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]
    
    return result