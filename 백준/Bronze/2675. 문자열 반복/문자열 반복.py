n = int(input())
for _ in range(n):
    my_str = ''
    m, s = map(str, input().split())
    for i in s:
        my_str+=i*int(m)
    print(my_str)