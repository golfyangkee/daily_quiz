def solution(array, height):
    # for 문 사용
    answer=0
    for i in array:
        if height < i:
            answer+=1
    return answer

    # 슬레이싱으로 찾아보기-> 같은 키이면 적용 못함
    # array.append(height)
    # array.sort()
    # num = array.index(height)
    # array = array[num+1:]
    # return len(array)
