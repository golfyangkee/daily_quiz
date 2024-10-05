def solution(cards1, cards2, goal):
    for i in goal:
        # len 안 하면 out of range 나온다.
        if len(cards1)>0 and i==cards1[0]:
            # pop 함수는 인덱스를 제거
            cards1.pop(0)
        elif len(cards2)>0 and i==cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
    return 'Yes'