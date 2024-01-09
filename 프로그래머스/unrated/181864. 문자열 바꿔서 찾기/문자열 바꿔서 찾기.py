def solution(myString, pat):
    list1=''
    for i in range(len(myString)):
        if myString[i]=='A':
            list1+='B'
        elif myString[i]=='B':
            list1+='A'
    if pat in list1:
        return 1
    else:
        return 0