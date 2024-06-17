def solution(numlist, n):
# sorted 함수 key 사용
# key = 의 기준을 (abs(n-x), n-x) 딕트 형태로 만들고
# 절대값이 같으면 n-x 값을 기준으로 정렬
# 일단 절대값이니 0 부터 쭈루륵
# 그 중 절대값이 같으면 더 큰 수로 정렬
    return sorted(numlist, key = lambda x : (abs(n-x), n-x))