# eval 쓰는게 보안 상 안 좋다고 함
def solution(quiz):
    answer = []
    for i in quiz:
        result = i.split()
        index_1 = result.index('=')
        if eval(''.join(result[:index_1])) == int(result[index_1+1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer
