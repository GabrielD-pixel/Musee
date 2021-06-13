"""Petit programme de gestion pour musée en P.O.O
 idées et code ©Gabriel-D Pixel 2021"""

# imports
import time


# classes
class Kontroleur(object):
    def __init__(self):
        self.TARIFS = [
            {
                "titre": "Jeune de moins de 18 ans : 5€"
            },
            {
                "titre": "Chômeur : 5 €"
            },

            {
                "titre": "Classique : 11 €"
            },
            {
                "titre": "Senior : 9,50 €"
            }
        ]

    def bonjour(self):
        print("Bienvenue à l'outil de réservation du musée !")
        time.sleep(0.5)
        print("Veuillez choisir une option parmi les suivantes :")
        for number, titre in enumerate(self.TARIFS, start=1):
            titre = titre["titre"]
            print(f"{number}. {titre}")
        cmd = input("Saisir le nombre correspondant : ")
        if self.tester_tarif(cmd):
            print("Erreur !")
        if self.confirmer_quitter(cmd):
            print("Hello world")
        else:
            print("Abandon de l'action")
    def confirmer_quitter(self, entree):
        trouc = input(f"Êtes-vous sûr de votre choix du tarif {entree} (o pour oui et n pour non) ? ")
        if trouc == "o":
            return True
        else:
            return False
    def tester_tarif(self, entree):
        num = int(entree)
        if num < 1 or num > 4:
            return True
        return False
if __name__ == "__main__":
    controleur = Kontroleur()
    controleur.bonjour()