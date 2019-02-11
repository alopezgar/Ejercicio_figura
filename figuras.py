class Forma():
    def __init__(self):
        pass

    def get_area(self):
        pass

    def get_perimetro(self):
        pass

class Cuadrado(Forma):
    def __init__(self,lado):
        self.lado = lado


    def get_area(self):
        area = self.lado*self.lado
        return area

    def get_perimetro(self):
        perimetro = 4*self.lado
        return perimetro


valor = Cuadrado(3)
print(valor.get_area())
