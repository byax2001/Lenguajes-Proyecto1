import Menus
import Automata
import csv
import os
from io import open

afd=[]
#afd1=[nombre,estados[],alfabetos[],estadoinicial,estadosdeaceptacion,transiciones]
estado1afd=[]
alfabeto1afd=[]
estadoaceptacicon1afd=[]
transiciones1afd=[]

Menus.Bienvenida.impbienvenida("")
Menus.Bienvenida.Menuprincipal("")
n=int(input("Ingrese una opcion: "))
if n>4 or n<1:
    print("\n------------------Opcion incorrecta--------------------")
while n != 4:
    #Apartado 1--------------------------------------------------------------------------------------------------
    if n == 1:
        Menus.Bienvenida.Menuafd("")
        n1= int(input("Ingrese una opcion: "))

        if n1 > 8 or n1 < 1:
            print("\n------------------Opcion incorrecta--------------------")
        while n1!=7:
            #Apartado 1

            if n1==1:
                print("\n--------Ingreso de nombre de AFD-----")
                nombre=input("Ingrese un nombre: ")
                #---------------------------------------------------------------------------------------------------------
                print("\n----------Ingreso de Estado----------")
                n=int(input("Ingrese numero de estados a agregar: "))
                for i in range(n):
                    estado = input("Ingresar estado: ")
                    estado1afd=Menus.Bienvenida.existenciaestados(estado, estado1afd)
#-------------------------Ingreso de alfabeto
                print("\n----------Ingreso de Alfabeto----------")
                n = int(input("Ingrese numero de alfabetos a agregar: "))
                for i in range(n):
                    alfabeto = input("Ingresar Alfabeto: ")
                    alfabeto1afd=Menus.Bienvenida.existenciaAlfabeto(alfabeto,alfabeto1afd,estado1afd)
                print("\n")
#-----------------------------Ingreso de cual es el estado inicial
                estadoini=input("Ingresar nombre del estado incial: ")
                if estado1afd.count(estadoini)==0:
                    print("\nNo existe dicho estado en los estados anteriormente ingresados")
                    estadoini = input("Ingresar nombre del estado incial: ")
#----------------------------Ingreso de Estados de aceptacion
                print("\n----------Ingreso de Estados de aceptacion----------")
                n = int(input("Ingrese numero de estados de aceptacion: "))
                for i in range(n):
                    estadoaceptacion = input("Ingresar Estado de aceptacion: ")
                    estadoaceptacicon1afd=Menus.Bienvenida.Menuestadosaceptacion(estadoaceptacion,estado1afd,estadoaceptacicon1afd)
#------------------------------------Ingreso de transiciones
                print("\n----------Ingreso de Transiciones (Escriba fin para terminar)----------")
                n=0
                transicion = input("Ingresar transicion (Estado origen,simbolo de entrada,Estado Destino): ")
                if transicion!="fin":
                    transiciones1afd=Menus.Bienvenida.Transiciones(transicion,transiciones1afd)
                while transicion!="fin":
 #-------------------------------------------------------------------------------------------------
                    transicion = input("Ingresar transicion (Estado origen,simbolo de entrada,Estado Destino): ")
                    if transicion!="fin":
                        transiciones1afd=Menus.Bienvenida.Transiciones(transicion,transiciones1afd)
                lista=[nombre,estado1afd,alfabeto1afd,estadoini,estadoaceptacicon1afd,transiciones1afd]
                afd.append(lista)
#-------------------------------------------------------Apartado 2
            elif n1==2:
                listanueva=[]
                print("\n---------------Ingreso de afd's---------------")
                nombre=input("Ingrese nombre del archivo: ")
                archivo=open(f"{nombre}.afd","r")
                listalineas=archivo.readlines()
                archivo.close()

                for i in listalineas:
                    listanueva.append(i.rstrip("\n"))
                n=0
                afd=Menus.Bienvenida.Ingresoafd(n,listanueva,afd)
                print("-----------------Ingreso Exitoso-----------------")
#---------------------------------------------------------APARTADO 3
            elif n1==3:
                Cadenacorrecta=True
                print('----------------Evaluacion de cadenas---------------')
                n=0
                for i in afd:
                    n+=1
                    print(f"{n}.{i}")
                print("Opciones:")
                print("1.Evaluar Cadena")
                print("2.Ruta en AFD")
                n=int(input("Ingrese una opcion: "))
                if n==1:
                    numero=int(input("Ingrese numero de afd: "))
                    cadena=input("\nIngrese una cadena: ")
                    Cadenacorrecta=Automata.Afd.Evaluacionafd(afd[numero-1],cadena)
                    if Cadenacorrecta==True:
                        print("La cadena es valida")
                    else:
                        print("La cadena es invalida")
                elif n==2:
                    numero = int(input("Ingrese numero de afd: "))
                    cadena = input("\nIngrese una cadena: ")
                    Automata.Afd.rutaevaluaciones(afd[numero - 1], cadena)
                    print("\n")


                    #RECORDARSE DEL N-1 A LA HORA DE ESCOGER LA OPCION SI NO SE SALE DE LA LISTA
            elif n1==4:
                print("")
            elif n1==5:
                print('')
            elif n1==6:
                print("")

            Menus.Bienvenida.Menuafd("")
            n1 = int(input("Ingrese una opcion: "))
            if n1 > 8 or n1 < 1:
                print("\n------------------Opcion incorrecta--------------------")

    #Apartado 2------------------------------------------------------------------------------------------------------
    elif n==2:
        Menus.Bienvenida.Menugramaticas("")
    #Apartado 3
    elif n==3:
        print("Apartado 3")
    Menus.Bienvenida.Menuprincipal("")
    n=int(input("Ingrese una opcion: "))
    if n > 4 or n < 1:
        print("\n------------------Opcion incorrecta--------------------")

