from ast import main
from filecmp import cmp
from fltk import cree_fenetre, texte 


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
    liste = traitement(file)
    while liste[cmp] == "":
        cmp+=1
    if liste[cmp] == "P3\n":
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


def commentaire(texte):
    """
    """
    texte2 = ""
    a = texte.find("#")
    if a == 0:
        return ""
    else:
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
    liste2 = []
    for elem in liste:
        if "\n" in elem:
            liste2.append(elem[:len(elem) - 1])
        else:
            liste2.append(elem)
    return liste2

def main():
    pass                                # partie creation de fenetre


if __name__  == "__main__":

    liste = traitement("P3.txt")
    if check("P3.txt"):
        liste = totext(liste)
        liste = suppression(liste)
        print(backslash(liste))

    liste = traitement("P3.txt")
    if check("P3.txt"):
        liste = totext(liste)
        liste = suppression(liste)
        print(backslash(liste))