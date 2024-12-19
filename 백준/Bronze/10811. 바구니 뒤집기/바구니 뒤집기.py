n, m = map(int, input().split())
my_list = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    my_list[i-1:j] = my_list[i-1:j][::-1]

print(*my_list)