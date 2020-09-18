
class Bienvenida:
    def impbienvenida(self):
        print("Lenguajes Formales y de Programacion ")
        print("Sección: B")
        print("Carnet: 201800534")
        input("Presiones una tecla para continuar...")
    def Menuprincipal(self):
        print("\n---------------Menu principal----------------")
        print("1.Modulo AFD:")
        print("2.Modulo de gramaticas regulares: ")
        print("3.Acerca de: ")
        print("4.Salir")
    def Menuafd(self):
        print("1.Crear AFD")
        print("2.Cargar Archivo")
        print('3.Evaluar cadena')
        print("4.Guardar AFD en archivo")
        print("5.Generar reporte AFD")
        print("6.Generar Gramatica Regular")
        print("7.Salir")
    def Menugramaticas(self):
        print("1.Crear Gramaticas")
        print("2.Cargar archivo de entrada")
        print('3.Evaluar cadena')
        print("4.Eliminar recursividad por la izquierda")
        print("5.Generar AFD en archivo")
        print("6.Generar reporte de Gramatica Regular")
        print("7.Salir")

    def existenciaestados(estado,listaingreso):
            # Se ingresa el estado, si existe no pasa nada por que no hay prints, si no existe dara error y pasara a guardar en lista el valor
            if listaingreso.count(estado) == 0:
                listaingreso.append(estado)
            else:
                print("-------------Dicho estado ya se encuentra ingresado-----------")
                estado = input("Ingrese otro estado: ")
                listaingreso.append(estado)
            return listaingreso
    def existenciaAlfabeto(alfabeto,alfabeto1afd,estado1afd):
        if alfabeto1afd.count(alfabeto) == 0 and estado1afd.count(alfabeto) == 0:
            alfabeto1afd.append(alfabeto)
        else:
            alfabeto = input("Dicho signo o estado ya se encuentra almacenado en el alfabeto escriba otro: ")
            alfabeto1afd.append(alfabeto)
        return alfabeto1afd
    def Menuestadosaceptacion(estadoaceptacion,estado1afd, estadoaceptacicon1afd):
        if estado1afd.count(estadoaceptacion) == 0:
            print("\nNo existe dicho estado en los estados anteriormente ingresados")
            estadoaceptacion = input("Ingrese el nombre de un estado que exista: ")
        estadoaceptacicon1afd.append(estadoaceptacion)
        return estadoaceptacicon1afd

    def Transiciones(transicion,transiciones1afd):
        n=0
        parte1 = transicion.split(",")
        parte0 = [parte1[0]]
        parte2 = parte1[1].split(";")
        parte0.extend(parte2)
        if len(parte0) == 3:
            for i in range(len(transiciones1afd)):
                if transiciones1afd[i][0] == parte0[0] and transiciones1afd[i][1] == parte0[1]:
                    n += 1
            if n == 0:
                transiciones1afd.append(parte0)
            else:
                transicion = input("Esta transicion destruye el afd ingrese otra (Estado origen,simbolo de entrada,Estado Destino): ")
                parte1 = transicion.split(",")
                parte0 = [parte1[0]]
                parte2 = parte1[1].split(";")
                parte0.extend(parte2)
                transiciones1afd.append(parte0)
        else:
            transicion = input("Cadena de ingreso incorrecta ingrese otra respetando el formato: ")
            parte1 = transicion.split(",")
            parte0 = [parte1[0]]
            parte2 = parte1[1].split(";")
            parte0.extend(parte2)
            transiciones1afd.append(parte0)
            if len(parte0) == 3:
                for i in range(len(transiciones1afd)):
                    if transiciones1afd[i][0] == parte0[0] and transiciones1afd[i][1] == parte0[1]:
                        n += 1
                if n == 0:
                    transiciones1afd.append(parte0)
                else:
                    transicion = input(
                        "Esta transicion destruye el afd ingrese otra (Estado origen,simbolo de entrada,Estado Destino): ")
                    parte1 = transicion.split(",")
                    parte0 = [parte1[0]]
                    parte2 = parte1[1].split(";")
                    parte0.extend(parte2)
                    transiciones1afd.append(parte0)
        return transiciones1afd

    def Ingresoafd(n,listaafd,afd):
        n=0
        afd=[]
        transiciones=[]

        while n!= len(listaafd):

            nombre = listaafd[n]
            n += 1
            estados=listaafd[n].split(",")
            n+=1
            alfabeto=listaafd[n].split(",")
            n+=1
            estadoinicial=listaafd[n]
            n+=1
            estadoaceptacion=listaafd[n].split(",")
            n+=1
            while listaafd[n]!="%":
                parte1=listaafd[n].split(",")
                parte2=[parte1[0]]
                parte3=parte1[1].split(";")
                parte2.extend(parte3)
                transiciones.append(parte2)
                n+=1
            transicion1=transiciones.copy()
            transiciones.clear()
            lista = [nombre, estados, alfabeto, estadoinicial, estadoaceptacion, transicion1]

            afd.append(lista)

            if listaafd[n]=="%":
                n+=1

        #nombre,estado,alfabeto,estado inic, estadoaceptacion,transiciones

        return afd


    #Apartado 1

    #Apartado 2
    #Apartado 3
