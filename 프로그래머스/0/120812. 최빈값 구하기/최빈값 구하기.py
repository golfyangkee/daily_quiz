def solution(array):
    answer = 0
    my_list=list(set(array))
    cnt=[]
    for i in my_list:
        cnt.append(array.count(i))
    a=max(cnt)
    b=cnt.index(a)
    cnt.remove(a)
    print(cnt)
    if a in cnt:
        return -1
    else:
        return my_list[b]