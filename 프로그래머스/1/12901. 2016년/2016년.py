def solution(a, b):
    
    # 1월1일이 금요일인까 금요일을 0인덱스로 둠
    weeks = ['FRI','SAT','SUN', 'MON','TUE','WED','THU']
    
    # 월에 따른 한달 일수 인데 5월 날짜면 아직 4월까지만 지난거니까
    day= [0, 31,29, 31,30,31,30,31,31,30,31,30]
    days=0
    for i in range(0,a): # a-1 달 만큼의 일수를 더한다.
        days+=day[i]
    
    # -1 을 하는 이유는 인덱스는 0부터 시작하니까
    return weeks[(days+b-1)%7]