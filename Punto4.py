
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"El punto es {x,y}")

class Rectángulo:
    def __init__(self, punto1, punto2):
        self.esquina_sup_izq = punto1
        self.esquina_inf_der = punto2
       
        print(f"Las esquinas son: esquina superior izquierda {punto1} y esquina inferior derecha {punto2}")

 



    
        


    

        

