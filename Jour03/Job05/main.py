
class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        '''les points de vie de l'adversaire se réduisent de un'''
        adversaire.vie -= 1

class Jeu:
    def __init__(self):
        self.niveau = None
    
    def choisirNiveau(self):
        self.niveau = input("Choisissez le niveau de difficulté : ")
    
    def lancerJeu(self):
        '''Instancier les objets Personnage en fonction du niveau choisi'''
        if self.niveau == "facile":
            joueur = Personnage("Joueur", 10)
            ennemi = Personnage("Ennemi", 5)
        elif self.niveau == "moyen":
            joueur = Personnage("Joueur", 8)
            ennemi = Personnage("Ennemi", 8)
        elif self.niveau == "difficile":
            joueur = Personnage("Joueur", 5)
            ennemi = Personnage("Ennemi", 10)
        else:
            print("Niveau invalide.")
            return
        
        '''Déroulement de la partie'''
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)
        
        '''Vérification du vainqueur '''
        if joueur.vie > 0:
            print("Le joueur a gagné !")
        else:
            print("L'ennemi a gagné !")

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
