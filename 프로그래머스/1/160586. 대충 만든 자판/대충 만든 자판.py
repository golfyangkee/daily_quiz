def solution(keymap, targets):
    answer = []
    hs = {} # 각 요소에 가장 최단 수의 알파벳들을 넣을 튜플
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1
            # 만약에 hs 안에 같은 문자가 있다면 더 작은 값을 넣는다.
        
    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs: # 없으면 break
                ret = - 1
                break
            ret += hs[ch] # hs 안에 있다면 valuse 값 더하기
        answer.append(ret)

    return answer

'''
def solution(keymap, targets):
    answer = []
    
    for target in targets:
        sum_, fail = 0, False
        for t in target:
            min_index = 999
            for key in keymap:
                min_index = key.find(t) if key.find(t) != -1 and key.find(t) <= min_index else min_index
            
            if min_index == 999 : fail = True ; break
            sum_ += min_index+1
        
        if fail : answer.append(-1)
        else : answer.append(sum_)
    
    return answer 
'''