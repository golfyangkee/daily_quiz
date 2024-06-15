def solution(chicken):
    answer = 0
    coupon = chicken
    while coupon >=10 :
        result = coupon //10
        answer += result
        coupon = coupon % 10 + result
    return answer