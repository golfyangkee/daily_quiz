def solution(common):
    if len(common) == 2:
        common.append(2*common[1]-common[0])
    else:
        num = common[1]-common[0] # 2
        last = common[-1]
        if common[2]-common[1] == num:
            common.append(last+num)
        else:
            num = common[1]/common[0]
            first = common[0]
            n = len(common)
            common.append(first*(num**n))
    return common[-1]