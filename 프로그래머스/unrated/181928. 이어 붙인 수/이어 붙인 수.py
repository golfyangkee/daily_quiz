def solution(num_list):
    answer = 0
    num_even=''
    num_odd=''
    for i in num_list:
        if i%2==0:
            num_even+=str(i)
        else:
            num_odd+=str(i)
    num_even_int=int(num_even)
    num_odd_int=int(num_odd)
    answer=num_even_int+num_odd_int
    return answer