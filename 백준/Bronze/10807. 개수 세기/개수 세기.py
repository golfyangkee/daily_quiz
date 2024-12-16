import sys
input = sys.stdin.readline

n = int(input())
my_list = list(map(int, input().split()))
v = int(input())
print(my_list.count(v))