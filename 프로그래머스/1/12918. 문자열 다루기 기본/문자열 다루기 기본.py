def solution(s):
    return s.isdigit() and len(s) in [4,6]
'''
내가 푼 것
def solution(s):
    r = ''.join(i for i in s if i.isdigit())
    if len(s) == 4 or len(s)==6:
        if len(r)==len(s):
            return True
    return False
'''
