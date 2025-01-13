'''
 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither
'''
while 9999:
    a, b = map(int, input().split())
    if a == 0 and b==0:
        break
    elif a%b == 0:
        print('multiple')
    elif b%a == 0:
        print('factor')
    else:
        print('neither')