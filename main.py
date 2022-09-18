from re import I
from xdrlib import ConversionError
from fltk import attend_fermeture, cree_fenetre, rectangle

def traitement(file):
    """
    prend en parametre un fichier texte et retourne une liste contenant les lignes du fichier.
    """
    f = open(file, "r")
    liste = f.readlines()
    liste = totext(liste)
    return liste


def check(file: str) -> bool:
    """
    """
    cmp = 0 
    liste = traitement(file)
    liste = backslash(liste)
    while liste[cmp] == "":
        cmp+=1
    if liste[cmp] == "P3":
        return True
    return False
    

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


def parametre(liste: list) -> tuple:
    '''
    '''
    pixels = []
    format = liste[1]
    valmax = int(liste[2])
    for i in range(3, len(liste)):
        pixels.append(liste[i])
    
    return (format, valmax, pixels)

def forme(format):
    liste = []
    for elem in format:
        if elem != ' ':
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
            if len(caractere) > 0:
                liste.append(int(caractere))
    return liste

def inttohex(pixels):
    """
    """
    couple = tuple
    
    return couple

def totuple(liste):
    """
    """
    liste2 = []
    for i in range(3, len(liste), 3):
        liste2.append((liste[i-3], liste[i-2], liste[i-1]))
    return liste2

def produit(valmax, liste):
    """
    """
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
    liste2 = []
    for i in range(len(liste)):
        liste2.append([])
        for j in range(len(liste[i])):
            liste2[i].append(''.join(liste[j]))
    aaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhhhhhhmoncerveau
    return liste2

def ligne(x, y, liste, taille=1):
    """
    """
    for i in range(x):
        for j in range(y):
            print(liste[x][y])
            rectangle((i*taille), (j*taille), ((i+1)*taille) ,((j+1)*taille), remplissage=str(liste[x][y]))


        
def main():
    pass







if __name__  == "__main__":

    liste = traitement("P3.txt")
    
    liste = totext(liste)
    liste = suppression(liste)
    liste = backslash(liste)
    format, valmax, pixels = parametre(liste)
    x, y = forme(format)
    pixels = separation(pixels)                 #Doit check type de fichier
    pixels = separation2(pixels)               
    pixels = strtoint(pixels)
    pixels = totuple(pixels)
    
    
    pixels = produit(valmax, pixels)
    pixels = convertion(pixels)
    pixels = addition(pixels)
    
    if x < 100 and y < 100:
        cree_fenetre(x*100, y*100)
        """ligne(x, y, pixels, 100)"""
    else:
        cree_fenetre(x*10, y*10)
        """ligne(x, y, pixels, 10)"""
    print(pixels)
    attend_fermeture()