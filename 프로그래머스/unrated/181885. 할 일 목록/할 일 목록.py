def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if int(finished[i])==0:
            answer.append(todo_list[i])
    return answer

# 다른 풀이
# return [work for idx, work in enumerate(todo_list) if not finished[idx]]