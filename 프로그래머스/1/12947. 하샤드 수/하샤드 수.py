def solution(x):
    hap = 0
    x_copy = x
    while x_copy >= 1:
        hap += x_copy%10
        x_copy = x_copy//10
    if x%hap ==0:
        return True
    return False