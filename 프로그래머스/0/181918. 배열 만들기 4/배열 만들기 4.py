def solution(arr):
    stk = []
    i=0
    while i<len(arr):
        if len(stk)==0:
            stk.append(arr[i])
            i+=1
        elif arr[i]>stk[-1]:
            stk.append(arr[i])
            i+=1
        elif arr[i]<=stk[-1]:
            del stk[-1]
    return stk