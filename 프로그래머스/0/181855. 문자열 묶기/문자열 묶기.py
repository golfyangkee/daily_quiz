def solution(strArr):
    answer = 0
    result=[]
    for i in strArr: # 각 원소들의 길이를 result 리스트에 넣음
        result.append(len(i))
    
    c_r = {} # 딕트 써서 key value로 만듦
    for i in result:
        if i in c_r:
            c_r[i]+=1
        else:
            c_r[i]=1
    
    list1 = []
    list1 = list(c_r.values())
    list1.sort()
    return list1[-1]