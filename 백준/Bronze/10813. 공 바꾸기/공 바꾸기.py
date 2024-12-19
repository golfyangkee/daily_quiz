n, m = map(int, input().split())
my_dict = {}
for i in range(n):
    my_dict[i+1] = i+1
    
for q in range(m):
    i, j = map(int, input().split())
    my_dict[i] , my_dict[j] = my_dict[j], my_dict[i]

print(*my_dict.values())