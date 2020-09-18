class Validacion:
    def validacion(cadena,terminales,noterminal,noterminalinicial,producciones):
        n=0
        actual=noterminalinicial
        n1=0
        for i in cadena:
            for k in terminales:
                if i==k:
                    n+=1
#n == tamaño de la cadena significa que solo se estan usando los terminales ingresados en los no terminales
        for i in range(len(cadena)):
            if i==0:
                index=Validacion.index(producciones,actual,i)
                if index!=len(producciones):
                    actual=producciones[index][2]





    def index(producciones,Noterminalactual,terminalactual):
        existe="False"
        n=0
#devolvera el tamano del la lista producciones si no se encontro
        for i in producciones:
            if i[0]==Noterminalactual and i[1]==terminalactual:
                break
            n+=1
        return n





