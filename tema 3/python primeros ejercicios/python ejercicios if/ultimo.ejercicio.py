dia = float(input("introduce el dia:"))
mes = float(input("introduce el mes:"))
año = float(input("introduce el año:"))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0): 
    if mes <= 12:
        if ((dia <= 31 and mes == 1) and (dia <= 31 and mes == 3) and (dia <= 31 and mes == 5) and (dia <= 31 and mes == 7) and (dia <= 31 and mes == 8) and (dia <= 31 and mes == 10) and (dia <= 31 and mes == 12)) or (dia <= 29 and mes == 2) or ((dia <=30 and mes ==4) and (dia <=30 and mes ==6) and (dia <=30 and mes ==9) and (dia <=30 and mes ==11)):
            print("introduce un dia correcto")            
        else: 
            print("introduce un dia correcto")
    else:
          print ("introduce un mes valido")
    if mes > 12:
        if ((dia <= 31 and mes == 1) and (dia <= 31 and mes == 3) and (dia <= 31 and mes == 5) and (dia <= 31 and mes == 7) and (dia <= 31 and mes == 8) and (dia <= 31 and mes == 10) and (dia <= 31 and mes == 12)) or ((dia <=30 and mes ==4) and (dia <=30 and mes ==6) and (dia <=30 and mes ==9) and (dia <=30 and mes ==11)):
            print("introduce un dia valido")            
        else: 
            print("introduce un dia valido")
    else:
        print ("introduce un mes valido")