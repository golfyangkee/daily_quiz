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