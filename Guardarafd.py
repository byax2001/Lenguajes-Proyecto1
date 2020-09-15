from io import open

class Guardar:

    def guardarafd(listaafdelegido):
        estados=""
        alfabeto=""
        estadoaceptacion=""
        transicion=""
        archivo=open(f"{listaafdelegido[0]}.afd","w")
        for i in range(len(listaafdelegido)):
            if i==0:
                archivo.write(listaafdelegido[i]+"\n")
            elif i==1:
                for z in range(len(listaafdelegido[i])):
                    if z==0:
                        estados=listaafdelegido[i][z]
                    else:
                        estados=estados+","+listaafdelegido[i][z]
                archivo.write(estados+"\n")
            elif i==2:
                for z in range(len(listaafdelegido[i])):
                    if z ==0:
                        alfabeto= listaafdelegido[i][z]
                    else:
                        alfabeto = alfabeto +","+listaafdelegido[i][z]
                archivo.write(alfabeto+"\n")
            elif i==3:
                archivo.write(listaafdelegido[i]+"\n")
            elif i==4:
                for z in range(len(listaafdelegido[i])):
                    if z == 0:
                        estadoaceptacion = listaafdelegido[i][z]
                    else:
                        estadoaceptacion = estadoaceptacion +","+ listaafdelegido[i][z]
                archivo.write(estadoaceptacion+"\n")
            elif i==5:
                for z in range(len(listaafdelegido[i])):  #Se elige la lista que contiene las listas de transiciones, cada z es una lista de transiciones
                    transicion=listaafdelegido[i][z][0]
                    transicion=transicion+","+listaafdelegido[i][z][1]
                    transicion= transicion+";"+listaafdelegido[i][z][2]
                    archivo.write(transicion+"\n")
        archivo.write("%")
        archivo.close()
