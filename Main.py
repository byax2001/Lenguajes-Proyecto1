import Menus
afd=[]
#afd1=[nombre,estados[],alfabetos[],estadoinicial,estadosdeaceptacion,transiciones]
estado1afd=[]
alfabeto1afd=[]
estadoaceptacicon1afd=[]
transiciones1afd=[]


def impbienvenida():
    print("Lenguajes Formales y de Programacion ")
    print("Sección: B")
    print("Carnet: 201800534")
    input("Presiones una tecla para continuar...")


def Menuprincipal():
    print("\n---------------Menu principal----------------")
    print("1.Modulo AFD:")
    print("2.Modulo de gramaticas regulares: ")
    print("3.Acerca de: ")
    print("4.Salir")


def Menuafd():
    print("1.Crear AFD")
    print("2.Cargar Archivo")
    print('3.Evaluar cadena')
    print("4.Guardar AFD en archivo")
    print("5.Generar reporte AFD")
    print("6.Generar Gramatica Regular")
    print("7.Salir")


def Menugramaticas():
    print("1.Crear Gramaticas")
    print("2.Cargar archivo de entrada")
    print('3.Evaluar cadena')
    print("4.Eliminar recursividad por la izquierda")
    print("5.Generar AFD en archivo")
    print("6.Generar reporte de Gramatica Regular")
    print("7.Salir")


impbienvenida()
Menuprincipal()
n=int(input("Ingrese una opcion: "))
if n>4 or n<1:
    print("\n------------------Opcion incorrecta--------------------")
while n != 4:
    #Apartado 1--------------------------------------------------------------------------------------------------
    if n == 1:
        Menuafd()
        n1= int(input("Ingrese una opcion: "))
        print("#################################################################33")
        if n1 > 8 or n1 < 1:
            print("\n------------------Opcion incorrecta--------------------")
        while n1!=7:
            #Apartado 1

            if n1==1:
                print("\n--------Ingreso de nombre de AFD-----")
                nombre=input("Ingrese un nombre: ")

                print("\n----------Ingreso de Estado----------")
                n=int(input("Ingrese numero de estados a agregar: "))
                for i in range(n):
                    estado = input("Ingresar estado: ")
#Se ingresa el estado, si existe no pasa nada por que no hay prints, si no existe dara error y pasara a guardar en lista el valor
                    if estado1afd.count(estado)==0:
                        estado1afd.append(estado)
                    else:
                        print("-------------Dicho estado ya se encuentra ingresado-----------")
                        estado = input("Ingrese otro estado: ")
                        estado1afd.append(estado)
#-------------------------Ingreso de alfabeto
                print("\n----------Ingreso de Alfabeto----------")
                n = int(input("Ingrese numero de alfabetos a agregar: "))
                for i in range(n):
                    alfabeto = input("Ingresar Alfabeto: ")
                    print(alfabeto.count(alfabeto))
                    print(estado1afd.count(alfabeto))
                    if alfabeto1afd.count(alfabeto)==0 and estado1afd.count(alfabeto)==0:
                        alfabeto1afd.append(alfabeto)
                    elif alfabeto1afd.count(alfabeto)!=0:
                        alfabeto=input("Dicho signo ya se encuentra almacenado en el alfabeto escriba otro: ")
                        alfabeto1afd.append(alfabeto)
                    elif estado1afd.count(alfabeto!=0):
                        alfabeto=input("Dicho valor ya se encuentra almacenado en los estados escriba otro: ")
                        alfabeto1afd.append(alfabeto)
                print("\n")
#-----------------------------Ingreso de cual es el estado inicial
                estadoini=input("Ingresar nombre del estado incial: ")
                if estado1afd.count(estadoini)==0:
                    print("\nNo existe dicho estado en los estados anteriormente ingresados")
                    estadoini = input("Ingresar nombre del estado incial: ")

                print("\n----------Ingreso de Estados de aceptacion----------")
                n = int(input("Ingrese numero de estados de aceptacion: "))
                for i in range(n):
                    estadoaceptacion = input("Ingresar Estado de aceptacion: ")
                    if estado1afd.count(estadoaceptacion) == 0:
                        print("\nNo existe dicho estado en los estados anteriormente ingresados")
                        estadoaceptacion = input("Ingrese el nombre de un estado que exista: ")
                    estadoaceptacicon1afd.append(estadoaceptacion)
#------------------------------------Ingreso de transiciones
                print("\n----------Ingreso de Transiciones (Escriba fin para terminar)----------")
                numero = 0
                transicion = input("Ingresar transicion (Estado origen,simbolo de entrada,Estado Destino): ")
                transiciones1afd.append(transicion)
                while transicion!="fin":
                    transicion = input("Ingresar transicion (Estado origen,simbolo de entrada,Estado Destino): ")
                    transiciones1afd.append(transicion)
                    if estado1afd.count(transicion[0])!=0 and estado1afd.count(transicion[4])!=0:
                        if len(transiciones1afd)==0:
                            transiciones1afd.append(transicion.split(","))
                        else:
                            for i in range(len(transiciones1afd)):
                                if transiciones1afd[i][2]==transicion[2] and transiciones1afd[i][0]==transicion[0]:
                                    print("transicion invalida, intenta realizar dos transiciones con el mismo simbolo")
                                    transicion = input("Ingresar transicion valida (Estado origen,simbolo de entrada,Estado Destino): ")
                                    transiciones1afd.append(transicion)
                                else:
                                    transiciones1afd.append(transicion)
                lista=[nombre,estado1afd,alfabeto1afd,estadoini,estadoaceptacicon1afd,transiciones1afd]
                afd.append(lista)
            elif n1==2:
                print("")
            elif n1==3:
                print('')
            elif n1==4:
                print("")
            elif n1==5:
                print('')
            elif n1==6:
                print("")
            print("*********************************************************")
            Menuafd()
            n1 = int(input("Ingrese una opcion: "))
            if n1 > 8 or n1 < 1:
                print("\n------------------Opcion incorrecta--------------------")

    #Apartado 2------------------------------------------------------------------------------------------------------
    elif n==2:
        Menus.Bienvenida.Menugramaticas("")
    #Apartado 3
    elif n==3:
        print("Apartado 3")
    print("XDXDXDXDXDXDDXDXDXDXDXDXDXDXD")
    Menuprincipal()
    n=int(input("Ingrese una opcion: "))
    if n > 4 or n < 1:
        print("\n------------------Opcion incorrecta--------------------")

