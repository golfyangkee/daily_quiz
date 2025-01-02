my_dict = {'A+': 4.5, 'A0': 4, 'B+':3.5, 'B0':3, 'C+':2.5, 'C0':2, 'D+':1.5, 'D0':1, 'F':0}
result = 0
s_count = 0
for _ in range(20):
    s, n, g = input().split()
    n = float(n)
    if g =='P':
        continue
    g = my_dict[g]
    result +=n*g
    s_count+=n
print(result/s_count)