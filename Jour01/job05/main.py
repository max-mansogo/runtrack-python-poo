
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Les coordonnées du point sont: ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La valeur de x est {self.x}")

    def afficherY(self):
        print(f"La valeur de y est {self.y}")

    def changerX(self, newX):
        self.x = newX

    def changerY(self, newY):
        self.y = newY