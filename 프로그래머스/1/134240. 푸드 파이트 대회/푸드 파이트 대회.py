def solution(food):
    answer = ''
    for i in range(len(food)):
        if food[i] == 1:
            continue
        else:
            result=food[i]//2
            answer+=str(i)*result
    re_answer=answer[::-1]
    answer+='0'+re_answer
    return answer