def dec2bin(n):
    #return "{0:b}".format(n)
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2

    return result

print(dec2bin(148))

def hexa2dec(c):
    #return int(c, 16)
    n = 0
    for (i,ch) in enumerate(c):
        val = "0123456789ABCDEF".index(ch)
        ind = len(c) - i - 1
        n = n + val * (16 ** ind)
    return n
        

print(hexa2dec("ABCD"))