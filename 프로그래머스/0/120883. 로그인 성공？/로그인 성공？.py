def solution(id_pw, db):
    answer = ''
    for id1, pw in db:
        if id1==id_pw[0]:
            if pw==id_pw[1]:
                answer='login'
            elif pw!=id_pw[1]:
                answer='wrong pw'
        elif id1!=id_pw[0]:
            if pw!=id_pw[1]:
                answer='fail'
    return answer