def solution(numbers):

    # dict1 = {'one': 1, 'two': 2, 'three': 3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    # answer = numbers.replace(dict1)
    # if 'one' in numbers:
    
    # 일일히 바꾸기
    # answer = ''
    # answer = numbers.replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9').replace('zero', '0')
    # return int(answer)

    # enumerate 로 풀기
    for num, eng in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine']):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)