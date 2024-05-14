def solution(cipher, code):
    answer = ''
    for i in range(1, len(cipher)//code+1):
        answer=answer+cipher[(code*i)-1]
    return answer
'''
슬라이스 이용하기
    return cipher[code-1::code]
'''