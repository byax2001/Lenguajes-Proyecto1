class Gramatica:

    def Ingresogramatica(listagramatica,gramatica):
        # Gramatica=[nombre,No terminales,terminales,No terminal inicial,producciones]
        n=0
        producciones=[]
        eliminables=[]
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
        #no terminales
        z=0
        y=0
        for i in gramatica:
            for k in i[4]:
                if len(k)==3:
                    print("Noterminales")
                    Existencia1=Gramatica.ExistenciaNT(i[1],k[0])
                    Existencia2=Gramatica.ExistenciaNT(i[1],k[2])
                    print(Existencia1)
                    print(Existencia2)
                    if Existencia1==False or Existencia2==False:
                        y+=1
                elif len(k)==2:
                    print("Noterminales con cadena vacia")
                    Existencia1=Gramatica.ExistenciaNT(i[1],k[0])
                    print(Existencia1)
                    if Existencia1==False:
                        y+=1
            #TERMINALES
            for m in i[4]:
                    if m[1]!="$":
                        Existencia1=Gramatica.ExistenciaNT(i[2],m[1])
                        if Existencia1==False:
                            y+=1
            if y>0:
                eliminables.append(z)
            z+=1
        t=0
        for i in eliminables:
            gramatica.pop(i-t)
            t+=1


        return gramatica

    def ExistenciaNT(listanoterminal,noterminal):
        Existencia=False
        n=0
        for i in listanoterminal:
            if i==noterminal:
                n+=1
        if n>0:
            Existencia=True
        else:
            Existencia=False
        return Existencia



