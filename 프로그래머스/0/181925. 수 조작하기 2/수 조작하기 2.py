def solution(numLog):
    answer = ''
    dict1 = {1:'w', -1:'s', 10:'d', -10:'a'}
    
    for i in range(1, len(numLog)):
        result = numLog[i]-numLog[i-1]
        answer+=dict1[result]
    return answer