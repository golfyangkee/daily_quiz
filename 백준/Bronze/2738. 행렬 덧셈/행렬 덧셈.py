f, l = map(int, input().split())
a = []
b = []
result = []
for _ in range(f):
    a.append(list(map(int, input().split())))

for _ in range(f):
    b.append(list(map(int, input().split())))
    
for i in range(f):
    row = []
    for j in range(l):
        row.append(a[i][j]+b[i][j])
    result.append(row)

for row in result:
    print(*row)

'''
for i in range(N):
    for j in range(M):
        A[i][j] = A[i][j] + B[i][j]
    print(*A[i])
'''
