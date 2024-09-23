""" Importe le module des chaînes de caractères et celui du code de la chaîne de caractères"""
import unicodedata
import string
#debut des fonctions

def ispalindrome(p):
    """
    Vérifie si une phrase ou un mot est un palindrome, 
    en ignorant les accents, la ponctuation, les espaces et la casse.
    """
    # Convertir en minuscules
    p = p.lower()

    # Supprimer les accents
    p = ''.join(
        char for char in unicodedata.normalize('NFD', p)
        if unicodedata.category(char) != 'Mn'
    )

    # Supprimer la ponctuation et les espaces
    p = p.translate(str.maketrans('', '', string.punctuation + ' '))

    # Comparer la chaîne avec son inverse
    return p == p[::-1]
#regarde si le mot est un palindrome



def main():
    """tests si les mots sont des palindromes"""

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))
#renvoie le mot et s'il est un palindrome


if __name__ == "__main__":
    main()
#fin
