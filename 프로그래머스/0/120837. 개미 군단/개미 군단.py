def solution(hp):
    answer = 0
    장군 = hp//5
    병정 = hp%5//3
    일 = hp%5%3
    answer = 장군 + 병정 + 일
    return answer