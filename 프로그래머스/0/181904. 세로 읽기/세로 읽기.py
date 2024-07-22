def solution(my_string, m, c):
    # 내가 푼 것
    answer = ''
    result = []
    for i in range(len(my_string)//m): # 짜른 문자 result 리스트에 저장
        result.append(my_string[m*i:m*i+m])
        
    for r in result: # 리스트 원소들 하나씩 빼서 c번째 answer에 넣기
        answer += r[c-1] # 배열로 보면 -1 해줘야 해당 번째니까
    return answer

    # retrun my_string[c-1::m]