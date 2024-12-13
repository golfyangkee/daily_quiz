import sys
input = sys.stdin.readline

n = int(input())
'''
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
'''
for i in range(n):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')