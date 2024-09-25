def solution(name, yearning, photo):
    map = dict(zip(name,yearning))
    answer = []
    
    for p in photo:
        total=0
        for person in p:
            total+=map.get(person,0)
        answer.append(total)
    return answer

# def solution(name, yearning, photo):
#     # name과 yearning을 zip으로 묶어 딕셔너리로 만듦
#     score_map = dict(zip(name, yearning))
    
#     # 결과를 담을 리스트
#     answer = []
    
#     # 각 사진마다 추억 점수를 계산
#     for p in photo:
#         total_score = 0
#         for person in p:
#             # 해당 인물이 그리움 점수에 있으면 더하고, 없으면 0
#             total_score += score_map.get(person, 0)
#         answer.append(total_score)
    
#     return answer