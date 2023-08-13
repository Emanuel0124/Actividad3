class carta:
    Pintas=("Corazones", "Diamantes", "Tréboles", "Picas")
    Valor=(1,2,3,4,5,6,7,8,9,10,"J","Q","K","A")
    
    def __init__(self, valor, pinta) -> None:
        self.valor=valor
        self.pinta=pinta
