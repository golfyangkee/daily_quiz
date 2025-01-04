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