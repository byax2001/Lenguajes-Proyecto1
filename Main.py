import Menus
import Automata
import Guardarafd
import Reporte
import AfdGramaticaRegular
import ModuloGramatica1
import ModuloGramatica2
import ModuloGramatica3
import ModuloGramatica4
import ModuloGramatica5
import csv
import os
from io import open
Gramatica=[]
afd=[]
GramaticaSinRizq=[]
GramaticaConRizq=[]

# Gramatica=[nombre,No terminales,terminales,No terminal inicial,producciones]
nombregramatica=""
Noterminales=[]
Terminales=[]
Noterminalinicial=""
producciones=[]

#afd1=[nombre,estados[],alfabetos[],estadoinicial,estadosdeaceptacion,transiciones]
estado1afd=[]
alfabeto1afd=[]
estadoaceptacicon1afd=[]
transiciones1afd=[]
n=0

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

#----------------------------------------Apartado 4
            elif n1==4:
                print("----------------GUARDAR ARCHIVO---------------")
                n = 0
                for i in afd:
                    n += 1
                    print(f"{n}.{i}")
                noarchivo=int(input("Ingrese numero de afd a guardar: "))
                Guardarafd.Guardar.guardarafd(afd[noarchivo-1])


            elif n1==5:
                n=0
                print("---------------GENERACION DE REPORTE--------------")
                if len(afd)==0:
                    print("No se han ingresado AFD's")
                else:
                    for i in afd:
                        n+=1
                        print(f"{n}.{i}")
                    n=int(input("Escoja numero de afd para generar reporte: "))
                    Reporte.reporte.generarreporte(afd[n-1])
                    print("----------GENERACION DE REPORTE EXITOSO-------")
            elif n1==6:
                n=0
                print("------------GENERACION DE GRAMATICA--------------")
                if len(afd)==0:
                    print("No se han ingresado AFD's")
                else:
                    #Terminales el alfabeto
                    #No terminales, estados
                    #Inicio, estado inicial

                    for i in afd:
                        n+=1
                        print(f"{n}.{i}")
                    n = int(input("Escoja numero de afd para generar reporte: "))
                    AfdGramaticaRegular.gramaticaRegular.generacionDeGramatica(afd[n-1])
                    opcion=input("\nDesea generar un reporte del afd escogido? (si/no): ")
                    if opcion=="si":
                        Reporte.reporte.generarreporte(afd[n-1])
                        print("***Gramatica y reporte generados con exito***")
                    else:
                        print("***Gramatica realizada con exito***")

            Menus.Bienvenida.Menuafd("")
            n1 = int(input("Ingrese una opcion: "))
            if n1 > 8 or n1 < 1:
                print("\n------------------Opcion incorrecta--------------------")
