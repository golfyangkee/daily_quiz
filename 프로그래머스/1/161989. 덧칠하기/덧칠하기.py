def solution(n, m, section):
    # 페인트칠 횟수
    count = 0
    # 마지막으로 페인트칠한 구역의 끝 번호
    last_painted = 0
    
    for s in section:
        # 현재 구역이 마지막으로 칠한 구역 범위 밖에 있다면
        if s > last_painted:
            # 새로운 롤러로 칠함
            count += 1
            # 이번 롤러로 칠한 구역의 끝 범위를 갱신 (s부터 s + m - 1까지 칠함)
            last_painted = s + m - 1
            
    return count