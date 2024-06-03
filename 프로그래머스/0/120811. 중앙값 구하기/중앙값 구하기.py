def solution(array):
    array.sort() # 정렬
    num = len(array)//2 # 나누기 2의 몫 = 인덱스
    return array[num]