def solution(s, n):
    # 다른 풀이
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    '''
    answer = ''
    for i in s:
        result = ord(i)+n
        if i ==' ':
            answer+=i            
        elif i.isupper() :
            if result > 90:
                answer += chr(64+result%90)
                # 왜 65가 아니라 64이냐면 91은 나머지가 1인데 65가 되어야 하니까
            else:
                answer += chr(result)
        else:
            if result > 122:
                answer  += chr(96 + result%122)
            else:
                answer += chr(result)
    return answer
    '''
# def solution(s, n):
#     answer = ''
#     '''65-90= 26개
#     97-122'''
#     for i in s:
#         if i == ' ':
#             answer+=i
#         elif 'A'<=i<='Z':
#             result=ord(i)+n%27
#             if result>90:
#                 answer+=chr(65+(result%90-1))
#             else:
#                 answer+=chr(result)
#         elif 'a'<=i<='z':
#             result=ord(i)+n%27
#             if result>122:
#                 answer+=chr(97+(result%122-1))
#             else:
#                 answer+=chr(result)
#     return answer