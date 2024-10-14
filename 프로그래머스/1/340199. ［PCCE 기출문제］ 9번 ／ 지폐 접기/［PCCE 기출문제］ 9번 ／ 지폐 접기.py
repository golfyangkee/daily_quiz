def solution(wallet, bill):
    answer = 0

    # 지폐의 긴 쪽과 짧은 쪽을 구분
    bill = sorted(bill, reverse=True)   # 큰 값이 bill[0], 작은 값이 bill[1]
    wallet = sorted(wallet, reverse=True)  # 큰 값이 wallet[0], 작은 값이 wallet[1]
    
    # if bill[0] > wallet[0] or bill[1] > wallet[1]:
    #         bill[0] /= 2
    #         bill.sort(reverse=True)
    #         answer += 1
    while 1:
        # 긴 쪽부터 접음
        if bill[0] > wallet[0] or bill[1] > wallet[1]:
            bill[0] //= 2  # 소수점 이하 버림
            bill.sort(reverse=True)
            answer += 1
        else:
            break
    return answer