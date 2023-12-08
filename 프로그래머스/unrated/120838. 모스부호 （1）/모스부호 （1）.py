def solution(letter):
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    
    answer = "".join([morse[code] for code in letter.split()])
    # 문자열.split(sep, maxsplit) 함수는 
    # 문자열을 maxsplit 횟수만큼 sep의 구분자를 기준으로 
    # 문자열을 구분하여 잘라서 리스트로 만들어 줍니다
    return answer