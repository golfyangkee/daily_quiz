n = input().upper()  # 대소문자를 구분하지 않으려면 모두 대문자로 변환
my_dict = {}

# 문자열 순회하며 빈도 계산
for i in n:
    my_dict[i] = my_dict.get(i, 0) + 1

# 최대 빈도 찾기
max_num = max(my_dict.values())

# 최대 빈도를 가진 문자 찾기
my_list = [key for key, value in my_dict.items() if value == max_num]

# 결과 출력
if len(my_list) != 1:
    print('?')
else:
    print(my_list[0])