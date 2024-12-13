import sys
input = sys.stdin.readline

result = 0
X = int(input())
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    result += a*b
if X == result:
    print('Yes')
else:
    print('No')