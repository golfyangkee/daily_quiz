from sys import stdin

my_list = list(map(int, stdin.buffer.read().split()))
num_max = max(my_list)
print(num_max)
print(my_list.index(num_max)+1)