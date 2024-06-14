def solution(before, after):
    answer = 0
    list_before = [i for i in before]
    list_after = [i for i in after]
    if sorted(list_before) == sorted(list_after):
        answer = 1
    return answer