def solution(order):
    answer = 0
    ameri_cnt=0
    latte_cnt=0
    for i in order:
        if "americano" in i:
            ameri_cnt+=1
        elif "latte" in i :
            latte_cnt+=1
        elif "anything" in i :
            ameri_cnt+=1
    answer=ameri_cnt*4500+latte_cnt*5000
    return answer