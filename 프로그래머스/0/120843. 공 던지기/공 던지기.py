def solution(numbers, k):
    num = len(numbers)//2
    test =[]
    if num <k:
        for i in range(0,k-num):
            test.extend(numbers)
    else:
          test = numbers  
    answer = test[::2]
    return answer[k-1]