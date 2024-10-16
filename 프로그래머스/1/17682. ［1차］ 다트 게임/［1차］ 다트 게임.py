def solution(dartResult):
    scores = []  # 각 라운드의 점수를 저장할 리스트
    n = ''  # 현재 점수를 저장할 변수 (문자열로 누적)

    for char in dartResult:
        if char.isdigit():  # 숫자인 경우
            n += char  # 여러 자리 수를 처리하기 위해 누적
        elif char in 'SDT':  # 보너스 문자일 경우
            score = int(n)  # 누적된 숫자를 정수로 변환
            if char == 'S':
                scores.append(score ** 1)
            elif char == 'D':
                scores.append(score ** 2)
            elif char == 'T':
                scores.append(score ** 3)
            n = ''  # 점수 초기화
        elif char == '*':  # 스타상 처리
            scores[-1] *= 2  # 현재 점수를 2배로
            if len(scores) > 1:  # 이전 점수도 있다면 2배로
                scores[-2] *= 2
        elif char == '#':  # 아차상 처리
            scores[-1] *= -1  # 현재 점수를 마이너스로

    return sum(scores)  # 최종 점수 합산