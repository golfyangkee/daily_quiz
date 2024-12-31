s = input()
my_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
result = 0
for i in my_list:
    result += s.count(i)
    s = s.replace(i, ' ')
s = s.replace(' ', '')
print(result+len(s))