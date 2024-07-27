def solution(arr, idx):
    result = arr[idx:]
    if 1 in result:
        answer = result.index(1) + idx
    else:
        answer = -1
    return answer