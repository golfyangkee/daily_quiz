def solution(arr1, arr2):
    arr1_num=len(arr1)
    arr2_num=len(arr2)
    arr1_sum=0
    arr2_sum=0
    for i in arr1:
        arr1_sum+=i
    for i in arr2:
        arr2_sum+=i
    if arr1_num>arr2_num:
        return 1
    elif arr1_num<arr2_num:
        return -1
    else:
        if arr1_sum>arr2_sum:
            return 1
        elif arr1_sum<arr2_sum:
            return -1
        else:
            return 0