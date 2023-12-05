def solution(array, n):
    answer = 0
    list1=[]
    array.sort()
    print(array)
    for i in array:
        num=abs(n-i)
        list1.append(num)
        answer=array[list1.index(min(list1))]
    return answer