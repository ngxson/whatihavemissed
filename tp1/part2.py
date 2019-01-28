def somme2bits(bit1, bit2):
    return str(int(bit1) ^ int(bit2))

def retenue3bits(b1, b2, b3):
    return str((int(b1) + int(b2) + int(b3)) >> 1)

def somme(n1, n2):
    max_ch = max(len(n1), len(n2))
    if len(n1) < len(n2):
        padding = max_ch - len(n1)
        n1 = "0" * padding + n1
    else:
        padding = max_ch - len(n2)
        n2 = "0" * padding + n2

    reminder = "0"
    result = ""
    for i in reversed(range(max_ch)):
        result = str(somme2bits(reminder, somme2bits(n1[i], n2[i]))) + result
        reminder = retenue3bits(reminder, n1[i], n2[i])
    if reminder == "1":
        result = "1" + result
    return result

print(somme("1011", "111"))

def produit(a, b):
    result = "0"
    for (i, num) in enumerate(b):
        if num == "1":
            result = somme(result, a + "0" * (len(b) - i - 1))
    return result

print(produit("1010", "101"))