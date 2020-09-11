import Menus
afd=[]
#afd1=[nombre,estados[],alfabetos[],estadoinicial,estadosdeaceptacion,transiciones]
estado1afd=[]
alfabeto1afd=[]
estadoaceptacicon1afd=[]
transiciones1afd=[]
lista=["xD",["lol","jijo"],"rains"]


Menus.Bienvenida.impbienvenida("")
Menus.Bienvenida.Menuprincipal("")
n=int(input("Ingrese una opcion: "))
if n>4 or n<1:
    print("\n------------------Opcion incorrecta--------------------")
while n!=4:
    #Apartado 1--------------------------------------------------------------------------------------------------
    if n==1:
        Menus.Bienvenida.Menuafd("")
        n1=int(input("----Ingrese una opcion: "))
        if n1 > 6 or n1 < 1:
            print("\n------------------Opcion incorrecta--------------------")
        while n!=7:
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
                

                print("\n----------Ingreso de Estados de aceptacion----------")
                n = int(input("Ingrese numero de estados de aceptacion: "))
                for i in range(n):
                    estado = input("Ingresar Estado de aceptacion: ")
                    estadoaceptacicon1afd.append(estado)
                print("\n----------Ingreso de Transiciones----------")
                n = int(input("Ingrese numero de transciones: "))
                for i in range(n):
                    transicion = input("Ingresar transicion (Estado origen, simbolo de entrada, Estado Destino): ")
                    transiciones1afd.append(transicion)
                afd.append(nombre,estado1afd,alfabeto1afd,estadoini,estadoaceptacicon1afd,transiciones1afd)

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

    #Apartado 2------------------------------------------------------------------------------------------------------
    elif n==2:
        Menus.Bienvenida.Menugramaticas("")
    #Apartado 3
    elif n==3:
        print("Apartado 3")
    Menus.Bienvenida.Menuprincipal("")
    if n > 4 or n < 1:
        print("\n------------------Opcion incorrecta--------------------")

