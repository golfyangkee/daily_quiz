def solution(myString, pat):
    my=myString.lower()
    pat_low=pat.lower()
    if pat_low in my:
        return 1
    else:
        return 0