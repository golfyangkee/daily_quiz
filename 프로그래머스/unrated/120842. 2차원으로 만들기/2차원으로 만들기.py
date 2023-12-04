def solution(num_list, n):
    res = []
    for i in range(0, len(num_list), n):
        temp = []
        for j in range(0, n):
            temp.append(num_list[i])
            i = i + 1
        res.append(temp)
    return res