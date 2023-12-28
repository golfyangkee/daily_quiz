def solution(num_list, n):
    answer = []
    num_list_left=num_list[:n]
    num_list_right=num_list[n:]
    answer=num_list_right+num_list_left
    return answer