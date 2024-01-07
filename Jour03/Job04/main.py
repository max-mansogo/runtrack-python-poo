
class Joueur:
    def __init__(self, nom, numero, position, buts_marques, passes_decisives, cartons_jaunes, cartons_rouges):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = buts_marques
        self.passes_decisives = passes_decisives
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = cartons_rouges

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom}:")
        print(f"Numéro: {self.numero}")
        print(f"Position: {self.position}")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, buts_marques, passes_decisives, cartons_jaunes, cartons_rouges):
        joueur.buts_marques += buts_marques
        joueur.passes_decisives += passes_decisives
        joueur.cartons_jaunes += cartons_jaunes
        joueur.cartons_rouges += cartons_rouges


'''Création des jouers et des équipes'''
joueur1 = Joueur("Jean", 10, "Attaquant", 5, 3, 1, 0)
joueur2 = Joueur("Pierre", 5, "Milieu de terrain", 2, 7, 2, 0)
joueur3 = Joueur("Paul", 3, "Défenseur", 0, 1, 3, 1)

equipe1 = Equipe("Équipe A")
equipe2 = Equipe("Équipe B")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)

'''Simulation d'un match'''
joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur2.recevoirUnCartonJaune()
joueur3.recevoirUnCartonRouge()

'''Statistiques des joueurs après le match'''
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
