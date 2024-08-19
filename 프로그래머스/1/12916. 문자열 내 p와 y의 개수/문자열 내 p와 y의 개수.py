def solution(s):
    s_list = list(s)
    answer = True
    p_num = s_list.count('p')
    P_num = s_list.count('P')
    y_num = s_list.count('y')
    Y_num = s_list.count('Y')

    if p_num+P_num != y_num+Y_num:
        return False
    return True