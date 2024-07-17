def solution(arr):
    even = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    for i in even:
        if len(arr)<=i:
            if len(arr)==i:
                break
            else:
                while len(arr)!=i:
                    arr.append(0)
                break
    return arr