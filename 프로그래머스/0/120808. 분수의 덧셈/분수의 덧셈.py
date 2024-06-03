def solution(numer1, denom1, numer2, denom2):
    answer = []
    num1 = numer1*denom2 + numer2*denom1
    num2 = denom1*denom2
    # 최대공약수
    num3 = gcd(num1, num2)
    answer = [num1/num3, num2/num3]
    return answer

# 최대공약수 구하는 함수 정의 ; 유클리드 호제
def gcd(a, b):
    while b:
        a,b = b, a%b
    return a