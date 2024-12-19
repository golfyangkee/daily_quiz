my_set = set()

for _ in range(10):
    n = int(input())
    my_set.add(n%42)

print(len(my_set))