def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1] # 일치한 번호 개수에 따른 등수 리스트
    # rank[2]는 2개의 번호가 일치할 때 5등

    cnt_0 = lottos.count(0) # 0의 개수를 세어 저장 
    ans = 0 # 일치하는 당첨 번호의 개수 저장 변수
    for x in win_nums:
        if x in lottos:
            ans += 1 # 당천 번호 개수 카운트
            
    return rank[cnt_0 + ans],rank[ans]
    # 최고 순위: 0을 모두 맞는 번호로 가정한 경우
    # 최저 순위: 0을 모두 틀린 번호로 가정한 경우
'''
def solution(lottos, win_nums):
    # 1. 맞힌 숫자 개수 계산 (0을 제외하고 비교)
    matched = len(set(lottos) & set(win_nums))
    
    # 2. 알아볼 수 없는 숫자(0)의 개수 계산
    zero_count = lottos.count(0)
    
    # 3. 최고 순위와 최저 순위 계산
    max_matched = matched + zero_count  # 최고 순위: 모든 0이 맞는 경우
    min_matched = matched               # 최저 순위: 모든 0이 틀린 경우

    # 4. 일치한 개수에 따른 순위를 계산하는 함수
    def get_rank(count):
        if count >= 2:
            return 7 - count  # 2개 맞추면 5등, 3개면 4등, ..., 6개면 1등
        else:
            return 6  # 0개 또는 1개는 6등

    # 5. 최고 순위와 최저 순위 반환
    return [get_rank(max_matched), get_rank(min_matched)]
'''