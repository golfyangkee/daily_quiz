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
# *** (애스터리스크)**는 **"언패킹 연산자"**입니다.
# 첫 번째 요소를 n에 저장하고, 나머지 숫자들을 num_list에 리스트 형태로 저장
# **언패킹(unpacking)**은 여러 개의 값을 하나의 변수나 객체에서 꺼내어 각각의 변수에 나누어 담는 작업을 의미합니다.
# Python에서는 **리스트, 튜플, 혹은 기타 반복 가능한 객체(iterable)**를 여러 개의 변수로 언패킹할 수 있습니다. 언패킹은 = 연산자를 사용해 여러 변수에 값을 할당할 때 이루어집니다.
# # 튜플 언패킹
# a, b, c = (1, 2, 3)
# print(a)  # 출력: 1
# print(b)  # 출력: 2
# print(c)  # 출력: 3

# # 리스트 언패킹
# x, y, z = [10, 20, 30]
# print(x)  # 출력: 10
# print(y)  # 출력: 20
# print(z)  # 출력: 30

print(min(num_list), max(num_list))
'''
