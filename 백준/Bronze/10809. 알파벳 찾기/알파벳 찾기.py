my_str = input()
my_dict = {}

for i in range(97, 123):
    my_chr = chr(i)
    my_dict[my_chr] = -1
    
for i in my_str:
    my_dict[i]=my_str.index(i)

print(*my_dict.values())