def solution(array):
    answer = []
    max_array=max(array)
    index_array=array.index(max_array)
    answer=[max_array,index_array]
    return answer