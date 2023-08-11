class punto:
    def __init__(self, Coordenada_X, Coordenada_Y) -> None:
        
        self.Coordenada_X=Coordenada_X
        self.Coordenada_Y=Coordenada_Y

        print(f"El punto en el plano cartesiano tiene las coordenadas ({Coordenada_X},{Coordenada_Y})")

    def mover(self):
        mover_puntoX=int(input("Digite las coordenadas que desea para el punto en el eje X:  "))
        mover_puntoY=int(input("Digite las coordenadas que desea para el punto en el eje Y:  "))
        print(f"Las nuevas coordenadas del punto son: ({mover_puntoX},{mover_puntoY})")

    
    
