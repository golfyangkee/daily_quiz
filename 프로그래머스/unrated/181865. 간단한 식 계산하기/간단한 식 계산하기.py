def solution(binomial):
    answer = 0
    list1=binomial.split(' ')
    a=list1[0]
    b=list1[2]
    op=list1[1]
    return int(eval(a+op+b))

# return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))