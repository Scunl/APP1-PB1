import sys
from fltk import attend_fermeture, cree_fenetre, mise_a_jour, rectangle

def traitement(file):
    """
    prend en parametre un fichier texte et retourne une liste contenant les lignes du fichier.
    """
    f = open(file, "r")
    liste = f.readlines()
    liste = totext(liste)
    f.close()
    return liste


def check(file: str) -> bool:
    """
    """
    cmp = 0 
    liste = traitement(file)
    liste = backslash(liste)
    while liste[cmp] == "":
        cmp+=1
    return liste[cmp]
    
def binaire(liste):
    liste2 = []
    for i in range(2, len(liste)):
        liste2.append(liste[i])
    return liste2

def totext(liste):
    """
    """
    liste2 = []
    for elem in liste:
        if '#' in elem:
            liste2.append(commentaire(elem))
        else:
            liste2.append(elem)
    return liste2


def commentaire(texte: str) -> str:
    """
    """
    a = texte.find("#")

    return texte[:a]


def suppression(liste):
    '''
    '''
    liste2 = []
    for elem in liste:
        if elem != '':
            liste2.append(elem)
    return liste2

def couple(liste):
    """
    """
    return liste[0], liste[1], "".join(liste[2:])

def backslash(liste):
    return list(map(str.rstrip, liste)) 


def parametrep1(liste: list) -> tuple:
    pixels = []
    px = liste[0]
    format = liste[1]
    for i in range(3, len(liste)):
        pixels.append(liste[i])
    return (px, format, pixels)

def parametrep3(liste: list) -> tuple:
    '''
    '''
    pixels = []
    format = liste[1]
    valmax = int(liste[2])
    px = liste[0]
    for i in range(3, len(liste)):
        pixels.append(liste[i])
    return (format, valmax, pixels)

def forme(format):
    liste = []
    format2 = format.split(" ")
    for elem in format2:
        liste.append(int(elem))
    return tuple(liste)


def separation(pixels):
    liste = []
    for elem in pixels:
        liste.append([elem])
    return liste


def separation2(pixels: list) -> tuple:
    liste = []
    for elem in pixels:
        for caractere in elem:
            liste.append(caractere.split(" "))
    return liste

def strtoint(pixels):
    liste = []
    for elem in pixels:
        for caractere in elem:
            if caractere != ' ':
                liste.append(int(caractere))
    return liste

def totuple(liste):
    """
    """
    liste2 = []
    for i in range(3, len(liste) + 3, 3):
        liste2.append((liste[i-3], liste[i-2], liste[i-1]))
    return liste2

def produit(liste):
    """
    """
    valmax = parametrep3(liste)
    liste2 = []
    for i, elem in enumerate(liste):
        liste2.append([])
        for val in elem:
            a = (val*255)//valmax
            liste2[i].append(a)
    return liste2


def convertion(liste):
    """
    """
    liste2 = list()
    for i, elem in enumerate(liste):
        liste2.append([])
        for tupl in elem:
            liste2[i].append(hex(tupl)[2:])
    return liste2

def addition(liste):
    '''
    '''
    print(liste)
    liste = convertion(liste)
    liste2 = []
    for i, seq in enumerate(liste):
        liste2.append([])
        for elem in seq:
            if len(elem) == 1:
                liste2[i].append(elem + '0')
            else:
                liste2[i].append(elem)
    return liste2

def addition2(liste):
    '''
    '''
    liste = addition(liste)
    liste2 = []
    for i in range(len(liste)):
        liste2.append(''.join(liste[i]))
    return liste2

def lignep3(x, y, liste, taille=1):
    """
    """
    cmpt = 0
    for j in range(x):
        for i in range(y):
            rectangle((i*taille), (j*taille), ((i+1)*taille) ,((j+1)*taille), remplissage='#' + str(liste[cmpt]), epaisseur=0)
            cmpt += 1
    return None

def lignep1(x, y, liste, taille=1):
    cmpt = 0
    for i in range(x):
        for j in range(y):
            
            if liste[x]:
                rectangle((j*taille), (i*taille), ((j+1)*taille) ,((i+1)*taille), remplissage='Black', epaisseur=0)
            else:
                rectangle((j*taille), (i*taille), ((j+1)*taille) ,((i+1)*taille), remplissage='White', epaisseur=0)
            cmpt += 1
    
    return None

def traitementp1(liste, taille=1):
    a, b = liste[0], liste[1]
    a = b.split(" ")
    liste2 = []
    for elem in a:
        liste2.append(int(elem))
    cree_fenetre(liste2[0]*taille, liste2[1]*taille)
    pixels = binaire(liste)
    pixels = strtoint(pixels)

    return a, b, pixels, liste2


def fonctiontraitementp1(liste, taille=1):
    file = "P1-P6\guybrush3.p3.ppm"
    liste = traitement(file)
    liste = totext(liste)
    liste = suppression(liste)
    liste = backslash(liste)
    a, b, pixels, liste2 = traitementp1(liste, taille)
    cmpt = 0
    for i in range(liste2[1]):
        for j in range(liste2[0]):
            if pixels[cmpt]:
                rectangle((j*taille), (i*taille), (j+1)*taille, (i+1)*taille, remplissage='Black', epaisseur=0)
            else:
                rectangle((j*taille), (i*taille), (j+1)*taille, (i+1)*taille, remplissage='White', epaisseur=0)
            cmpt += 1
    return None

def fonctiontraitementp3(liste):
    file = "P1-P6\chambers.txt"
    liste = traitement(file)
    liste = totext(liste)
    liste = suppression(liste)
    liste = backslash(liste)
    if check(file) == "P3":
        px, format, valmax, pixels = parametrep3(liste)
        pixels = separation(pixels)
        pixels = separation2(pixels)
        pixels = strtoint(pixels)
        pixels = totuple(pixels)
        pixels = produit(valmax, pixels)
        pixels = convertion(pixels)
        pixels = addition(pixels)
        pixels = addition2(pixels)
        x, y = forme(format)

def fonctionp2(liste, taille):
    pass



if __name__  == "__main__":

    liste = traitement("P3.txt")  
    liste = totext(liste)
    liste = suppression(liste)
    liste = backslash(liste)
    format, valmax, pixels = parametrep3(liste)
    x, y = forme(format)
    pixels = separation(pixels)                 #Doit check type de fichier
    pixels = separation2(pixels)               
    pixels = strtoint(pixels)
    pixels = totuple(pixels)
    pixels = produit(valmax, pixels)
    pixels = convertion(pixels)
    pixels = addition(pixels)
    pixels = addition2(pixels)
    
    if x < 100 and y < 100:
        cree_fenetre(x*100, y*100)
        lignep3(x, y, pixels, 100)
    else:
        cree_fenetre(x*10, y*10)
        lignep3(x, y, pixels, 10)
    attend_fermeture()