def solution(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    if len2 > len1:
        return -1
    elif len1 > len2:
        return 1
    else:
        sum1 = sum(arr1)
        sum2 = sum(arr2)
        if sum2 > sum1:
            return -1
        elif sum1 > sum2:
            return 1
        else:
            return 0
