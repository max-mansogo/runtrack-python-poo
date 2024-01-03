
class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Mouvements: haut, bas, droite et gauche
    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y -= 1

    def haut(self):
        self.y += 1

    #Coordonnées en tuples 
    def position(self):
        return (self.x, self.y)


