import random

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

def burbujeo(lista1,lista2,lista3,lista4,lista5):
    for i in range(0, len(lista1)-1):
        for j in range(0, len(lista1)-1-i):
            
            if (lista1[j] < lista1[j+1]):
                aux = lista1[j]
                lista1[j] = lista1[j+1]
                lista1[j+1] = aux
                
                aux = lista2[j]
                lista2[j] = lista2[j+1]
                lista2[j+1] = aux
                
                aux = lista3[j]
                lista3[j] = lista3[j+1]
                lista3[j+1] = aux
                
                aux = lista4[j]
                lista4[j] = lista4[j+1]
                lista4[j+1] = aux
                
                aux = lista5[j]
                lista5[j] = lista5[j+1]
                lista5[j+1] = aux

def sumaLista(lista):
    suma = 0
    for i in range (len(lista)):
        suma = suma + lista[i]
    return suma

def maximo(lista):
    for i in range(len(lista)):
        if (i==0) or (lista[i]>valMaximo):
            valMaximo=lista[i]
            imax=i
    return imax

def ingresoProductor():
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

def ingresoCliente(LiDNI,cont,LiMo,LiAu,LiCa,LiMod,LiVa):
    nombreApellido=input("Ingrese nombre y apellido del cliente: ")
    Auxdni=validarRango(10000000,99999999,"Ingrese dni del cliente: ")
    while busqueda(LiDNI,Auxdni) != -1:
        print("DNI ya registrado, si desea ingresar un nuevo vehiculo para el mismo dni inicie sesion nuevamente")
        Auxdni=validarRango(10000000,99999999,"Ingrese su dni: ")
    LiDNI.append(Auxdni)
    print("El nro de cliente es: ",1+cont)
    print("")
    opcion=validarRango(1,3, "Ingrese 1 si el tipo de vehiculo es una moto, ingrese 2 si es un auto y 3 si es un camion: ")
    azar=random.randint(0,5)
    if opcion==1:
        print("->El modelo de vehiculo es el: ",LiMo[azar])
        LiMod.append(LiMo[azar])
        LiVa.append(random.randint(1000000,4000000))
        print("->El precio del vehiculo es: $",LiVa[cont])
    elif opcion==2:
        print("->El modelo de vehiculo es el: ",LiAu[azar])
        LiMod.append(LiAu[azar])
        LiVa.append(random.randint(5000000,10000000))
        print("->El precio del vehiculo es: $",LiVa[cont])
    else:
        print("->El modelo de vehiculo es el: ",LiCa[azar])
        LiMod.append(LiCa[azar])
        LiVa.append(random.randint(8000000,13000000))
        print("->El precio del vehiculo es: $",LiVa[cont])

def cotizacion(LiVa,LiEm,cont,LiPa):
    auxval=LiVa[cont]*0.001
    opcion=validarRango(1,3, "Ingrese 1 si el tipo de seguro es contra tercero, 2 contra tercero completo y 3 para todo riesgo: ")

    if opcion == 1:
        auxval = auxval * 5
        print("")
        print("***COTIZACION: contra tercero***")
        print("")
        print("->empresa 1: $",round(auxval*1,0))
        print("->empresa 2: $",round(auxval*1.25,0))
        print("->empresa 3: $",round(auxval*1.5,0))
        opcionem=validarRango(1,3, "Elija cual empresa (1,2,3): ")
        if opcionem == 1:
            pagomen=round(auxval*1,0)
        elif opcionem == 2:
            pagomen=round(auxval*1.25,0)
        else:
            pagomen=round(auxval*1.5,0)
    elif opcion == 2:
        auxval = auxval * 7
        print("")
        print("***COTIZACION: contra tercero completo***")
        print("")
        print("->empresa 1: $",round(auxval*1.5,0))
        print("->empresa 2: $",round(auxval*1,0))
        print("->empresa 3: $",round(auxval*1.25,0))
        print("")
        opcionem=validarRango(1,3, "Elija cual empresa (1,2,3): ")
        if opcionem == 1:
            pagomen=round(auxval*1.5,0)
        elif opcionem == 2:
            pagomen=round(auxval*1,0)
        else:
            pagomen=round(auxval*1.25,0)
    else:
        auxval = auxval * 13
        print("")
        print("***COTIZACION: todo riesgo***")
        print("")
        print("->empresa 1: $",round(auxval*1.25,0))
        print("->empresa 2: $",round(auxval*1.5,0))
        print("->empresa 3: $",round(auxval*1,0))
        print("")
        opcionem=validarRango(1,3, "Elija cual empresa (1,2,3): ")
        if opcionem == 1:
            pagomen=round(auxval*1.25,0)
        elif opcionem == 2:
            pagomen=round(auxval*1.5,0)
        else:
            pagomen=round(auxval*1,0)
    LiEm.append(opcionem)
    LiPa.append(pagomen)
 
def poliza(LiDni, LiMod, LiVa, LiPa, LiEm):
    print("")
    print("")
    print("==========================================================================")
    print("				***POLIZA***				")
    print("==========================================================================")
    print("\tDNI        MODELO               		VALOR VEHICULO      PAGO MENSUAL    EMPRESA")
    i=-1
    print("\t%-10d %-35s $%14.2f $%13.2f %10s" % (LiDni[i], LiMod[i], LiVa[i], LiPa[i], LiEm[i]))

