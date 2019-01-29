def somme2bits(bit1, bit2):
    # XOR operation
    # https://en.wikipedia.org/wiki/XOR_gate
    return str(int(bit1) ^ int(bit2))


def retenue3bits(b1, b2, b3):
    # bit shift (right) operation
    # https://stackoverflow.com/questions/141525
    return str((int(b1) + int(b2) + int(b3)) >> 1)


def somme(n1, n2):
    max_ch = max(len(n1), len(n2)) # maximum number of characters
    if len(n1) < len(n2):
        # if n1 is shorter, fill the rest with 0
        padding = max_ch - len(n1)
        n1 = "0" * padding + n1
    else:
        # if n2 is shorter, fill the rest with 0
        padding = max_ch - len(n2)
        n2 = "0" * padding + n2

    reminder = "0"
    result = ""
    for i in reversed(range(max_ch)): # do in reversed order
        result = somme2bits(reminder, somme2bits(n1[i], n2[i])) + result
        reminder = retenue3bits(reminder, n1[i], n2[i])

    if reminder == "1":
        # in the end, if reminder = 1, we write it to the end of result
        result = "1" + result

    return result


print(somme("1011", "111"))


def produit(a, b):
    result = "0"
    # we will try to do multiplication by adding
    for (i, num) in enumerate(b):
        if num == "1":
            pos = len(b) - i - 1 # position of this digit
            # add zeros to the right of the number, and add it back to result
            result = somme(result, a + "0" * pos)
    return result


print(produit("1010", "101"))
