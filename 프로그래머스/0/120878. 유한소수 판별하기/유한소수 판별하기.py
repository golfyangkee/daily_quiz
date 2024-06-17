def solution(a, b):
    answer = 2
    b_list = []
    # a 랑 b 공통 인수로 나누기
    for i in range(2, 1001):
        if a%i==0 and b%i ==0:
            a //= i
            b //= i
            
    # b 약수 찾기
    # b_copy = b
    # for num in range(2, b_copy+1):
    #     if b%num == 0:
    #         b_list.append(num)
    #         b //= num
    div =2
    while b > 1 :
        if b%div == 0:
            b_list.append(div)
            b = b//div
            # 계속 나눔
        else: 
            # 2로 안 나눠지면 하나씩 키움
            div+=1


    if all(x in [2, 5] for x in b_list):
    # if b_list == [5] or b_list==[2] or b_list ==[2,5]:
        answer = 1
    return answer