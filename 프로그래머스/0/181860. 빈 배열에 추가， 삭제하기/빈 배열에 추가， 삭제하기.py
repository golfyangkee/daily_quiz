def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i] == True:
            num = arr[i]
            a = num*2
            for i in range(a):
                answer.append(num)
        else:
            if len(answer) !=0:
                for i in range(arr[i]):
                    answer.pop()
    return answer