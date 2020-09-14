
class Afd:
    def Evaluacionafd(afdEscogido,cadena):
        #[nombre, estados, alfabeto, estadoinicial, estadoaceptacion, transiciones]
        comprobantealfabeto=0
        estadoinicial=afdEscogido[3]
        estadosfinales=afdEscogido[4]
        transiciones=afdEscogido[5]
        TransicionExiste=False
        Cadenacorrecta=True
        posiblesinicios=[]
        posiblesfinales=[]
        aprobacionalfabeto=False
        aprobacioninicial=False
        aprobacionfinal=False
        # posibles inicios

        posiblesinicios=Afd.posiblesinicios(transiciones,estadoinicial)
        # Posibles finales
        for estadoaceptado in estadosfinales: #cada uno de los estados de aceptacion
            for i in transiciones:
                if i[2] == estadoaceptado:
                    posiblesfinales.append(i[1])

        #solo letras del alfabeto
        for i in cadena:
            for alfabeto in afdEscogido[3]:
                if alfabeto==i:
                    comprobantealfabeto=+1

        index2 = 0
        n=0
        estadoactual=""
    #metodo transiciones:
        while TransicionExiste==False:
            for signo in cadena:
                if n==len(cadena):
                    TransicionExiste=True
                    print("JIJOLINES")
                else:
                    if index2 == 0:
                        index2 = Afd.index(transiciones, estadoinicial, signo)
                        if index2 == len(transiciones):
                            TransicionExiste = True
                            print("JIJOLINESPAPT")
                        else:
                            estadoactual = transiciones[index2][2]
                            index2=Afd.index(transiciones,estadoactual,signo)
                            print(estadoactual)
                            n += 1
                            print("JIJOLINESPIP")

                    else:
                        index2 = Afd.index(transiciones, estadoactual, signo)
                        if index2 == len(transiciones):
                            TransicionExiste = True
                            print("MIXD")
                        else:
                            estadoactual = transiciones[index2][2]
                            index2 = Afd.index(transiciones, estadoactual, signo)
                            n += 1
                            print(estadoactual)
                            print("Hollysh")

        n2=0
        for i in posiblesfinales:
           if i==cadena[len(cadena)-1]:
               n2+=1
        print("------------------------------------------------------------------")
        print(n)
        print(n2)

        if n2>0 and n==len(cadena):
            Cadenacorrecta=True
            print("xD")
            return Cadenacorrecta
        else:
            Cadenacorrecta=False
            return Cadenacorrecta




#-----------------------------------------------------------------------------------------------------------
    def index(listatransiciones,Estadoizq,signo):
        tam=len(listatransiciones)
        existe=False
        numero=0
        while existe==False:
            print("XD")
            if numero==tam:
                existe==True
            else:
                if listatransiciones[numero][0]==Estadoizq and listatransiciones[numero][1]==signo:
                    existe=True
                else:
                    numero+=1

        return numero

    def posiblesinicios(transiciones,estadoinicial):
        n=0
        posinicios=[]
        for i in transiciones:
            if estadoinicial==i[0]:
                posinicios.append(i[1])
        return posinicios

