


def traitement(file):
    """
    prend en parametre un fichier texte et retourne une liste contenant les lignes du fichier.
    """
    f = open(file, "r")
    liste = f.readlines()

    return liste

def check(liste):
    """
    """
    if liste[0] == "P3":
        return True
    return False
    

def totext(liste):
    """
    """
    liste2 = []
    for i in range(len(liste)):
        if '#' in liste[i]:
            liste2.append(commentaire(liste[i]))
    return liste2


def commentaire(texte):
    """
    """
    liste2=[]
    a = texte.find("#")
    for i in range(a):
        if "#" in texte: 
            liste2.append(texte[i])
    return liste2

def supression(liste):
    '''
    '''
    liste2 = []
    for elem in liste:
        if len(elem) != 0:
            for elems in elem:
                if elems != ' ':
                    liste2.append(elems)
    return liste2

def couple(liste):
    """
    """
    return liste.pop(0), liste.pop(0), "".join(liste) 

