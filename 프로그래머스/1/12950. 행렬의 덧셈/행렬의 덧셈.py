def solution(arr1, arr2):
    n = len(arr1)
    answer=[]
    for i in range(n):
        row = [] # 한 행렬 크기 저장할 리스트
        
        for j in range(len(arr1[0])):
        # for j in range(n): 하면 안된다.
        # 정사각형 배열이 아니라 그냥 arr1과 arr2의 행렬 크기가 같다는 의미이다.
            row.append(arr1[i][j]+arr2[i][j])
        answer.append(row)
    return answer
'''
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[i])):
            row.append(arr1[i][j]+arr2[i][j])
        answer.append(row)
    return answer
'''