def solution(age):
    # 딕셔너리로 풀기
    dict1 = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    answer1= ''.join(dict1[int(i)] for i in str(age))
    
    # 튜플로 풀기
    tuple1= ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
    answer2 = ''.join(tuple1[int(i)] for i in str(age))
    
    # 문자열로 풀기
    str1 = 'abcdefghij'
    answer3 = ''.join(str1[int(i)] for i in str(age))
    
    return answer3