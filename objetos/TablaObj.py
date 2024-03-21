class TablaObj:

    def __init__(self, tabla):
        self.tabla = tabla
        self.multiplicador = 0

    def __repr__(self):
        return 
    
    def multiplicar(self):
        for i in range (1, 11):
            print (f"{self.tabla} * {i} = {self.tabla * i}")

    def preguntas(self):
        for i in range (1, 11):
            if int(input(f"cuanto es {self.tabla} * {i}?")) == self.tabla * i:
                print("acertaste")
            else:
                print("fallaste")

        
tabla = int(input("dime de que numero quieres que sea la tabla?"))
tabla1 = TablaObj(tabla)
tabla1.multiplicar()
tabla1.preguntas()

