def solution(M, N):
    answer = 0
    if M==1 and N==1:
        return answer
    else:
        answer=(M-1)+(N-1)*M
        return answer