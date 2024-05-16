def solution(num_list):
    answer = 0
    sum_even = sum(num_list[1::2])
    sum_odd = sum(num_list[::2])
    answer= max(sum_even, sum_odd)
    return answer