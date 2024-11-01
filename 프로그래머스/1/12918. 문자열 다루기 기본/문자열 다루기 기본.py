def solution(s):
    return s.isdigit() and len(s) in [4,6] 
    # s 가 숫자로만 되어 있다면 True, s의 길이가 4 또는 6이면 True 반환해서
    # 둘다 True이면 True, 하나라도 False면 False 리턴
'''
내가 푼 것
def solution(s):
    r = ''.join(i for i in s if i.isdigit())
    if len(s) == 4 or len(s)==6:
        if len(r)==len(s):
            return True
    return False
'''
