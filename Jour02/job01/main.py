
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Creer un objet rectangle avec les valeurs initiales
rectangle = Rectangle(10, 5)

# Modifier la longitude et la latitude
rectangle.set_longueur(15)
rectangle.set_largeur(8)

# Verification de changements
print("Longitude:", rectangle.get_longueur())
print("Latitude:", rectangle.get_largeur())
