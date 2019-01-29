def dec2bin(n):
    #return "{0:b}".format(n)
    result = ""
    while n > 0:
        # divide n by 2, and take the rest
        result = str(n % 2) + result
        # divide n by 2, take the result (integer) and save it back to n
        n = n // 2
    return result

print(dec2bin(148))

def hexa2dec(c):
    #return int(c, 16)
    n = 0
    for (i,ch) in enumerate(c):
        digit = "0123456789ABCDEF".index(ch) # get value of this digit in decimal
        pos = len(c) - i - 1 # position of this digit
        n = n + digit * (16 ** pos) # add the value of this digit to n
    return n


print(hexa2dec("ABCD"))