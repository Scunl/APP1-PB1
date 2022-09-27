import argparse
from filecmp import cmp
from fltk import attend_fermeture, cree_fenetre, mise_a_jour, rectangle

def traitement(file):
    """
    prend en parametre un fichier texte et retourne une liste contenant les lignes du fichier.
    """
    f = open(file, "r")
    liste = f.readlines()
    liste = totext(liste)
    return liste


def check(file):
    """
    """
    cmp = 0
    file = backslash(liste)
    while liste[cmp] == "":
        cmp+=1

    return str(liste[cmp])
    
    

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


def parametre(liste, type):
    '''
    '''
    pixels = []
    format = liste[1]
    if type == "P3":

        valmax = int(liste[2])
        for i in range(3, len(liste)):
            pixels.append(liste[i])
        return (format, valmax, pixels)

    if type == "P1":
        for i in range(2, len(liste)):
            pixels.append(liste[i])
        
        return pixels, format
    

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
            if len(caractere) > 0:
                liste.append(int(caractere))
    return liste


def strtoint1(pixels):
    liste = []
    for elem in pixels:
        for caractere in elem:
            if caractere != " ":
                liste.append(int(caractere))
    return liste


def totuple(liste):
    """
    """
    liste2 = []
    for i in range(3, len(liste) + 3, 3):
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
    liste2 = []
    for i in range(len(liste)):
        liste2.append(''.join('{:02X}'.format(a) for a in liste[i]))
    return liste2


def addition(liste):
    '''
    '''
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
    liste2 = []
    for i in range(len(liste)):
        liste2.append(''.join(liste[i]))
    return liste2


def ligne(x, y, liste, miseajour=False, taille=1):
    """
    """
    cmpt = 0
    for i in range(y):
        for j in range(x):
            rectangle((j*taille), (i*taille), ((j+1)*taille) ,((i+1)*taille), remplissage='#' + str(liste[cmpt]), epaisseur=0)
            cmpt += 1
            if miseajour:
                mise_a_jour()
    return None

def ligne1(x, y, liste, miseajour=False, taille=1):
    """
    """
    cmpt = 0
    for i in range(y):
        for j in range(x):
            if liste[cmpt] == 0:
                rectangle((j*taille), (i*taille), ((j+1)*taille) ,((i+1)*taille), remplissage='White', epaisseur=0)
            else:
                rectangle((j*taille), (i*taille), ((j+1)*taille) ,((i+1)*taille), remplissage='Black', epaisseur=0)
            cmpt += 1
            if miseajour:
                mise_a_jour()
    return None


"""
def parametrep1(liste: list) -> tuple:
    pixels = []
    px = liste[0]
    format = liste[1]
    for i in range(3, len(liste)):
        pixels.append(liste[i])
    return (px, format, pixels)

>>>> Fonction a inserer <<<<
"""

def binaire(liste):
    liste2 = []
    for i in range(2, len(liste)):
        liste2.append(liste[i])
    return liste2

def p2(liste):
    """
    """
    return [(liste[i], liste[i], liste[i]) for i in range(len(liste))]

if __name__  == "__main__":
    
    parser = argparse.ArgumentParser(prog='app1-pb1-106',
                                    description='Affiche des images PPM')
    parser.add_argument('fichier', help='Selectionner des images sous format PPM (3, 2 ou 1)')     
    parser.add_argument('--mise_a_jour', type=bool, default=False,
                                    help='Affiche image px par px')

    args = vars(parser.parse_args())
    miseajour = args['mise_a_jour']
    liste = traitement(args['fichier'])
    liste = totext(liste)
    liste = suppression(liste)
    liste = backslash(liste)

    if check(args['fichier']) == "P3" or check(args['fichier']) == "P2":
        format, valmax, pixels = parametre(liste, "P3")
        x, y = forme(format)
        pixels = separation(pixels)                 #Doit check type de fichier
        pixels = separation2(pixels)               
        pixels = strtoint(pixels)

        if check(args['fichier']) == "P2":
            pixels = p2(pixels)
        else:
            pixels = totuple(pixels)
        pixels = produit(valmax, pixels)
        pixels = convertion(pixels)
        pixels = addition(pixels)
        pixels = addition2(pixels)
        if x < 100 and y < 100:
            cree_fenetre(x*10, y*10)
            ligne(x, y, pixels, miseajour=miseajour, taille=10)
        else:
            cree_fenetre(x, y)
            ligne(x, y, pixels, miseajour=miseajour)

    if check(args['fichier']) == "P1":

        pixels, format = parametre(liste, 'P1')
        a, b = liste[0], liste[1]
        a = b.split(" ")
        liste2 = []
        for elem in a:
            liste2.append(int(elem))
        x, y = liste2[0], liste2[1]
        if x <= 50 or y <= 50:
            cree_fenetre(x*10, y*10)
        else:
            cree_fenetre(x, y)
        pixels = binaire(liste)
        liste = strtoint1(pixels)
        ligne1(x, y, liste, miseajour=miseajour)

    attend_fermeture()