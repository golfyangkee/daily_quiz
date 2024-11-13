def solution(number):
    answer = 0
    num = len(number)
    for i in range(num):
        for j in range(i, num):
            for k in range(j, num):
                if number[i]+number[j]+number[k]==0 and i!=j!=k:
                    answer+=1
    return answer

# def solution(number):
#     answer = 0
#     n =len(number)
#     result=0
#     for i in range(n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 answer= number[i]+number[j]+number[k]
#                 if answer==0:
#                     result+=1
#     return result