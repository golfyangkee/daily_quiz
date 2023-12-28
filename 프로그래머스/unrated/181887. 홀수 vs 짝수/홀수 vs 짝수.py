def solution(num_list):
    answer = 0
    odd_sum=0
    even_sum=0
    for i in num_list[::2]:
        odd_sum+=i
    for i in num_list[1::2]:
        even_sum+=i
    answer=max(odd_sum,even_sum)
    return answer