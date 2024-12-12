A, B = map(int, input().split())
'''
if A>B:
    print('>')
elif A == B:
    print('==')
else:
    print('<')
'''
print("==" if A==B else "><"[A<B])
'''
"><"[A<B]의 의미
문자열 "><"는 두 문자 >와 <로 이루어진 문자열입니다.
[A<B]는 조건 A < B의 결과(True 또는 False)를 숫자 0 또는 1로 변환합니다:
A < B가 True이면 1.
A < B가 False이면 0.
'''
