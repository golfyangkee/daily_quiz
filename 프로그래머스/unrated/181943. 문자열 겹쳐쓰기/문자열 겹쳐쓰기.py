def solution(my_string, overwrite_string, s):
    answer=''
    len1=len(overwrite_string)
    answer=my_string[:s]+overwrite_string+my_string[s+len1:]
    return answer