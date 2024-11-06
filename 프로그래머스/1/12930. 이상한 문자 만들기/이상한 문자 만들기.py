def solution(s):
    result = s.split(' ')
    answer = ''
    for i in result:
        for j in range(len(i)):
            if j&1:
                answer+=i[j].lower()
            else:
                answer+=i[j].upper()
        answer+=' '
    return answer[:-1] # 마지막 띄어쓰기 뺄라고


'''
def solution(s):
    result= s.split(' ')
    list1=[]
    for i in result:
        answer=''
        for j in range(len(i)):
            if j%2==0:
                answer+=i[j].upper()
            else:
                answer+=i[j].lower()
        list1.append(answer)
               
    return ' '.join(i for i in list1)
'''