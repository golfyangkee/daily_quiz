def solution(a, d, included):
    answer = 0
    # 등차수열 = [a,a+d,a+d*2,a+d*3,,,]
    i_cnt=len(included)
    list1=[]
    for i in range(i_cnt):
        list1.append(a+d*i)
    for i in range(i_cnt):
        if included[i]==True:
            answer+=list1[i]
    return answer