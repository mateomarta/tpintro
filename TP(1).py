import random

#Funciones genericas:
def validarRango(desde,hasta,texto):
    valor=int(input(texto))
    while valor>hasta or valor<desde:
        print("Rango invalido")
        valor=int(input(texto))
    return valor

def busqueda (lista,valor):
    pos = -1
    i = 0
    while (pos == -1) and (i<len(lista)):
        if (lista[i] == valor):
            pos = i
        i+=1
    return pos

##############################################
def ingresoProductor(): #falta presentacion
    nombreApellido=input("Ingrese su nombre y apellido: ")
    dni=validarRango(10000000,99999999,"Ingrese su dni: ")

def ingresoCliente(LiDNI,cont,LiMo,LiAu,LiCa,LiMod,LiVa):
    #Ingreso y validacion del DNI (por rango y duplicado)
    nombreApellido=input("Ingrese su nombre y apellido: ")
    Auxdni=validarRango(10000000,99999999,"Ingrese su dni: ")
    while busqueda(LiDNI,Auxdni) != -1:
        print("DNI DUPLICADO")
        Auxdni=validarRango(10000000,99999999,"Ingrese su dni: ")
    LiDNI.append(Auxdni)
    #
    print("el nro de cliente es: ",1+cont)
    print("")
    #Ingreso tipo de veiculo
    opcion=validarRango(1,3, "Ingrese 1 si el tipo de vehiculo es una moto, ingrese 2 si es un auto y 3 si es un camion")
    #Se asigna un modelo y valor random en base al tipo de vehiculo
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
    auxval=LiVa[cont]*0.001
    #Elegir tipo de seguro
    opcion=validarRango(1,3, "Ingrese 1 si el tipo de seguro es contra tercero, 2 contra tercero completo y 3 para todo riesgo")
    #En base al tipo de seguro se imprime el coste que tendria segun cada empresa
    #El primer if representa el tipo de seguro, el segundo if la empresa
    if opcion == 1:
        auxval = auxval * 5
        print("cotizacion: contra tercero")
        print("")
        print("->empresa 1: $",round(auxval*1,0))
        print("->empresa 2: $",round(auxval*1.25,0))
        print("->empresa 3: $",round(auxval*1.5,0))
        opcionem=validarRango(1,3, "elija tipo de empresa (1,2,3): ")
        if opcionem == 1:
            pagomen=round(auxval*1,0)
        elif opcionem == 2:
            pagomen=round(auxval*1.25,0)
        else:
            pagomen=round(auxval*1.5,0)
    elif opcion == 2:
        auxval = auxval * 7
        print("cotizacion: contra tercero completo")
        print("")
        print("->empresa 1: $",round(auxval*1.5,0))
        print("->empresa 2: $",round(auxval*1,0))
        print("->empresa 3: $",round(auxval*1.25,0))
        print("")
        opcionem=validarRango(1,3, "elija tipo de empresa (1,2,3): ")
        if opcionem == 1:
            pagomen=round(auxval*1.5,0)
        elif opcionem == 2:
            pagomen=round(auxval*1,0)
        else:
            pagomen=round(auxval*1.25,0)
    else:
        auxval = auxval * 13
        print("cotizacion: todo riesgo")
        print("")
        print("->empresa 1: $",round(auxval*1.25,0))
        print("->empresa 2: $",round(auxval*1.5,0))
        print("->empresa 3: $",round(auxval*1,0))
        print("")
        opcionem=validarRango(1,3, "elija tipo de empresa (1,2,3): ")
        if opcionem == 1:
            pagomen=round(auxval*1.25,0)
        elif opcionem == 2:
            pagomen=round(auxval*1.5,0)
        else:
            pagomen=round(auxval*1,0)
    #Una vez elegida una opcion, se guarda la empresa y el pago por mes en las listas
    LiEm.append(opcionem)
    LiPa.append(pagomen)
    #PROVICIONAL: se imprime el valor recien cargado para verificar
    print(LiEm[cont])
    print(LiPa[cont])
    
##############################################
def main():
    #Preinicializacion de listas:
        #Listas con los modelos
    motos=["moto: Harley-Davidson Road Glide Special", "Ducati Panigale V4", "BMW R 1250 GS ", "Kawasaki Ninja ZX-10R", "Yamaha MT-07", "Honda CRF450R"]
    autos=["Toyota Corolla", "Honda Civic", "Ford Mustang", "Chevrolet Silverado", "Tesla Model 3", "BMW Serie 3"]
    camion=["Scania R Series", "Mercedes-Benz Actros", "Volvo FH16", "MAN TGX", "Freightliner Cascadia", "DAF XF"]
    ##########################################
        #Listas con los datos de los clientes
    dni=[]
    modelo=[]
    valorVehiculo=[]
    empresas=[]
    pagoxmes=[]
    ##########################################
    #Contador para saber posicion de la lista que esta siendo cargada en cada momento
    nrocli=0
    #Mensaje de vienvenida del programa
    ingresoProductor()
    #While principal
    #Condicion de finalizacion del while main -> variable opcion
    opcion=validarRango(1,3, "Por favor, ingrese 1 para cargar datos de clientes, 2 para ver listas o 3 para generar informe y salir: ")
    while opcion != 3:
        if opcion==1:
            ingresoCliente(dni,nrocli,motos,autos,camion,modelo,valorVehiculo)
            cotizacion(valorVehiculo,empresas,nrocli,pagoxmes)
            #Luego de completar la carga incrementa el contador de posicion
            nrocli+=1
        #Finalizacion del ciclo while, nuevamente condicion de finalizacion
        opcion=validarRango(1,3, "Por favor, ingrese 1 para cargar datos de clientes, 2 para ver listas o 3 para generar informe y salir: ")    

if __name__ == "__main__":
    main()
