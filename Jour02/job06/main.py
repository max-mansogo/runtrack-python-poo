
class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": self.__statut_commande}

    def annuler_commande(self):
        self.__statut_commande = "annulée"

    def __calculer_total(self):
        total = 0
        for plat in self.__plats_commandes.values():
            total += plat["prix"]
        return total

    def afficher_commande(self):
        total = self.__calculer_total()
        print("Commande n°", self.__numero_commande)
        for nom_plat, plat in self.__plats_commandes.items():
            print(nom_plat, "-", plat["prix"], "€")
        print("Total à payer:", total, "€")

    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * taux_tva / 100
        return tva

# Création d'une commande
commande = Commande(1)

# Ajout de plats à la commande
commande.ajouter_plat("Pizza Margherita", 10)
commande.ajouter_plat("Salade César", 8)
commande.ajouter_plat("Tiramisu", 5)

# Annulation de la commande
commande.annuler_commande()

# Affichage de la commande
commande.afficher_commande()

# Calcul de la TVA
tva = commande.calculer_tva(20)
print("TVA:", tva, "€")
