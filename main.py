"""Petit programme de gestion pour musée en P.O.O
 idées et code ©Gabriel-D Pixel 2021"""

# imports
import time

# constantes
TARIFS = [
{
    "titre" : "1. Jeune de moins de 18 ans : 5€"
},
{
    "titre" : "2. Chômeur : 5 €"
},

{
    "titre" : "3. Classique : 11 €"
},
{
    "titre" : "4. Senior : 9,50 €"
}
]


# classes
class Kontroleur(object):
    def __init__(self):
        self.bonjour()
        self.tarifs = TARIFS["titre"]
    def bonjour(self):
        print("Bienvenue à l'outil de réservation du musée !")
        time.sleep(0.5)
        print("Veuillez choisir une option parmi les suivantes :")
        print(TARIFS)
        cmd = input("Saisir le nombre correspondant : ")
    """def confirmer_quitter(self, entrée):
        input("Êtes-vous sûr de votre choix ?")
        if entrée"""
if __name__ == "__main__":
    controleur = Kontroleur()
