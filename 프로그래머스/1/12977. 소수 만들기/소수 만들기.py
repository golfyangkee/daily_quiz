def solution(nums):
    answer = 0
    nums.sort()
    for i in range(len(nums)):
        result=0
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                result= nums[i]+nums[j]+nums[k] # 합 구하기
                
                # 소수인지 알기 위해 약수 구하기
                total=[]
                for s in range(1, result+1):
                    if result%s==0:
                        total.append(s)

                # 소수인지 구하기
                if len(total)==2:
                    answer+=1
                    # print('result', result, nums[i], nums[j], nums[k], 'total', total)
    return answer

