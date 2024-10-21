def solution(s, skip, index):
    answer = ''
    
    
    # 알파벳 기본셋 설정
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    # 알파벳 기본셋에서 skip 문자 제거
    alpha = ''.join([char for char in alpha if char not in skip])

    for i in s:
        num = alpha.index(i)+index
        if num >= len(alpha): 
            # 같은 거도 고려해야 한다. 
            # 인덱스니까 길이가 같으면 0번째 인덱스로 인식 시켜야 한다.
            num %= len(alpha)
        answer+= alpha[num]
    
    return answer