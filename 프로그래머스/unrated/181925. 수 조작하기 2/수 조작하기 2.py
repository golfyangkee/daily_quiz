def solution(numLog):
    answer = ''
    for i in range(1,len(numLog)):
        res=0
        res=numLog[i]-numLog[i-1]
        if res==1:
            answer+='w'
        elif res==-1:
            answer+='s'
        elif res==10:
            answer+='d'
        elif res==-10:
            answer+='a'
    return answer