my_str = input()
my_dict = {}

for i in range(97, 123):
    my_chr = chr(i)
    my_dict[my_chr] = -1
    
for i in my_str:
    my_dict[i]=my_str.index(i)

print(*my_dict.values())

'''
find 함수
반환값
**find()**는 주어진 substring이 string에서 처음으로 나타나는 인덱스(정수)를 반환합니다.
만약 substring이 string에 없다면, **-1**을 반환합니다.

my_str = input()
for i in range(97, 123):
    print(my_str.find(chr(i)), end=' ')
'''
