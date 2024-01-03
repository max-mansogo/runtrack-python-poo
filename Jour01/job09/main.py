
class Produit:
    def __init__(self, nom, prixHT, tva):
        self.nom = nom
        self.prixHT = prixHT
        self.tva = tva

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.tva)

    def afficherInformations(self):
        print("Nom : ", self.nom)
        print("Prix HT : ", self.prixHT)
        print("TVA : ", self.tva)

    def modifierNom(self, nouveauNom):
        self.nom = nouveauNom

    def modifierPrix(self, nouveauPrix):
        self.prixHT = nouveauPrix

    def obtenirNom(self):
        return self.nom

    def obtenirPrix(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.tva

# Créer des produits
produit1 = Produit("Produit 1", 10, 0.21)
produit2 = Produit("Produit 2", 20, 0.10)
produit3 = Produit("Produit 3", 30, 0.05)

# Calculer les prix avec TVA
prixTTC1 = produit1.calculerPrixTTC()
prixTTC2 = produit2.calculerPrixTTC()
prixTTC3 = produit3.calculerPrixTTC()

# Afficher les informations des produits
produit1.afficherInformations()
produit2.afficherInformations()
produit3.afficherInformations()

# Modifier le nom et le prix des produits
produit1.modifierNom("Nouveau Produit 1")
produit1.modifierPrix(15)

produit2.modifierNom("Nouveau Produit 2")
produit2.modifierPrix(25)

produit3.modifierNom("Nouveau Produit 3")
produit3.modifierPrix(35)

# Afficher les nouveaux prix des produits
print("Nouveau prix Produit 1 : ", produit1.calculerPrixTTC())
print("Nouveau prix Produit 2 : ", produit2.calculerPrixTTC())
print("Nouveau prix Produit 3 : ", produit3.calculerPrixTTC())
