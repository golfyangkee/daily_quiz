def solution(A, B):
    answer = 0
    if A==B:
        return 0
    for i in range(0, len(A)):
        a = A[-1]
        
        A = a + A[:-1]
        answer +=1
        print(A)
        if A == B:
            return answer
    return -1