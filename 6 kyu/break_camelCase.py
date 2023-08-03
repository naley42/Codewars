def solution(s):
    # split the string into a list of letters
    s = list(s)
    
    #using enumerate to get the index of the letter, and store the index of the capital letter in a list
    capital_index = [i for i, letter in enumerate(s) if letter.isupper()]
    capital_index = [0] + capital_index
    
    #store the result in a list
    result = []
    
    #loop through the list of index to create the words
    for i in range(1, len(capital_index)):
        result.append(''.join(s[capital_index[i - 1]:capital_index[i]]))
    
    #append the last word
    result.append(''.join(s[capital_index[-1]:]))
    
    #return the result
    return ' '.join(result)
    
    
print(solution("helloWorld"))

#alt
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)

#alt
# import re
# def solution(s):
#     return re.sub('([A-Z])', r' \1', s)
