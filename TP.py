import random

def ingresoProductor(): #falta presentacion
    nombreApellido=input("Ingrese su nombre y apellido: ")
    dni=validarRango(10000000,99999999,"Ingrese su dni: ")
    

def validarRango(desde,hasta,texto):
    valor=int(input(texto))
    while valor>hasta or valor<desde:
        print("Rango invalido")
        valor=int(input(texto))
    return valor

def ingresoCliente(LiDNI,cont,LiMo,LiAu,LiCa,LiMod,LiVa):
    nombreApellido=input("Ingrese su nombre y apellido: ")
    Auxdni=validarRango(10000000,99999999,"Ingrese su dni: ")
    if busqueda(LiDNI,Auxdni) != -1:
        print("DNI DUPLICADO")
        Auxdni=validarRango(10000000,99999999,"Ingrese su dni: ")
    else:
        LiDNI.append(Auxdni)
        print("el nro de cliente es: ",1+cont)
        print("")
        
        opcion=validarRango(1,3, "Ingrese 1 si el tipo de vehiculo es una moto, ingrese 2 si es un auto y 3 si es un camion")
        azar=random.randint(0,5)
        if opcion==1:
            print("el modelo de vehiculo es el: ",LiMo[azar])
            LiMod.append(LiMo[azar])
            LiVa.append(random.randint(1000000,4000000))
            print("el precio del vehiculo es: $",LiVa[cont])
        elif opcion==2:
            print("el modelo de vehiculo es el: ",LiAu[azar])
            LiMod.append(LiAu[azar])
            LiVa.append(random.randint(5000000,10000000))
            print("el precio del vehiculo es: $",LiVa[cont])
        else:
            print("el modelo de vehiculo es el: ",LiCa[azar])
            LiMod.append(LiCa[azar])
            LiVa.append(random.randint(8000000,13000000))
            print("el precio del vehiculo es: $",LiVa[cont])
#carga lista dni, modelo y el precio


def cotizacion(LiVa,LiEm,cont,LiPa):
    auxval=LiVa[cont]*0.005
    
    opcion=validarRango(1,3, "Ingrese 1 si el tipo de seguro es contra tercero, 2 contra tercero completo y 3 para todo riesgo")
    
    if opcion == 1:
        calculo=auxval*1.005
        print("cotizacion: contra tercero")
        print("")
        print("->empresa 1: $",round(calculo*1.008,0))
        print("->empresa 2: $",round(calculo*1.014,0))
        print("->empresa 3: $",round(calculo*1.011,0))
        opcionem=validarRango(1,3, "elija tipo de empresa (1,2,3): ")
        if opcionem == 1:
            pagomen=round(calculo*1.08,0)

        elif opcionem == 2:
            pagomen=round(calculo*1.14,0)

        else:
            pagomen=round(calculo*1.11,0)

            
    elif opcion == 2:
        calculo=auxval*1.010
        print("cotizacion: contra tercero completo")
        print("")
        print("->empresa 1: $",round(calculo*1.022,0))
        print("->empresa 2: $",round(calculo*1.017,0))
        print("->empresa 3: $",round(calculo*1.020,0))
        print("")
        opcionem=validarRango(1,3, "elija tipo de empresa (1,2,3): ")
        if opcionem == 1:
            pagomen=round(calculo*1.22,0)

        elif opcionem == 2:
            pagomen=round(calculo*1.17,0)

        else:
            pagomen=round(calculo*1.10,0)

            
    else:
        calculo=auxval*1.020
        print("cotizacion: todo riesgo")
        print("")
        print("->empresa 1: $",round(calculo*1.024,0))
        print("->empresa 2: $",round(calculo*1.027,0))
        print("->empresa 3: $",round(calculo*1.033,0))
        print("")
        opcionem=validarRango(1,3, "elija tipo de empresa (1,2,3): ")
        if opcionem == 1:
            pagomen=round(calculo*1.24,0)

        elif opcionem == 2:
            pagomen=round(calculo*1.27,0)

        else:
            pagomen=round(calculo*1.33,0)

        
    LiEm.append(opcionem)
    LiPa.append(pagomen)
    
    print(LiEm[cont])
    print(LiPa[cont])
            

    
        
    
    
    
 
    
    
    
        
        
        
        
        
        
           
def busqueda (lista,valor):
    pos = -1
    i = 0
    while (pos == -1) and (i<len(lista)):
        if (lista[i] == valor):
            pos = i
        i+=1
    return pos

    

    
def main():
    
    dni=[]
    motos=["moto: Harley-Davidson Road Glide Special", "Ducati Panigale V4", "BMW R 1250 GS ", "Kawasaki Ninja ZX-10R", "Yamaha MT-07", "Honda CRF450R"]
    autos=["Toyota Corolla", "Honda Civic", "Ford Mustang", "Chevrolet Silverado", "Tesla Model 3", "BMW Serie 3"]
    camion=["Scania R Series", "Mercedes-Benz Actros", "Volvo FH16", "MAN TGX", "Freightliner Cascadia", "DAF XF"]
    modelo=[]
    valorVehiculo=[]
    empresas=[]
    nrocli=0
    pagoxmes=[]
    tipoSeguro=[]

    ingresoProductor()
    opcion=validarRango(1,3, "Por favor, ingrese 1 para cargar datos de clientes, 2 para ver listas o 3 para generar informe y salir: ")
    
    while opcion != 3:
        if opcion==1:
            
            ingresoCliente(dni,nrocli,motos,autos,camion,modelo,valorVehiculo)
            cotizacion(valorVehiculo,empresas,nrocli,pagoxmes)
            nrocli+=1
        opcion=validarRango(1,3, "Por favor, ingrese 1 para cargar datos de clientes, 2 para ver listas o 3 para generar informe y salir: ")
            

if __name__ == "__main__":
    main()
