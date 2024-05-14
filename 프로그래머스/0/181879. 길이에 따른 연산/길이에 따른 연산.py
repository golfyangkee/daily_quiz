def solution(num_list):
    answer = 0
    time=1
    if len(num_list) >=11:
        return sum(i for i in num_list)
    else:
        for i in num_list:
            time*=i
        return time