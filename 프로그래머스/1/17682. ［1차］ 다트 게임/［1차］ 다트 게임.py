def solution(dartResult):
    answers = [] # 각각의 한 세트씩의 점수들을 담을 리스트
    n='' # 한세트들을 문자열로 기록할 예정
    
    
    for i in dartResult:
        if i.isdigit(): # 숫자면 n에 더할거다. n은 0으로 초기화될 거다.
            n+=i
        elif i in 'SDT': # 문자면 각각 처리한다.
            answer=int(n)
            if i=='S':
                answers.append(answer**1)
            elif i=='D':
                answers.append(answer**2)
            elif i=='T':
                answers.append(answer**3)
            n='' # 한세트 완료 후 처리
        elif i == '*':
            answers[-1]*=2 # n이 아니라 담긴 리스트의 마지막 인수를 변경
            if len(answers)>1: # 본인과 앞의 숫자들만 건드니까 가정 넣어서 진행
                answers[-2]*=2
        elif i=='#':
            answers[-1]*=-1
    
    return sum(answers) # 각각 처리한 점수들 합침
    '''
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
    '''