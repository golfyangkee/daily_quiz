a = []

# 5줄 입력 받기
for _ in range(5):
    a.append(input().strip())  # 문자열을 리스트에 추가

# 최대 길이 찾기
num = max(len(word) for word in a)

result = ''

# 세로로 읽기
for k in range(num):
    for j in range(5):
        try:
            result += a[j][k]  # 현재 위치의 문자 추가
        except IndexError:
            pass  # 인덱스 초과 시 무시하고 넘어감

print(result)