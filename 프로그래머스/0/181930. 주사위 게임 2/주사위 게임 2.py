def solution(a, b, c):
    answer = 0
    list1 = [a,b,c]
    list2 = list(set(list1))
    num = len(list2)
    if num == 3:
        answer = a+b+c
    elif num == 2:
        answer = (a+b+c) * (a**2+b**2+c**2)
    elif num == 1:
        answer = (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3) 
    return answer