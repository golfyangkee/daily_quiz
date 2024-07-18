def solution(myStr):
    result = []
    current = []
    
    for char in myStr:
        if char in 'abc':
            if current:
                result.append(''.join(current))
                current = []
        else:
            current.append(char)

    if current:
        result.append(''.join(current))
    
    return result if result else ["EMPTY"]