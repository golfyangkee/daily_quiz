def solution(date1, date2):
    result = date1 < date2
    # print(result) # False
    if result:
        return 1
    else:
        return 0
    
    
    
    
    # answer = 0
    # if date1[0] < date2[0]:
    #     answer = 1
    # elif date1[0] == date2[0] & date1[1] < date2[1]:
    #     answer = 1
    # elif (date1[0] == date2[0]) & (date1[1] == date2[1]) & (date1[2] < date2[2]):
    #     answer = 1
    # return answer

    ## 전체수로 비교할 게 아니라 1000 이랑 0이랑 먼저 비교하고 순서대로 해야한다.
    # 실패
    # answer =0
    # date1_str =''
    # date2_str = ''
    # for i in range(3):
    #     date1_str += str(date1[i])
    #     date2_str += str(date2[i])
    # print(date1_str, date2_str)
    # if date1_str < date2_str:
    #     answer = 1
    # return answer