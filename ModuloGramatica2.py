class gramatica:

    def Ingresogramatica(listagramatica,gramatica):
        # Gramatica=[nombre,No terminales,terminales,No terminal inicial,producciones]
        n=0
        producciones=[]
        while n!= len(listagramatica):

            nombre = listagramatica[n]
            n += 1
            NoTerminales=listagramatica[n].split(",")
            n+=1
            Terminales=listagramatica[n].split(",")
            n+=1
            Noterminalinicial=listagramatica[n]
            n+=1
            #PRODUCCIONES
            parte2=[]
            parte3=[]
            parte4=[]
            while listagramatica[n]!="%":
                parte1=listagramatica[n].split(">")
                parte2=[parte1[0]]
                parte3=parte1[1].split(" ")
                parte2.extend(parte3)
                producciones.append(parte2)
                n+=1
            producciones1=producciones.copy()
            producciones.clear()
            lista = [nombre, NoTerminales, Terminales, Noterminalinicial, producciones1]
            gramatica.append(lista)

            if listagramatica[n]=="%":
                n+=1

        #nombre,estado,alfabeto,estado inic, estadoaceptacion,transiciones

        return gramatica