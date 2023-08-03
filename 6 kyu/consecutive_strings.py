def longest_consec(strarr, k):
    n = len(strarr)
    
    if n == 0 or k > n or k <= 0:
        return ''
    
    ans = ''.join(strarr[:k])
    for i in range(1, n - k + 1):
        tmp = ''.join(strarr[i:i + k])
        if len(tmp) > len(ans):
            ans = tmp
    
    return ans