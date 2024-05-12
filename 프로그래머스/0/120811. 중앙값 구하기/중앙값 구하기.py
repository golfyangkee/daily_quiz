def solution(array):
    answer = 0
    array.sort()
    num=len(array)//2
    answer=array[num]
    return answer