def solution(order):
    answer = 0
    s_order = str(order)
    num1 = s_order.count('3')
    num2 = s_order.count('6')
    num3 = s_order.count('9')
    answer = num1 + num2 + num3
    return answer