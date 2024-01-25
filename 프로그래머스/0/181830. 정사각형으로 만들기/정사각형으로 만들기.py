def solution(arr):
    a=len(arr)
    b=len(arr[0])
    c=a-b
    if c>0:
        for i in range(a):
            for j in range(c):
                arr[i].append(0)
    elif c<0:
        for i in range(-c):
            arr.append([0]*b)
    return arr
