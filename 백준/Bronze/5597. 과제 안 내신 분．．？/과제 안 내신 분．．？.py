my_list = []
for _ in range(28):
    n = int(input())
    my_list.append(n)

x_list = []
for i in range(1, 31):
    if i in my_list:
        pass
    else:
        x_list.append(i)
x_list.sort()
print(x_list[0])
print(x_list[1])