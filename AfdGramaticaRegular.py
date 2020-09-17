
class gramaticaRegular:
    def generacionDeGramatica(listafd):
        terminales=listafd[2]
        Noterminales=listafd[1]
        inicio=listafd[3]
        transiciones=listafd[5]
        n=0

        print("------------GRAMATICA REGULAR-----------")
        for i in terminales:
            if i==terminales[0]:
                print("Terminales {"+i+",",end="")
            elif i==terminales[len(terminales)-1]:
                print(i+"}")
            else:
                print(i+",",end="")
        for i in Noterminales:
            if i==Noterminales[0]:
                print("Terminales {"+i+",",end="")
            elif i==Noterminales[len(Noterminales)-1]:
                print(i+"}")
            else:
                print(i+",",end="")
        print(f"Inicio: {inicio}")
        print("producciones: ")
        for i in Noterminales:
            for z in transiciones:
                if z[0]==i and n==0:
                    print(f"{i} > {z[1]}{z[2]}")
                    n=+1
                elif z[0]==i and n>0:
                    print(f"   | {z[1]}{z[2]}")
            n=0
