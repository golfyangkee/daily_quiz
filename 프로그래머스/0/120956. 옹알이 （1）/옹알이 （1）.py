def solution(babbling):
    words = ['aya', 'ye', 'woo', 'ma']
    for i in range(0, len(babbling)):
        for word in words:
            babbling[i] = babbling[i].replace(word,' ')
        babbling[i]= babbling[i].replace(' ','')
    return babbling.count('')
# 키포인트 : 안에 있다면 ' '로 바꿔서 카운트 해보자.