
class Circle:
    def __init__(self, radio):
        self.radio = radio

    def changerRayon(self, new_radio):
        self.radio = new_radio
        '''changer le rayon'''

    def afficherInfos(self):
        print("Information du circle:")
        print("Radio:", self.radio)
        print("Circonférence:", self.circonférence())
        print("Diametre:", self.diametre())
        print("Area:", self.area())
        '''Afficher plus d'info sur les circles'''

    def circonférence(self):
        return 2 * 3.1416 * self.radio
    '''Calcule de la circonférence'''

    def diametre(self):
        return 2 * self.radio
    '''Calcul du rayon'''

    def area(self):
        return 3.1416 * self.radio ** 2
    '''Calcule de la superfice'''


# Creer deux circles de radios 4 y 7
circulo1 = Circle(4)
circulo2 = Circle(7)

# Plus sur les Circles
circulo1.afficherInfos()
circulo2.afficherInfos()
