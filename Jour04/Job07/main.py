
import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()
        self.joueur_main = []
        self.croupier_main = []

    def creer_paquet(self):
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def calculer_total(self, main):
        total = 0
        as_present = False

        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                as_present = True
                total += 1
            else:
                total += int(carte.valeur)

        if as_present and total + 10 <= 21:
            total += 10

        return total

    def distribuer_cartes_initiales(self):
        self.joueur_main = [self.paquet.pop(), self.paquet.pop()]
        self.croupier_main = [self.paquet.pop(), self.paquet.pop()]

    def afficher_main(self, joueur=True):
        if joueur:
            print("Main du joueur :")
            for carte in self.joueur_main:
                print(f"{carte.valeur} de {carte.couleur}")
            print(f"Total : {self.calculer_total(self.joueur_main)}")
        else:
            print("Main du croupier :")
            print(f"{self.croupier_main[0].valeur} de {self.croupier_main[0].couleur}")
            print("Carte cachée")
            print(f"Total : {self.calculer_total([self.croupier_main[0]])}")

    def joueur_tirer_carte(self):
        self.joueur_main.append(self.paquet.pop())

    def croupier_jouer(self):
        while self.calculer_total(self.croupier_main) < 17:
            self.croupier_main.append(self.paquet.pop())

    def verifier_gagnant(self):
        total_joueur = self.calculer_total(self.joueur_main)
        total_croupier = self.calculer_total(self.croupier_main)

        if total_joueur > 21 or (total_croupier <= 21 and total_croupier > total_joueur):
            return "Le croupier gagne."
        elif total_croupier > 21 or (total_joueur <= 21 and total_joueur > total_croupier):
            return "Le joueur gagne."
        else:
            return "Égalité, match nul."

# Exemple d'utilisation
jeu_blackjack = Jeu()
jeu_blackjack.distribuer_cartes_initiales()
jeu_blackjack.afficher_main()

while True:
    choix = input("Voulez-vous tirer une carte ? (Oui/Non) ").lower()
    if choix == "oui":
        jeu_blackjack.joueur_tirer_carte()
        jeu_blackjack.afficher_main()
        if jeu_blackjack.calculer_total(jeu_blackjack.joueur_main) > 21:
            print("Le joueur a dépassé 21. Le croupier gagne.")
            break
    else:
        jeu_blackjack.croupier_jouer()
        jeu_blackjack.afficher_main(joueur=False)
        print(jeu_blackjack.verifier_gagnant())
        break
