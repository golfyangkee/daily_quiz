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
    # if db_pw := dict(db).get(id_pw[0]):
    #     return "login" if db_pw == id_pw[1] else "wrong pw"
    # return "fail"
#  Python 3.8부터 도입된 "walrus 연산자(walrus operator)"
# 대입문과 표현식을 결합하여 한 번의 평가에서 값을 변수에 할당하고 그 값을 다시 사용할 수 있게 합니다.