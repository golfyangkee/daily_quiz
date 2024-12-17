import sys
input = sys.stdin.readline  # 빠른 입력을 위해 사용

# 입력 받기
n = int(input())  # 첫 번째 줄: 정수 개수 N
numbers = list(map(int, input().split()))  # 두 번째 줄: N개의 정수 입력

# 최솟값과 최댓값 구하기
min_value = min(numbers)
max_value = max(numbers)

# 결과 출력
print(min_value, max_value)

'''
from sys import stdin
# stdin은 표준 입력을 처리하는 객체


n, *num_list = map(int, stdin.buffer.read().split())
# **stdin.buffer.read()**는 모든 입력을 바이트 단위로 한 번에 읽음
# 일반적인 input()은 한 줄씩 입력을 처리하지만
# stdin.buffer.read()는 전체 입력을 한 번에 읽어 속도가 훨씬 빠름

print(min(num_list), max(num_list))
'''
