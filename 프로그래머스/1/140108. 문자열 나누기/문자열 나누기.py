def solution(s):
    answer = 0  # 분할 개수
    i = 0  # 문자열을 탐색할 인덱스

    while i < len(s):
        # 현재 구간의 첫 번째 문자
        x = s[i]
        x_c = 1  # 첫 번째 문자와 같은 개수
        x_nc = 0  # 첫 번째 문자와 다른 개수

        # 현재 구간 탐색
        for j in range(i + 1, len(s)):
            if s[j] == x:
                x_c += 1
            else:
                x_nc += 1

            # 같은 개수일 때 분할
            if x_c == x_nc:
                i = j + 1  # 다음 탐색 시작점 갱신
                break
        else:
            # for문이 정상 종료되면 남은 문자열 끝까지 처리한 것
            i = len(s)

        answer += 1  # 분할 개수 증가

    return answer
'''
슬라이싱 사용하면 효율이 낮음
def solution(s):
    answer = 0 # 분할 개수
    
    while s: # s가 남아있을 때까지 실행
        
        # 변경되는 s에 마다 갱신해줘야 함
        x = s[0] # 첫번째 문자
        x_c = 1 # 첫번째 문자랑 맞는 횟수
        x_nc = 0 # 첫번째 문자랑 안 맞는 횟수
        
        for i in range(1, len(s)):
            
            if s[i]==x:
                x_c+=1
            else:
                x_nc+=1
            
            if x_c == x_nc: # 같으면 멈추기
                break            

        answer+=1 # 분할개수 갱신
        s = s[i+1:] # 분할
        
    return answer
'''