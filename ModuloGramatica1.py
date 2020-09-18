class gramatica:
    def IngresoNoterminales(N):
        noterminales=[]

        for i in range(N):
            noterminal = input("Ingrese un No Terminal: ")
            if i==0:
                noterminales.append(noterminal)
            else:
                n=0
                for z in noterminales:
                    if z==noterminal:
                        n+=1
                if n>0:
                    noterminal = input("Ya se ingreso dicho no terminal ingrese otro: ")
                    noterminales.append(noterminal)
                else:
                    noterminales.append(noterminal)
        return noterminales
    def IngresoTerminalees(N,listanoterminales):
        terminales=[]
        for i in range(N):
            n=0
            terminal = input("Ingrese un Terminal: ")
            for z in listanoterminales:
                if z==terminal:
                    n+=1
            for k in terminales:
                if k==terminal:
                    n+=1
            if n==0:
                terminales.append(terminal)
            else:
                print("\nDicho terminal ya fue ingresado o se encuentra en los no terminales")
                noterminal=input("Ingrese otro Terminal: ")
                terminales.append(terminal)
        return terminales

    def Noterminalini(listanoterminales):
        inicial=input("Ingrese el estado No terminal inicial: ")
        n=0
        for i in listanoterminales:
            if i==inicial:
                n+=1
        if n==0:
            print("\nDicho no terminal no se encuentra en la lista de los no terminales anteriormente ingresados")
            inicial=input("Ingrese otro No terminal inicial: ")

        return inicial

    def producciones(listaterminales,listanoterminales,N):
        producciones=[]
        p=""
        p3=[]
        produccion=""
#------------DEBEN DE EXISTIR EN LOS NO TERMINALES Y TERMINALES-------------------
        for i in range(N):
            n=0
            k=0
            existe=False
            produccion=input("Ingrese produccion : ")
            p=produccion.split(" ")
#-------si tiene mas que 2 entonces si se encuentran ambos estados ingresados:
            if len(p)==4 or len(p)==3 and p[1]==">":

                print("SI CUMPLIO CON EL FORMATO")
                existe=gramatica.comprobantetransiciones(listaterminales,listanoterminales,p)
                if existe==True:
                    p3=gramatica.produccionAingresar(p)
                    producciones.append(p3)
                    print("XD")
                else:
                    print("Existe un Terminal o No terminal no ingresado ")
                    produccion=input("Ingrese otra produccion: ")
                    p = produccion.split(" ")
                    p3 = gramatica.produccionAingresar(p)
                    producciones.append(p3)

            else:
                produccion=input("Ingreso una produccion incorrecta ingrese otra: ")
                p=produccion.split(" ")
                existe=gramatica.comprobantetransiciones(listaterminales,listanoterminales,p)
                if existe==True:
                    p3 = gramatica.produccionAingresar(p)
                    producciones.append(p3)
                else:
                    print("Existe un Terminal o No terminal no ingresado ")
                    produccion=input("Ingrese otra produccion: ")
                    p = produccion.split(" ")
                    p3 = gramatica.produccionAingresar(p)
                    producciones.append(p3)
        return producciones


    def comprobantetransiciones(listaterminales,listanoterminales,p):
        n=0
        k=0
        ingreso=True
        for i in listaterminales:
            if i == p[0] or i == p[3]:
                n += 1
        for i in listanoterminales:
            if i == p[2]:
                k += 1
        if n>1 and k>0:
            ingreso=True
        else:
            ingreso=False

        return ingreso

    def produccionAingresar(p):
        produccionretorno=[]
        if len(p)==3:
            produccionretorno.append(p[0])
            produccionretorno.append(p[2])
        if len(p)==4:
            produccionretorno.append(p[0])
            produccionretorno.append(p[2])
            produccionretorno.append(p[3])
        return produccionretorno


















