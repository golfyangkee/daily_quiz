def solution(arr):
    stk = []
    num = len(arr)
    i=0
    while i<num:
        if stk == []:
            stk.append(arr[i])
            i +=1
        elif stk[-1]<arr[i]:
            stk.append(arr[i])
            i+=1
        elif stk[-1] >= arr[i]:
            stk = stk[:-1]
    return stk