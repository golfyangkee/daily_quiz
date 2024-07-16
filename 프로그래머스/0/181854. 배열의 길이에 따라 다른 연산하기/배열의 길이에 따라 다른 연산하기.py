def solution(arr, n):
    answer = []
    num = len(arr)
    if num%2==0:
        for i in range(num):
            if i%2!=0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
    else:
        for i in range(num):
            if i%2==0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
    return answer