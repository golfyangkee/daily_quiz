n = list(map(int, input().split()))
result = []
real = [1, 1, 2, 2, 2, 8]
for i in range(len(real)):
    result.append(real[i]-n[i])
print(*result)