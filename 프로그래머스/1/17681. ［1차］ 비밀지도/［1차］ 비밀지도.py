# def solution(n, arr1, arr2):
#     answer = []
#     result=[]
#     for i in arr1:
#         for j in arr2:
#             result.append(bin(i)|bin(j))
#     for i in result:
#         i.replace(0, ' ').replace(1. '#')
#         answer.append(i)
#     return answer

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        # arr1[i]와 arr2[i]에 대해 비트 OR 연산을 수행
        binary_or = bin(arr1[i] | arr2[i])[2:]  # '0b'를 제거하고 이진수로 변환
        # 이진수를 n길이로 맞추기 위해 앞쪽을 0으로 채움
        binary_or = binary_or.zfill(n)
        
        # '0'을 ' '로, '1'을 '#'으로 변환
        result = binary_or.replace('0', ' ').replace('1', '#')
        
        # 결과를 answer에 추가
        answer.append(result)
    
    return answer

# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer
