def solution(ineq, eq, n, m):
    if ineq == '>':
        if eq =='=':
            return int(bool(n>=m))
        else:
            return int(bool(n>m))
    elif ineq == '<':
        if eq == '=':
            return int(bool(n<=m))
        else:
            return int(bool(n<m))
