n, m = map(int, input().split())
my_dict = {}
for i in range(n):
    my_dict[i+1] = 0
    
for q in range(m):
    i, j, k = map(int, input().split())
    for key in range(i, j+1): # 딕트는 슬라이싱 안됨
        my_dict[key] = k

print(*my_dict.values())