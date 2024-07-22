'''
등차수열이란?
등차수열(等差數列)은 각 항이 일정한 차이를 가지며 나열된 수열을 말합니다. 이 일정한 차이를 공차(公差)라고 합니다. 예를 들어, 수열 2, 5, 8, 11, 14는 공차가 3인 등차수열입니다. 각 항을 이전 항에 공차를 더한 값으로 얻을 수 있습니다.
'''
'''
정리하면 True만 더해
'''
def solution(a, d, included):
    answer = 0
    
    # true만 더해보자.
    for i in range(len(included)):
    # answer += (a + d * i) * int(included[i])
    # int(true) = 1 이니까 이런식으로 for 문 안쓰고도 할 수 있다.
        if included[i] ==True:
            answer += a + d*i

    return answer