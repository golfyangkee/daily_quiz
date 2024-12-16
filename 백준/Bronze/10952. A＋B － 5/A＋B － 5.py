import sys
input = sys.stdin.readline
a, b = map(int, input().split())

while a != 0 and b !=0:
    print(a+b)
    a, b = map(int, input().split())
'''
for line in sys.stdin:
    a, b = map(int, line.split())
    if a + b != 0:
        print(a + b)
'''
