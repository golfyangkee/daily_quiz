import sys
input = sys.stdin.read  # 표준 입력을 한꺼번에 읽습니다.

data = input().splitlines()  # 모든 입력을 줄 단위로 분리합니다.
T = int(data[0])  # 첫 번째 줄은 테스트 케이스의 수입니다.

for i in range(1, T + 1):  # 두 번째 줄부터 데이터를 처리합니다.
    a, b = map(int, data[i].split())  # 각 줄을 분리하여 a와 b로 나눕니다.
    print(a + b)  # 결과 출력