def main():
    motos=["moto: Ducati 696", "moto: Honda XR", "moto: KTM Duke", "moto: Yamaha YZ", "moto: Susuki GS", "moto: BMW F800"]
    autos=["auto: Mazda 3", "auto: Audi TT", "auto: Ford GT", "auto: Subaru BRZ", "auto: Lexus RX", "auto: Toyota GT"]
    camion=["camión: MAN TGA", "camión: Iveco 35", "camión: Hino 338", "camión: Volvo FM", "camión: Scania P", "camión: DAF CF85."]
    dni=[]
    modelo=[]
    valorVehiculo=[]
    empresas=[]
    pagoxmes=[]
    nrocli=0
    cont1=0
    cont2=0
    cont3=0
    ingresoProductor()
    opcion=validarRango(1,3, "Por favor, ingrese 1 para cargar datos de clientes, 2 para ver listas o 3 para generar informe y salir: ")
    print("")
    while opcion != 3:
        if opcion == 1:
            ingresoCliente(dni,nrocli,motos,autos,camion,modelo,valorVehiculo)
            cotizacion(valorVehiculo,empresas,nrocli,pagoxmes)
            if empresas[-1] == 1:
                cont1+=1
            elif empresas[-1] == 2:
                cont2+=1
            elif empresas[-1] == 3:
                cont3+=1
            nrocli+=1
            poliza(dni,modelo,valorVehiculo,pagoxmes,empresas)
        print("")
        if opcion == 2:
            burbujeo(empresas,valorVehiculo,dni,modelo,pagoxmes)
            print("")
            if len(dni) > 0:
                print("==========================================================================")
                print("				***CLIENTES***				")
                print("==========================================================================")
                print("\tDNI        MODELO               		VALOR VEHICULO      PAGO MENSUAL    EMPRESA")
                for i in range(len(dni)):
                    print("\t%-10d %-35s $%14.2f $%13.2f %10s" % (dni[i], modelo[i], valorVehiculo[i], pagoxmes[i], empresas[i]))
                print("")
                opcionBus=validarRango(1,2,"Ingrese 1 si desea buscar un cliente por DNI o 2 si desea continuar: ")
                while opcionBus != 2:
                    dniBus=validarRango(10000000,99999999,"Ingrese dni del cliente: ")
                    posi=busqueda(dni,dniBus)
                    if posi == -1:
                        print("No se encontro un cliente con ese DNI")
                    else:
                        print("_______________________________________________________________________________________________")
                        print("\tDNI        MODELO               		VALOR VEHICULO      PAGO MENSUAL    EMPRESA")
                        print("\t%-10d %-35s $%14.2f $%13.2f %10s" % (dni[posi], modelo[posi], valorVehiculo[posi], pagoxmes[posi], empresas[posi]))
                    print("")
                    opcionBus=validarRango(1,2,"Ingrese 1 si desea buscar otro cliente por DNI o 2 si desea continuar: ")
            else:
                print("____________________________________")
                print("***no se ingreso ningun cliente***")
                print("____________________________________")
                print("")
        opcion=validarRango(1,3, "Por favor, ingrese 1 para cargar datos de clientes, 2 para ver listas o 3 para generar informe y salir: ")
        
    if nrocli == 0:
        print("no se cargaron clientes")
    else:
        promedio=sumaLista(valorVehiculo)/len(valorVehiculo)
        masCaro=maximo(valorVehiculo)
        print("==========================================================================")
        print("				***INFORME***				")
        print("==========================================================================")
        print("")
        print("La ganancia del productor es: $", round(sumaLista(pagoxmes)*0.10,0))
        print("")
        print("la cantidad de clientes registrados en esta sesion: ",nrocli)
        print("cantidad de clientes por empresa......")
        print("empresa 1: ",cont1, " %6.2f" %(cont1*100/len(dni)),"%")
        print("empresa 2: ",cont2, " %6.2f" %(cont2*100/len(dni)),"%")
        print("empresa 3: ", cont3, " %6.2f" %(cont3*100/len(dni)),"%")
        print("")
        print("El valor promedio de los vehiculos es: $",round(promedio,0))
        print("")
        print("El cliente con el vehiculo mas caro fue: ")
        print("_______________________________________________________________________________________________")
        print("\tDNI        MODELO               		VALOR VEHICULO      PAGO MENSUAL    EMPRESA")
        print("\t%-10d %-35s $%14.2f $%13.2f %10s" % (dni[masCaro], modelo[masCaro], valorVehiculo[masCaro], pagoxmes[masCaro], empresas[masCaro]))
        print("")
        if (nrocli>1):
            print("")
            print("Clientes con vehiculos cuyo valor esta por devajo del promedio: ")
            print("_______________________________________________________________________________________________")
            print("\tDNI        MODELO               		VALOR VEHICULO      PAGO MENSUAL    EMPRESA")
            for i in range(len(dni)):
                if valorVehiculo[i]<promedio:
                    print("\t%-10d %-35s $%14.2f $%13.2f %10s" % (dni[i], modelo[i], valorVehiculo[i], pagoxmes[i], empresas[i]))
        
if __name__ == "__main__":
    main()