#Apartado 2------------------------------------------------------------------------------------------------------
    elif n==2:
        print("------------MODULO DE GRAMATICAS--------------")
        Menus.Bienvenida.Menugramaticas("")
        n1=int(input("Ingrese una opcion: "))
        if n1>7 and n1<0:
            print("opcion invalida")
        while n1!=7:
            if n1==1:
                print("--------------INGRESO DE GRAMATICA------------")
                # Gramatica=[nombre,No terminales,terminales,No terminal inicial,producciones]
                nombregramatica=input("Inserte Nombre de Gramatica: ")
            #----------------------------------------------------------------------------------
                print("---------------Ingreso de No terminales-----------")
                N=int(input("Ingrese numero de No terminales a ingresar: "))
                Noterminales=ModuloGramatica1.gramatica.IngresoNoterminales(N)
            #---------------------------------------------------------------------------------
                print("----------------Ingreso de Terminales--------------")
                N = int(input("Ingrese numero de Terminales a ingresar: "))
                Terminales=ModuloGramatica1.gramatica.IngresoTerminalees(N,Noterminales)
            #-----------------------------------------------------------------
                print("----------------Ingreso No Terminal Inicial")
                Noterminalinicial=ModuloGramatica1.gramatica.Noterminalini(Noterminales)
            #-----------------------------------------------------------------
                print("---------------Ingreso de producciones (Ej: A > 2 B)-----------------")
                N=int(input("Ingrese NUMERO de producciones a agregar: "))
                producciones=ModuloGramatica1.gramatica.producciones(Terminales,Noterminales,N)
                lista=[nombregramatica,Noterminales,Terminales,Noterminalinicial,producciones]
                Gramatica.append(lista)
            elif n1==2:
                listanueva = []
                print("\n---------------Ingreso de Gramaticas---------------")
                nombre = input("Ingrese nombre del archivo: ")
                archivo = open(f"{nombre}.gre", "r")
                listalineas = archivo.readlines()
                archivo.close()
                for i in listalineas:
                    listanueva.append(i.rstrip("\n"))
                n=0
                Gramatica=ModuloGramatica2.gramatica.Ingresogramatica(listanueva,Gramatica)
                print("\n-------------Gramaticas ingresadas con exito---------------")
                print("\n")

            elif n1==3:
                print("----------------Evaluacion de Gramaticas--------------------")
                n = 0
                for i in Gramatica:
                    n += 1
                    print(f"{n}.{i}")
                print("Opciones:")
                print("1.Validar una cadena")
                print("2.Proceso de Expasion")
                n = int(input("Ingrese una opcion: "))
                if n == 1:
                    numero = int(input("Ingrese numero de Gramatica: "))
                    cadena = input("\nIngrese una cadena: ")
                    Cadenacorrecta=ModuloGramatica3.Validacion.validacion(cadena,Gramatica[numero-1])
                    if Cadenacorrecta == True:
                        print("La cadena es valida")
                        print("\n")
                    else:
                        print("La cadena es invalida")
                        print("\n")
                elif n == 2:
                    numero = int(input("Ingrese numero de gramatica: "))
                    cadena = input("\nIngrese una cadena: ")
                    Cadenacorrecta = ModuloGramatica3.Validacion.procesoexpansion(cadena, Gramatica[numero - 1])
                    if Cadenacorrecta == True:
                        print("La cadena es valida")
                        print("\n")
                    else:
                        print("La cadena es invalida")
                        print("\n")
#Modulo 2 opcion 4--------------------------------------------------------------------------------------------------
            elif n1==4:
                listanueva = []
                print("\n---------------Ingreso de Gramaticas---------------")
                nombre = input("Ingrese nombre del archivo: ")
                archivo = open(f"{nombre}.gre", "r")
                listalineas = archivo.readlines()
                archivo.close()
                for i in listalineas:
                    listanueva.append(i.rstrip("\n"))
                n = 0
                GramaticaConRizq = ModuloGramatica2.gramatica.Ingresogramatica(listanueva, Gramatica)
                GramaticaSinRizq=ModuloGramatica4.Gramaticasinizq.gramaticaSinizq(GramaticaConRizq)
                print(GramaticaSinRizq)

                print("\n-------------Gramatica con eliminacion de recursividad por la izquierda con exito---------------")
                print("\n")
#APARTADO 5 MODULO 2---------------------------------------------------------------------------------
            if n1==5:
                print("----------------GUARDAR ARCHIVO---------------")
                n = 0
                for i in Gramatica:
                    n += 1
                    print(f"{n}.{i}")
                noarchivo = int(input("Ingrese numero de gramatica a guardar: "))
                ModuloGramatica5.archivoGramatica.guardargramatica(Gramatica[noarchivo - 1])
                print("\n-Archivo generado con exito-\n")
            elif n1==6:
                print("xd")
            Menus.Bienvenida.Menugramaticas("")
            n1 = int(input("Ingrese una opcion: "))
            if n1 > 7 and n1 < 0:
                print("opcion invalida")


    #Apartado 3
    elif n==3:
        print("Apartado 3")
    Menus.Bienvenida.Menuprincipal("")
    n=int(input("Ingrese una opcion: "))
    if n > 4 or n < 1:
        print("\n------------------Opcion incorrecta--------------------")

