
'''
1.1:
    taille du fichier: 36 00 04 00 = 0x00040036 = 262198 bytes
    offset: 36 00 00 00 = 0x00000036 = 54
    largeur: 00 01 00 00 = 0x00000100 = 256 px
    hauteur: 00 FF FF FF = 0xFFFFFF00 = -256 px
    nombre de bits par couleur: 20 00 = 0x0020 = 32 bits

1.2:
    L'image est décalée,
    parce que le dernier pixel est ignoré sur chaque ligne. Donc, il apparaît à la ligne suivante.
    Par exemple:
        avant: 123456789
               123456789
               123456789
        après: 12345678
               91234567
               89123456

1.3:
    L'image est coupée en 2 et répétée 2 fois,
    parce que 2 lignes consécutives sont jointes.
    Par exemple:
        avant: 123456789
               123456789
               123456789
               123456789
        après: 123456789123456789
               123456789123456789

1.4:
    L'image est étirée et la couleur est dérangée,
    parce que les canaux de couleur sont dérangés.
    Par exemple, si l'arrangement des couleurs est: ARGBARGBARGBARGB
        avant (4 octets / couleur). Alors, on a 4 pixels:
            ARGB-ARGB-ARGB-ARGB
        après (2 octets / couleur). Alors, on a 8 pixels:
            AR-GB-AR-GB-AR-GB-AR-GB

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


'''
1.5: drapeau polonais
    Pologne's flag has 2 colors: white on top and red on bottom
    so we fill up half of all pixels with white color
    and the rest in red color
'''

f = open("formes_1.5.bmp", 'r+b')
taille_fichier = lit_entier(f, 2, 4)
debut_image = lit_entier(f, 10, 4)
bytes_arr = []

# the size of image is 256 by 256, so we have 256*256 pixels
num_of_pixels = 256 * 256

# for the top half (white)
for row in range(0, num_of_pixels // 2):
    bytes_arr.append(0xff) # blue
    bytes_arr.append(0xff) # green
    bytes_arr.append(0xff) # red
    bytes_arr.append(0xff) # non-transparent

# for the bottom half (red)
for row in range(0, num_of_pixels // 2):
    bytes_arr.append(0x00) # blue
    bytes_arr.append(0x00) # green
    bytes_arr.append(0xff) # red
    bytes_arr.append(0xff) # non-transparent

ecrit_liste(f, debut_image, bytes_arr)
f.close()


'''
1.6: drapeau français
    France's flag has 3 colors: blue - white - red
    We divide each row into 3 parts
    and fill blue - white - red respectively in each part
'''

f = open("formes_1.6.bmp", 'r+b')
taille_fichier = lit_entier(f, 2, 4)
debut_image = lit_entier(f, 10, 4)
bytes_arr = []

for row in range(0, 256):
    # we do this action on each of 256 rows
    for column in range(0, 256):
        if column < (256 // 3):
            # we fill blue color in the first part
            bytes_arr.append(0xff) # blue
            bytes_arr.append(0x00)
            bytes_arr.append(0x00)
            bytes_arr.append(0xff)
        elif column < (256 // 3) * 2:
            # we fill white color in the second part
            bytes_arr.append(0xff) # blue
            bytes_arr.append(0xff) # green
            bytes_arr.append(0xff) # red
            bytes_arr.append(0xff)
        else:
            # we fill red color in the rest of this row
            bytes_arr.append(0x00)
            bytes_arr.append(0x00)
            bytes_arr.append(0xff) # red
            bytes_arr.append(0xff)

ecrit_liste(f, debut_image, bytes_arr)
f.close()
