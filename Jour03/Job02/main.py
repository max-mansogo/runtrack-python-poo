
class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = False

    def afficher(self):
        print("Détails du compte:")
        print("Numéro de compte:", self.__numero_compte)
        print("Nom:", self.__nom)
        print("Prénom:", self.__prenom)
        print("Solde:", self.__solde)

    def afficherSolde(self):
        print("Solde du client:", self.__solde)

    def versement(self, montant):
        self.__solde += montant

    def retrait(self, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            print("Nouveau solde:", self.__solde)
        else:
            print("Montant indisponible. Opération annulée.")

    def agios(self):
        if self.__solde < 0:
            self.__solde -= self.__solde * 0.05
            print("Agios appliqués. Nouveau solde:", self.__solde)

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement effectué avec succès.")
        else:
            print("Montant indisponible. Virement annulé.")


compte1 = CompteBancaire("123456789", "Dupont", "Jean", 1000)

compte1.afficher()

compte1.afficherSolde()

compte1.versement(500)

compte1.retrait(200)

'''Application des agios'''
compte1.agios()

'''Création d'un compte bancaire à découvert'''
compte2 = CompteBancaire("987654321", "Martin", "Sophie", -500)

compte1.virement(compte2, 700)
