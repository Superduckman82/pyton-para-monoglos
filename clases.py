class coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        self.gasofa = 5
        self.arrancao = False

        

    def arrancar(self):
        if self.gasofa > 0:
            self.arrancao = True


    

    def color(self, colorn):
        self.color = colorn

micoche = coche("mercedes","negro")
micoche.arrancar()

print("Esta arrancao? " + str(micoche.arrancao))

            
