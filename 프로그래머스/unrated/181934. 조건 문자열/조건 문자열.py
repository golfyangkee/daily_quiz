def solution(ineq, eq, n, m):
    if ineq=='>' and eq=='=':
        if n>=m:
            return 1
        else:
            return 0
    elif ineq=='<' and eq=='=':
        if n<=m:
            return 1
        else:
            return 0
    elif ineq=='>' and eq=='!':
        if n>m:
            return 1
        else:
            return 0
    elif ineq=='<' and eq=='!':
        if n<m:
            return 1
        else:
            return 0
# 다른 풀이
# return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))