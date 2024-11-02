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
    print("*** PROGRAMA SEGUROS AUDE ***")
    print("_____________________________")
    nombreApellido=input("Ingrese su nombre y apellido: ")
    dni=validarRango(10000000,99999999,"Ingrese su dni: ")
    print("")
    print("->Iniciando sesion y validando cuenta<-")
    print("==========================================================================")
    print("	<<<<		BIENVENIDO AL PROGRAMA 			>>>>")
    print("==========================================================================")
    print("")
######
def ingresoCliente(LiDNI,cont,LiMo,LiAu,LiCa,LiMod,LiVa):
    #Ingreso y validacion del DNI (por rango y duplicado)
    nombreApellido=input("Ingrese nombre y apellido del cliente: ")
    Auxdni=validarRango(10000000,99999999,"Ingrese dni del cliente: ")
    while busqueda(LiDNI,Auxdni) != -1:
        print("DNI ya registrado, si desea ingresar un nuevo vehiculo para el mismo dni inicie sesion nuevamente")
        Auxdni=validarRango(10000000,99999999,"Ingrese su dni: ")
    LiDNI.append(Auxdni)
    #
    print("El nro de cliente es: ",1+cont)
    print("")
    #Ingreso tipo de veiculo
    opcion=validarRango(1,3, "Ingrese 1 si el tipo de vehiculo es una moto, ingrese 2 si es un auto y 3 si es un camion: ")
    #Se asigna un modelo y valor random en base al tipo de vehiculo
    azar=random.randint(0,5)
    if opcion==1:
        print("El modelo de vehiculo es el: ",LiMo[azar])
        LiMod.append(LiMo[azar])
        LiVa.append(random.randint(1000000,4000000))
        print("El precio del vehiculo es: $",LiVa[cont])
    elif opcion==2:
        print("El modelo de vehiculo es el: ",LiAu[azar])
        LiMod.append(LiAu[azar])
        LiVa.append(random.randint(5000000,10000000))
        print("El precio del vehiculo es: $",LiVa[cont])
    else:
        print("El modelo de vehiculo es el: ",LiCa[azar])
        LiMod.append(LiCa[azar])
        LiVa.append(random.randint(8000000,13000000))
        print("El precio del vehiculo es: $",LiVa[cont])
#carga lista dni, modelo y el precio

#######
def cotizacion(LiVa,LiEm,cont,LiPa,cont1,cont2,cont3):
    auxval=LiVa[cont]*0.001
    #Elegir tipo de seguro
    opcion=validarRango(1,3, "Ingrese 1 si el tipo de seguro es contra tercero, 2 contra tercero completo y 3 para todo riesgo: ")
    #En base al tipo de seguro se imprime el coste que tendria segun cada empresa
    #El primer if representa el tipo de seguro, el segundo if la empresa
    if opcion == 1:
        auxval = auxval * 5
        print("***COTIZACION: contra tercero***")
        print("")
        print("->empresa 1: $",round(auxval*1,0))
        print("->empresa 2: $",round(auxval*1.25,0))
        print("->empresa 3: $",round(auxval*1.5,0))
        opcionem=validarRango(1,3, "Elija cual empresa (1,2,3): ")
        if opcionem == 1:
            cont1 += 1
            pagomen=round(auxval*1,0)
        elif opcionem == 2:
            cont2 += 1
            pagomen=round(auxval*1.25,0)
        else:
            cont3 += 1
            pagomen=round(auxval*1.5,0)
    elif opcion == 2:
        auxval = auxval * 7
        print("***COTIZACION: contra tercero completo***")
        print("")
        print("->empresa 1: $",round(auxval*1.5,0))
        print("->empresa 2: $",round(auxval*1,0))
        print("->empresa 3: $",round(auxval*1.25,0))
        print("")
        opcionem=validarRango(1,3, "Elija cual empresa (1,2,3): ")
        if opcionem == 1:
            cont1 += 1
            pagomen=round(auxval*1.5,0)
        elif opcionem == 2:
            cont2 += 1
            pagomen=round(auxval*1,0)
        else:
            cont3 += 1
            pagomen=round(auxval*1.25,0)
    else:
        auxval = auxval * 13
        print("***COTIZACION: todo riesgo***")
        print("")
        print("->empresa 1: $",round(auxval*1.25,0))
        print("->empresa 2: $",round(auxval*1.5,0))
        print("->empresa 3: $",round(auxval*1,0))
        print("")
        opcionem=validarRango(1,3, "Elija caul empresa (1,2,3): ")
        if opcionem == 1:
            pagomen=round(auxval*1.25,0)
        elif opcionem == 2:
            pagomen=round(auxval*1.5,0)
        else:
            pagomen=round(auxval*1,0)
    #Una vez elegida una opcion, se guarda la empresa y el pago por mes en las listas
    LiEm.append(opcionem)
    LiPa.append(pagomen)
    return cont1,cont2,cont3
 
