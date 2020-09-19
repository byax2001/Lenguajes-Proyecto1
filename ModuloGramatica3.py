class Validacion:
    def validacion(cadena,Gramatica):
        # Gramatica=[nombre,No terminales,terminales,No terminal inicial,producciones]
        terminales=Gramatica[2]
        noterminal=Gramatica[1]
        producciones=Gramatica[4]
        noterminalinicial=Gramatica[3]
        n=0
        existencia=True
        actual=noterminalinicial
        terminalesfinales=[]
        n1=0
        n2=0
        terminalfinal = Validacion.terminalfinal(producciones)
        for i in cadena:
            for k in terminales:
                if i==k:
                    n+=1
            for z in terminalfinal:
                if i==z:
                    n+=1

#2 factores importantes para ser validas, que n1 sea igual al tamano de la cadena, que el ultimo valor sea una cadena vacia,
#n == tamaño de la cadena significa que solo se estan usando los terminales ingresados en los no terminales
        for i in cadena:
            index=Validacion.index(producciones,actual,i)
            if index!=len(producciones):
                if len(producciones[index])==2:
                    n1+=1
                else:
                    actual=producciones[index][2]
                    n1+=1

#EN EL CASO QUE SEA EL NO TERMINAL DE LA CADENA VACIA HACER UN IF ESPECIAL PUES ESTOS NO LLEGAN HASTA [2] SI NO A [1]
            else:
                break

        for i in terminalfinal:
            if cadena[len(cadena)-1]==i:
                n2+=1
        print("----------------*****************------------------------")
        print(terminalfinal)
        print(n1)
        print(n2)
        print(n)
        if n1==len(cadena) and n2>0 and n==len(cadena):
            existencia=True
        else:
            existencia=False
        return existencia



    def terminalfinal(producciones):
        terminalfinal=[]
        for i in producciones:
            if len(i)==2:
                terminalfinal.append(i[1])
        return terminalfinal




    def index(producciones,Noterminalactual,terminalactual):
        existe="False"
        n=0
#devolvera el tamano del la lista producciones si no se encontro
        for i in producciones:
            if i[0]==Noterminalactual and i[1]==terminalactual:
                break
            n+=1
        return n





