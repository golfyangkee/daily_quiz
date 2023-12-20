def solution(num_list):
    num_list_sum=0
    num_list_gop=1
    for i in num_list:
        num_list_sum+=i
        num_list_gop*=i
        print(num_list_sum,num_list_gop)
    if num_list_gop<num_list_sum**2:
        return 1
    else:
        return 0