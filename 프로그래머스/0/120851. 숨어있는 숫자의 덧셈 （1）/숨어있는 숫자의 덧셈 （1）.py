def solution(my_string):
    # 예외구문 사용하기
    # answer = 0
    # for i in my_string:
    #     try:
    #         # 숫자가 되면 더하기
    #         answer += int(i)
    #     except ValueError:
    #         # 밸류에러 나면 pass
    #         pass
    # return answer

    # isdigit() 함수 이용하기 - 숫자인지 판별
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer+=int(i)
    return answer