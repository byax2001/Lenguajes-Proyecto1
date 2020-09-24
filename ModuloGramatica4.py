class Gramaticasinizq:
    def gramaticaSinizq(GramaticaConizq):
    #lista = [nombre, NoTerminales, Terminales, Noterminalinicial, producciones1]
        GramaticaSinRizq=[]
        GramaticaSinRizq1=[]
        GramaticaSinRizq2=[]
        for i in GramaticaConizq:
            nombre=i[0]
            NoTerminales=i[1]
            Terminales=i[2]
            NoTerminalinicial=i[3]
            produccionessinizq = Gramaticasinizq.eliminaciondeRizq(i[4],NoTerminales)
            lista=[nombre,NoTerminales,Terminales,NoTerminalinicial,produccionessinizq]
            GramaticaSinRizq2=lista.copy()
            GramaticaSinRizq.append(GramaticaSinRizq2)
            lista.clear()
        return GramaticaSinRizq





    def eliminaciondeRizq(produccionesizq,Noterminales):
        produccionesSinRizq=[]
        produccionconvertida=[]
        noterminal1=""
        terminal=""
        noterminal2=""
        for k in Noterminales:
            for i in produccionesizq:

                if i[0]==k and len(i)==3:
                    noterminal1 = f"{k}'"
                    terminal = i[2]
                    noterminal2 = f"{k}'"
                    produccionconvertida1 = [noterminal1, terminal, noterminal2]

                if i[0]==k and len(i)==2:
                    noterminal1=f"{k}"
                    terminal=i[1]
                    noterminal2=f"{k}'"
                    produccionconvertida=[noterminal1,terminal,noterminal2]
                    produccionesSinRizq.append(produccionconvertida)
            produccionesSinRizq.append(produccionconvertida1)
            produccionfinal=[f"{k}'","Ɛ"]
            produccionesSinRizq.append(produccionfinal)
        return produccionesSinRizq







