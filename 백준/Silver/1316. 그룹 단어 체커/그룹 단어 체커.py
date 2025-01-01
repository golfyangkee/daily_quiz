n = int(input())  # 단어 개수 입력
result = 0  # 그룹 단어 개수

for _ in range(n):
    s = input()  # 단어 입력
    seen = set()  # 등장한 문자 저장
    prev = None  # 이전 문자
    
    is_group_word = True
    for char in s:
        if char != prev:  # 새로운 문자 등장
            if char in seen:  # 이미 나온 문자라면 그룹 단어가 아님
                is_group_word = False
                break
            seen.add(char)  # 새로운 문자 저장
        prev = char  # 이전 문자 갱신
    
    if is_group_word:
        result += 1

print(result)

'''
N = int(input())
count = 0

for _ in range(N):
  string = input()
  if list(string) == sorted(string, key=string.find):
    count += 1

print(count)
'''
