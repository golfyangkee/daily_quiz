def solution(order):
    answer = 0
    dict1 = {4500:["iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"], 5000:["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]}
    menu = {}
    for price, items in dict1.items():
        for item in items:
            menu[item] = price
    
    for i in order:
        if i in menu:
            answer += menu[i]
    return answer