######
def poliza(LiDni, LiMod, LiVa, LiPa, LiEm):
    print("")
    print("")
    print("==========================================================================")
    print("				***POLIZA***				")
    print("==========================================================================")
    print("\tDNI        MODELO               		VALOR VEHICULO      PAGO MENSUAL    EMPRESA")
    i=-1
    print("\t%-10d %-35s $%14.2f $%13.2f %10s" % (LiDni[i], LiMod[i], LiVa[i], LiPa[i], LiEm[i]))

######
def burbujeo(lista1,lista2):
    for i in range(0, len(lista1)-1):
        for j in range(0, len(lista1)-1-i):
            
            if (lista1[j] < lista1[j+1]):
                aux = lista1[j]
                lista1[j] = lista1[j+1]
                lista1[j+1] = aux
                
                aux = lista2[j]
                lista2[j] = lista2[j+1]
                lista2[j+1] = aux
    
##############################################
def main():
    #Preinicializacion de listas:
        #Listas con los modelos
    motos=["moto: Ducati 696", "moto: Honda XR", "moto: KTM Duke", "moto: Yamaha YZ", "moto: Susuki GS", "moto: BMW F800"]
    autos=["auto: Mazda 3", "auto: Audi TT", "auto: Ford GT", "auto: Subaru BRZ", "auto: Lexus RX", "auto: Toyota GT"]
    camion=["camión: MAN TGA", "camión: Iveco 35", "camión: Hino 338", "camión: Volvo FM", "camión: Scania P", "camión: DAF CF85."]
    ##########################################
        #Listas con los datos de los clientes
    dni=[]
    modelo=[]
    valorVehiculo=[]
    empresas=[]
    pagoxmes=[]
    ##########################################
    #Contadores
    nrocli=0
    #Mensaje de vienvenida del programa
    ingresoProductor()
    #While principal
    #Condicion de finalizacion del while main -> variable opcion
    opcion=validarRango(1,3, "Por favor, ingrese 1 para cargar datos de clientes, 2 para ver listas o 3 para generar informe y salir: ")
    print("")
    while opcion != 3:
        if opcion == 1:
            ingresoCliente(dni,nrocli,motos,autos,camion,modelo,valorVehiculo)
            cotizacion(valorVehiculo,empresas,nrocli,pagoxmes)
            #Luego de completar la carga incrementa el contador de posicion
            nrocli+=1
            poliza(dni,modelo,valorVehiculo,pagoxmes,empresas)

        print("")
        
        if opcion == 2:
            orden=burbujeo(empresas,valorVehiculo)
            print("")
            print("==========================================================================")
            print("				***CLIENTES***				")
            print("==========================================================================")
            print("\tDNI        MODELO               		VALOR VEHICULO      PAGO MENSUAL    EMPRESA")
            for i in range(len(dni)):
                print("\t%-10d %-35s $%14.2f $%13.2f %10s" % (dni[i], modelo[i], valorVehiculo[i], pagoxmes[i], empresas[i]))
        
        opcion=validarRango(1,3, "Por favor, ingrese 1 para cargar datos de clientes, 2 para ver listas o 3 para generar informe y salir: ")
        
        

    if nrocli == 0:
        print("no se cargaron clientes")
    else:
        print("==========================================================================")
        print("				***CLIENTES***				")
        print("==========================================================================")
        print("")
        print("la cantidad de clientes registrados en esta sesion: ",nrocli)
        print("cantidad de clientes por empresa......")
        print("empresa 1: ")
        print("empresa 2: ")
        print("empresa 3: ")
        
if __name__ == "__main__":
    main()
