
'''
2.1:
    Si on multiplie la fréquence par 2, le ton est plus élevé et la longueur du son est plus courte
    Si on divise la fréquence par 2, la hauteur est plus basse et la longueur du son est plus longue

2.2:
    Si on multiplie nombre de bits par échantillon par 2, le son est désordonné et bruyant
    Parce que 2 échantillon sont joués dans même temps
    Par example:
        Avec 8 bits par échantillon:
        01 02 03 04 05 06 07 08
        --|--|--|--|--|--|--|--

        Avec 16 bits par échantillon:
        01 02 03 04 05 06 07 08
        -----|-----|-----|-----
'''

def lit(fichier, position, nb_octets): #lit une suite d'octet et en retourne la liste
    fichier.seek(position)
    return list(fichier.read(nb_octets))

def lit_entier(fichier, position, nb_octets): # lit un entier sur plusieurs octets
    fichier.seek(position)
    return int.from_bytes(fichier.read(nb_octets), byteorder="little", signed=True)

def ecrit(fichier, position, octet) : # ecrit un seul octet
    fichier.seek(position)
    fichier.write(bytes([octet]))

def ecrit_liste(fichier, position, octets) : # ecrit une liste d'octets
    fichier.seek(position)
    fichier.write(bytes(octets))

def ecrit_entier(fichier, position, entier, nb_octets): # écrit un entier (sur plusieurs octets)
    fichier.seek(position)
    fichier.write(entier.to_bytes(nb_octets, byteorder='little', signed=True))

f = open("xf.wav", 'r+b')
la_frequence = lit_entier(f, 24, 4)
nombre_bits_par_echantillon = lit_entier(f, 34, 2)
nombre_octets = lit_entier(f, 40, 4)

print("La freqence est", la_frequence)
print("Nombre de bits par echantillon est", nombre_bits_par_echantillon)
print("Pour le contenu, nombre de octets est", nombre_octets)


'''
2.3: inverse the order of the sound
    we read from address 44
'''

# we read the existing content and store it to bytes_arr
# we have 8 bits / sample, so it equals to 1 byte / sample

bytes_arr = lit(f, 44, 44 + nombre_octets)

ecrit_liste(f, 44, reversed(bytes_arr))
f.close()
