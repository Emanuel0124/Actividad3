class Cuenta_Bancaria:
    def __init__(self,numero_cuenta,propietarios, balance) -> None:
      
        
        
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    
        print(f"Su numero de cuenta es {numero_cuenta} , los propietarios son {propietarios} y el balance inicial de su cuenta es {balance}")

