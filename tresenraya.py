class Juego:
    
    def __init__(self):
        self.matriz=[["","",""],
                     ["","",""],
                     ["","",""]]
        
    def imprimirtablero(self):
        for i in range (0, 3):
            print (f"{self.matriz[i]}\n")
            
    def jugador1(self):
        while True:
            columna = int(input("dime el numero de columna, juegas con 0"))
            fila =  int(input("dime el numero de fila, juegas con 0"))
            if self.matriz[fila-1][columna-1] == "X" or self.matriz[fila-1][columna-1] == 0:
                print("ese espacio ya esta ocupado")
                for i in range (0, 3):
                    print (f"{self.matriz[i]}\n")
            else: 
                self.matriz[fila-1][columna-1] = 0
                for i in range (0, 3):
                    print (f"{self.matriz[i]}\n")
                break
            
    def jugador2(self):
        while True:
            columna = int(input("dime el numero de columna, juegas con X"))
            fila =  int(input("dime el numero de fila, juegas con X"))
            if self.matriz[fila-1][columna-1] == "X" or self.matriz[fila-1][columna-1] == 0:
                print("ese espacio ya esta ocupado")
                for i in range (0, 3):
                    print (f"{self.matriz[i]}\n")
            else:
                self.matriz[fila-1][columna-1] = "X"
                for i in range (0, 3):
                    print (f"{self.matriz[i]}\n")
                break
            
    def Cvictoria(self):
        if (self.matriz[0][0] == self.matriz[1][1] and self.matriz[0][0] == self.matriz[2][2]) or (self.matriz[0][0] == self.matriz[0][1] and self.matriz[0][0] == self.matriz[0][2]) or (self.matriz[0][0] == self.matriz[1][0] and self.matriz[0][0] == self.matriz[2][0]):
            if self.matriz[0][0] == 0:
                print("gana jugador 1")
                return True
            elif self.matriz[0][0] == "X":
                print("gana jugador 2")
                return True
        if (self.matriz[1][0] == self.matriz[1][1] and self.matriz[1][0] == self.matriz[1][2]):
            if self.matriz[1][0] == 0:
                print("gana jugador 1")
                return True
            elif self.matriz[1][0] == "X":
                print("gana jugador 2")
                return True
        if (self.matriz[1][1] == self.matriz[0][1] and self.matriz[1][1] == self.matriz[2][1]):
            if self.matriz[1][1] == 0:
                print("gana jugador 1")
                return True
            elif self.matriz[1][1] == "X":
                print("gana jugador 2")
                return True
        if (self.matriz[0][2] == self.matriz[1][2] and self.matriz[0][2] == self.matriz[2][2]):
            if self.matriz[0][2] == 0:
                print("gana jugador 1")
                return True
            elif self.matriz[0][2] == "X":
                print("gana jugador 2")
                return True
        if (self.matriz[2][0] == self.matriz[1][1] and self.matriz[2][0] == self.matriz[0][2]) or (self.matriz[2][0] == self.matriz[2][1] and self.matriz[2][0] == self.matriz[2][2]):
            if self.matriz[2][0] == 0:
                print("gana jugador 1")
                return True
            elif self.matriz[2][0] == "X":
                print("gana jugador 2")
                return True
  
class Loop:
    def __init__(self, victoria, contador):
        self.victoria = victoria
        self.contador = contador
        self.juga1 = 0
        self.juga2 = 0
        
    
    def bucle(self):
        jg1=Juego()
        jg1.imprimirtablero()
        while True:  
            self.victoria = jg1.Cvictoria()
            if self.victoria == True or contador == 9:
                self.juga2 += 1
                break
            jg1.jugador1()
            self.victoria = jg1.Cvictoria()
            if self.victoria == True or contador == 9:
                self.juga1 += 1
                break
            jg1.jugador2()
            
    def tabladepuntajes(self):
        print(f"\n victorias del jugador 1(0): {self.juga1}" f"\n victorias del jugador 2(X): {self.juga2}")

decision = "si"
victoria = False
contador = 0
juego1 = Loop(victoria, contador)
while decision != "no":
    juego1.bucle()
    juego1.tabladepuntajes()
    decision = input("deseas jugar devuelta?")
    