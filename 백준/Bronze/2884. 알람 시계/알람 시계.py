H, M = map(int, input().split())
if M>=45:
    M -=45
    print(f'{H} {M}')
else:
    M = M+15
    if H == 0:
        H = 23
    else:
        H -=1
    print(f'{H} {M}')