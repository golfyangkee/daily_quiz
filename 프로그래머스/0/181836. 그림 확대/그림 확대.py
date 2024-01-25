def solution(picture, k):
    answer = []
    for row in picture: # 이미지의 한 줄을 가져온다.
        resized = ''
        
        for pixel in row:
            resized += pixel * k # 한 픽셀을 k배 만큼 가로로 늘린다.
        
        for _ in range(k):
            answer.append(resized) # 가로로 늘려진 이미지 한 줄을 k배 만큼 세로로 늘린다. 
# 언더스코어 _는 반복 변수의 값을 사용하지 않을 때 사용되는 관례적인 표현입니다. 여기서는 _를 통해 반복 횟수만큼 반복한다는 것을 나타냅니다.
    return answer