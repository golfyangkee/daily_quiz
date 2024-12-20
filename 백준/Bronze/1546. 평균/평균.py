n = int(input())
my_list = list(map(int, input().split()))
num_max = max(my_list)
for i in range(n):
    my_list[i] = my_list[i]/num_max *100
avg_my_list = sum(my_list)/n
print(avg_my_list)