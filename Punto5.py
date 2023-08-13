class circulo:
    def __init__(self,centro, radio) -> None:
        self.centro=centro
        self.radio=radio

        print(f"El centro está en {centro} y el radio mide {radio}")

    def area(self):
        area_circulo=3.14*(self.radio*self.radio)
        print(f"El area del circulo es: {area_circulo}")

    def perimetro(self):
        perimetro_circulo=2*3.14*self.radio
        print(f"El perimetro del circulo es: {perimetro_circulo}")
    
    

