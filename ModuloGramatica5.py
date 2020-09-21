from io import open
class archivoGramatica:
    def guardargramatica(listagramatica):

        # lista = [nombre, NoTerminales, Terminales, Noterminalinicial, producciones1]
        noterminales=""
        terminales=""
        producciones=""
        archivo=open(f"{listagramatica[0]}.gre","w")
        for i in range(len(listagramatica)):
            if i==0:
                archivo.write(listagramatica[i]+"\n")
            elif i==1:
                for z in range(len(listagramatica[i])):
                    if z==0:
                        noterminales=listagramatica[i][z]
                    else:
                        noterminales=noterminales+","+listagramatica[i][z]
                archivo.write(noterminales+"\n")
            elif i==2:
                for z in range(len(listagramatica[i])):
                    if z ==0:
                        terminales= listagramatica[i][z]
                    else:
                        terminales = terminales +","+listagramatica[i][z]
                archivo.write(terminales+"\n")
            elif i==3:
                archivo.write(listagramatica[i]+"\n")
            elif i==4:
                for z in listagramatica[i]:  #PRODUCCIONES
                    if len(z)==2:
                        producciones=f"{z[0]}>{z[1]}"
                    elif len(z)==3:
                        producciones = f"{z[0]}>{z[1]} {z[2]}"
                    archivo.write(producciones+"\n")
        archivo.write("%")
        archivo.close()
