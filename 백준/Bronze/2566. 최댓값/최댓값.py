my_list = []
for i in range(9):
    row = list(map(int, input().split()))
    my_list.append(row)

n_max = max(max(row) for row in my_list)


row_index = 0
col_index=0

for i, row in enumerate(my_list):
    if n_max in row:
        row_index = i
        col_index = row.index(n_max)
        break # 찾으면 멈춰라
        
print(n_max)
print(f'{row_index+1} {col_index+1}')

'''
my_list=[]
for _ in range(9):
    my_list += list(map(int, input().split())) # 1차원으로 더해짐

n_max = my_list.max()

y, x = divmod(my_list.index(n_max), 9) 
# divmod(a, b) 는 a를 b로 나눴을 때 몫 과 나머지를 튜플형태로 반환하는 함수로 인덱스가 3면 3//9, 3%9 니까 (0,3) 이 나오게 되고
# 문제에서는 0번째가 아니라 1번부터 시작하고 있으니 각각 1씩 더해서 출력해준다.
# index 함수는 0부터 시작하는 인덱스값 반환 그니까 만약에 최대값 인덱스가 10이면 10//9, 10%9 = (1,1) 이 나올거고 
# 0~8까지 첫 째줄, 9~17까지가 두번째 줄 ... 할거고
# 실제 0행, 0열부터 시작이면 이대로 출력하면 되지만 1행 1열부터 시작이니까 +1 씩 해준다.

print(n_max)
print(y+1, x+1)
'''
