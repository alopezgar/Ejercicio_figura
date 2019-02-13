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

class Rectangulo(Forma):
    def __init__(self,lado1,lado2):
        self.lado1 = lado1
        self.lado2 = lado2
     
    def get_area(self):
        area = lado1 * lado2
        return area
    
    def get_perimetro(self):
        perimetro = 2*lado1 + 2*lado2
        return perimetro
    
 class Circulo(Forma):
    def __init__(self,radio):
        self.radio = radio
    
    def get_area(self):
        area = math.pi*radio**2
        return area
    def get_perimetro(self):
        perimetro = 2*math.pi*radio
        return perimetro

a = Cuadrado(3)
print(a.get_area())
print(a.get_perimetro())

b = Rectangulo(3,4)
print(b.get_area())
print(b.get_perimetro())

c = Circulo(2)
print(c.get_area())
print(c.get_perimetro())
