n = int(input())  # 데이터의 개수
my_list = list(map(int, input().split()))  # 리스트에 입력된 값들

# 최대값 구하기
num_max = max(my_list)

# 각 값들을 최대값에 비례하여 100을 기준으로 변환
for i in range(n):
    my_list[i] = my_list[i] / num_max * 100

# 평균 구하기
avg_my_list = sum(my_list) / n
print(avg_my_list)