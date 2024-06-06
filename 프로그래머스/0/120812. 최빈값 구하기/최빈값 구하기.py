def solution(array):
    test=list(set(array)) # 중복 숫자 제거
    answer={} # 요소 개수 저장할 튜플

    # 각각의 요소 개수 저장
    values=[]
    answer = {num:array.count(num) for num in test}
    for i in answer.values():
        values.append(i)
    
    # 최빈값의 개수
    max_num=max(values)
    
    # 최빈값의 값을 알기 위해
    if values.count(max_num) == 1:
        fre= [i for i, values in answer.items() if values==max_num]
        return int(''.join(map(str, fre)))
    else:
        return -1