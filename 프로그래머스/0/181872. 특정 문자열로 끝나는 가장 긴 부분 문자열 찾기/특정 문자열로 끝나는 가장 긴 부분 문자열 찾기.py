def solution(myString, pat):
    answer = ''
    re_s=myString[::-1]
    re_p=pat[::-1]
    if re_p in re_s:
        a=re_s.index(re_p)
        re_a=re_s[a:]
        answer=re_a[::-1]
    return answer
# solution=lambda x,y:x[:x.rindex(y)+len(y)]