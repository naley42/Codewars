def dig_pow(n, p):
    total = 0
    digits = [int(d) for d in str(n)]
    total = sum([digits[i] ** (p + i) for i in range(len(digits))])
    k = total / n
    
    return k if int(k) == k else -1

#alt
# def dig_pow(n, p):
#     k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
#     return -1 if fail else k