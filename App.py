from Punto1_carro import carro
from Punto2_y_3_plano import punto
from Punto4 import Rectángulo
from Punto4 import Punto
from Punto5 import circulo
from Punto7 import Cuenta_Bancaria

Vehiculo_1=carro("200", "1500")
Punto_plano=punto(2,8)
Punto_plano2=punto(6,4)
Punto_plano.mover()

circulo_1=circulo((2,4),4)
circulo_1.area()
circulo_1.perimetro()
numero_cuenta=int(input("Escriba su numero de cuenta: "))
propietarios=str(input("Escriba los propiestarios de la cuenta: "))
balance=int(input("Ingrese el balance de su cuenta: "))
Cuenta1=Cuenta_Bancaria(numero_cuenta,propietarios,balance)