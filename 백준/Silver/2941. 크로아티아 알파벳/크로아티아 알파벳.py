s = input()
my_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
result = 0
for i in my_list:
    result += s.count(i)
    s = s.replace(i, ' ')
s = s.replace(' ', '')
print(result+len(s))

'''
replace 를 쓰면 효율이 떨어진다.
그래서 효율을 어떻게 하면 높일 수 있을 지 보았다.
'''
s = input()
patterns = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
i = 0
count = 0

while i < len(s):
    if s[i:i+3] == 'dz=':
        i += 3
    elif s[i:i+2] in patterns:
        i += 2
    else:
        i += 1
    count += 1

print(count)

'''
지피티 말로는 replace 를 없이 한번만 순회하면 진행 가능하도록 만든 거다.

replace()와 count()를 반복적으로 쓰는 대신 한 번만 순회 (while 루프)하면서 처리.

'dz='는 3글자이므로 먼저 검사.

매칭되면 해당 길이만큼 i를 증가시키고, 아니면 1씩 이동.

매치 여부와 상관없이 문자 하나를 처리했으므로 count += 1.

for 문보다는 while문 사용이 더 효율적인 듯 하다
'''
