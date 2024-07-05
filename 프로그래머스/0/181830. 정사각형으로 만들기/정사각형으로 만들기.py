def solution(arr):
    row = len(arr)
    column = len(arr[0])
    if row > column:
        num = row-column
        for i in range(0,row):
            for j in range(0,num):
                arr[i].append(0)
    elif row < column:
        num = column - row
        for i in range(0,num):
            add = []
            for j in range(0, column):
                add.append(0)
            arr.append(add)
    return arr