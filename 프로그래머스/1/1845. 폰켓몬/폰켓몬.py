def solution(nums):
    answer = 0
    n = len(nums)//2
    num = set(nums)
    result = len(num)

    return min(n,result)