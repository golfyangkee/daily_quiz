def solution(num_list):
    odd_hap = 0
    even_hap = 0
    for i in range(len(num_list)):
        if i%2==0:
            odd_hap += num_list[i]
        else:
            even_hap += num_list[i]
    return max(odd_hap, even_hap)