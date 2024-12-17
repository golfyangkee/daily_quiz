*a,=map(int,open(0)) 
# open(0)은 **표준 입력(stdin)**을 의미합니다.
# 이는 **sys.stdin**과 같은 역할을 하지만, 파일처럼 열어서 입력을 읽을 수 있습니다.
# open(0)을 호출하면 표준 입력의 모든 내용을 읽어옵니다.
# 언패킹을 통해 map 객체에서 반환된 모든 정수 값을 리스트 **a**에 저장합니다.
# ***a,**에서 콤마(,)는 튜플 언패킹을 의미하지만, Python 문법상 단일 리스트로 저장됩니다.
# 예를 들어 1, 4, 2, 6, 3이 입력되면 a = [1, 4, 2, 6, 3]이 됩니다.

m=max(a)
print(m,a.index(m)+1)

'''
from sys import stdin

my_list = list(map(int, stdin.buffer.read().split()))
num_max = max(my_list)
print(num_max)
print(my_list.index(num_max)+1)
'''
