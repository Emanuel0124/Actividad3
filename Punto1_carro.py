class carro:
    def __init__(self, velocidad_maxima, kilometraje) -> None:
        
        self.velocidad_maxima=velocidad_maxima
        self.kilometraje=kilometraje

        print(f"El automovil posee {kilometraje} kilometros recorridos y alcanza los {velocidad_maxima} Km/h ")