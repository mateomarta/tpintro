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

def ingresoCliente(LiDNI,LiTV):
    nombreApellido=input("Ingrese su nombre y apellido: ")
    Auxdni=validarRango(10000000,99999999,"Ingrese su dni: ")
    if busqueda(LiDNI,Auxdni) != -1:
        print("DNI DUPLICADO")
        Auxdni=validarRango(10000000,99999999,"Ingrese su dni: ")
    else:
        LiDNI.append(Auxdni)
        LiTV.append(validarRango(1,3,"Ingrese 1 si es moto, 2 si es camion o 3 si es auto"))
           
def busqueda (lista,valor):
    pos = -1
    i = 0
    while (pos == -1) and (i<len(lista)):
        if (lista[i] == valor):
            pos = i
        i+=1
    return pos

def cotizacion(LiTV,LiValorveh,LiMo,LiAu,LiCa):
    azar=random.randint(0,5)
    if LiTV==1:
        print("Su modelo de vehiculo es: " ,LiMo[azar])
    elif LiTV==2:
        print("Su modelo de vehiculo es: " ,LiCa[azar])
    else:
        print("Su modelo de vehiculo es: " ,LiAu[azar])
    
    

    
def main():
    
    dni=[]
    motos=["Harley-Davidson Road Glide Special", "Ducati Panigale V4", "BMW R 1250 GS ", "Kawasaki Ninja ZX-10R", "Yamaha MT-07", "Honda CRF450R"]
    autos=["Toyota Corolla", "Honda Civic", "Ford Mustang", "Chevrolet Silverado", "Tesla Model 3", "BMW Serie 3"]
    camion=["Scania R Series", "Mercedes-Benz Actros", "Volvo FH16", "MAN TGX", "Freightliner Cascadia", "DAF XF"]
    tipoVehiculo=[]
    valorVehiculo=[]

    ingresoProductor()
    opcion=validarRango(1,3, "Por favor, ingrese 1 para cargar datos de clientes, 2 para ver listas o 3 para generar informe y salir")
    
    while opcion != 3:
        if opcion==1:
            ingresoCliente(dni, tipoVehiculo)
            cotizacion(tipoVehiculo,valorVehiculo,motos,autos,camion)
        opcion=validarRango(1,3, "Por favor, ingrese 1 para cargar datos de clientes, 2 para ver listas o 3 para generar informe y salir")
            

if __name__ == "__main__":
    main()




