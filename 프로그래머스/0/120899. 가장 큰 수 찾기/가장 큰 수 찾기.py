def solution(array):
    max_num=0
    for i in array:
        if max_num<=i:
            max_num=i
    max_index=array.index(max_num)
    answer = [max_num, max_index]
    return answer