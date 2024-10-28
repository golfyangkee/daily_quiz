def solution(n):
    r = int(n**0.5)
    if n==r**2:
        return (r+1)**2
    else:
        return -1