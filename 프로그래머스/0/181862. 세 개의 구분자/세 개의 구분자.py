def solution(myStr):
    answer = []
    str1=""
    for i in ["a","b","c"]:
        myStr=myStr.replace(i," ")
    answer=myStr.split()
    if not answer:
        answer=["EMPTY"]
    return answer