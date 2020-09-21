class Validacion:
    def validacion(cadena,Gramatica):
        # Gramatica=[nombre,No terminales,terminales,No terminal inicial,producciones]
#-------------------------------------------------------------------------------------------------------
        terminales=Gramatica[2]
        noterminal=Gramatica[1]
        producciones=Gramatica[4]
        noterminalinicial=Gramatica[3]
        n=0
#------------------------------------------------------------------------------------------------------------
        existencia=True
        actual=noterminalinicial
        n1=0
        n2=0
        noterminalfinal = Validacion.noterminalfinal(producciones)
        secuencia=[]
#----------------------------------------------------------
        secuencia.append(actual)
#------------------------------------------------
        for i in cadena:
            for k in terminales:
                if i==k:
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
                    secuencia.append(actual)
                    n1+=1

#EN EL CASO QUE SEA EL NO TERMINAL DE LA CADENA VACIA HACER UN IF ESPECIAL PUES ESTOS NO LLEGAN HASTA [2] SI NO A [1]
            else:
                break

#---------------------------------------ULTIMO NOTERMINAL ES IGUAL A UNO DE TODOS LOS NO TERMINALES
        for i in noterminalfinal:
            if i==secuencia[len(secuencia)-1]:
                n2+=1

        if n1==len(cadena) and n==len(cadena)  and n2>0:
            existencia=True
        else:
            existencia=False
        return existencia



    def noterminalfinal(producciones):
        noterminalfinal=[]
        for i in producciones:
            if len(i)==2:
                noterminalfinal.append(i[0])
        return noterminalfinal




    def index(producciones,Noterminalactual,terminalactual):
        existe="False"
        n=0
#devolvera el tamano del la lista producciones si no se encontro
        for i in producciones:
            if i[0]==Noterminalactual and i[1]==terminalactual:
                break
            n+=1
        return n

    def procesoexpansion(cadena,Gramatica):
        # Gramatica=[nombre,No terminales,terminales,No terminal inicial,producciones]
        # -------------------------------------------------------------------------------------------------------
        terminales = Gramatica[2]
        noterminal = Gramatica[1]
        producciones = Gramatica[4]
        noterminalinicial = Gramatica[3]
        n = 0
        # ------------------------------------------------------------------------------------------------------------
        existencia = True
        actual = noterminalinicial
        n1 = 0
        n2 = 0
        noterminalfinal = Validacion.noterminalfinal(producciones)
        secuencia = []
        ruta=[]
        # ----------------------------------------------------------
        secuencia.append(actual)
        # ------------------------------------------------
        for i in cadena:
            for k in terminales:
                if i == k:
                    n += 1

        # 2 factores importantes para ser validas, que n1 sea igual al tamano de la cadena, que el ultimo valor sea una cadena vacia,
        # n == tamaño de la cadena significa que solo se estan usando los terminales ingresados en los no terminales
        for i in cadena:
            index = Validacion.index(producciones, actual, i)
            if index != len(producciones):
                if len(producciones[index]) == 2:
                    n1 += 1
                else:
                    ruta1=f"{producciones[index][0]} > {producciones[index][1]} {producciones[index][2]}"
                    ruta.append(ruta1)
                    actual = producciones[index][2]
                    secuencia.append(actual)
                    n1 += 1

            # EN EL CASO QUE SEA EL NO TERMINAL DE LA CADENA VACIA HACER UN IF ESPECIAL PUES ESTOS NO LLEGAN HASTA [2] SI NO A [1]
            else:
                break

        # ---------------------------------------ULTIMO NOTERMINAL ES IGUAL A UNO DE TODOS LOS NO TERMINALES
        for i in noterminalfinal:
            if i == secuencia[len(secuencia) - 1]:
                n2 += 1
        if n2>0:
            indexcadenavacia=Validacion.indexcadenavacia(producciones,actual)
            ruta1=f"{producciones[indexcadenavacia][0]} > {producciones[indexcadenavacia][1]}"
            ruta.append(ruta1)

        if n1 == len(cadena) and n == len(cadena) and n2 > 0:
            for i in ruta:
                print(i)
            existencia = True
        else:
            for i in ruta:
                print(i)
            existencia = False
        return existencia

    def indexcadenavacia(producciones,actual):
        n=0
        for i in producciones:
            if i[0]==actual and len(i)==2:
                break
            else:
                n+=1
        return n

