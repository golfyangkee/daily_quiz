def solution(numbers, direction):
    answer = []
    if direction == "left":
        answer = numbers[1:]
        answer.append(numbers[0])
    elif direction == "right":
        # answer.append(numbers[-1]) # 추가하는 객체의 성질 유지
        answer.extend(numbers[0:-1]) # 기존의 성질을 유지한 채 추가
        answer.insert(0, numbers[-1]) # 0번째 인덱스에서 추가
    return answer