from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import open
import os

class reporte:

    def generarreporte(listaafdelegido):
        lista=listaafdelegido
        w,h=A4
        estados = ""
        alfabeto = ""
        estadoaceptacion = ""
        transicion = ""
        Titulodocumento = f"Nombre:{lista[0]}"
#W WEIDGHT  H ALTURA
        #TITULO
        pdf = canvas.Canvas(f"{listaafdelegido[0]}.pdf",pagesize=A4)
        pdf.drawString(w-(w/2)-len(Titulodocumento),h-50,Titulodocumento)
        #CUERPO
        cuerpotexto=pdf.beginText(50,h-70)
        cuerpotexto.setFont("Times-Roman", 12)
        for i in range(len(listaafdelegido)):
            if i==0:
                cuerpotexto.textLine("")
            elif i==1:
                for z in range(len(listaafdelegido[i])):
                    if z==0:
                        estados=listaafdelegido[i][z]
                    else:
                        estados=estados+","+listaafdelegido[i][z]
                cuerpotexto.textLine(f"Estados: {estados}")
            elif i==2:
                for z in range(len(listaafdelegido[i])):
                    if z ==0:
                        alfabeto= listaafdelegido[i][z]
                    else:
                        alfabeto = alfabeto +","+listaafdelegido[i][z]
                cuerpotexto.textLine(f"Alfabeto: {alfabeto}")
            elif i==3:
                cuerpotexto.textLine(f'Estado inicial: {listaafdelegido[i]}')
            elif i==4:
                for z in range(len(listaafdelegido[i])):
                    if z == 0:
                        estadoaceptacion = listaafdelegido[i][z]
                    else:
                        estadoaceptacion = estadoaceptacion +","+ listaafdelegido[i][z]
                cuerpotexto.textLine(f'Estados de aceptacion: {estadoaceptacion}')
            elif i==5:
                cuerpotexto.textLine("Transiciones: ")
                for z in range(len(listaafdelegido[i])):  #Se elige la lista que contiene las listas de transiciones, cada z es una lista de transiciones
                    transicion=listaafdelegido[i][z][0]
                    transicion=transicion+","+listaafdelegido[i][z][1]
                    transicion= transicion+";"+listaafdelegido[i][z][2]
                    cuerpotexto.textLine(transicion)
        pdf.drawText(cuerpotexto)
#-----------------------------GENERACION DE IMAGEN Y poner esta en pdf---------------------------------------------
        reporte.generarImagen(lista)
        pdf.drawString(w-(w/2)-50,h-80,"Grafo:")
        pdf.drawImage(f"{listaafdelegido[0]}.png",w-(w/2)-50,h-90-170,width=280,height=170)
#--------------------------------CADENA VALIDA-------------------------------------------------------------
        cadena = reporte.Cadenavalida(listaafdelegido)
        pdf.drawString(50,h-(h/2),f'Cadena valida de ejemplo: {cadena}')
        pdf.save()
        os.system(f"{listaafdelegido[0]}.pdf")


#--------------------------------------------------------------------------------------------------------------------------------
    def generarImagen(afdescogido):
        listaafd=afdescogido
        listatransiciones=listaafd[5]
        listaestados=listaafd[1]
        nombre=listaafd[0]
        archivo=open(f"{nombre}.dot","w")
        archivo.write("digraph "+nombre+"{\n")
        archivo.write('node[style="filled", shape=circle, fillcolor="white"];\n')
        archivo.write('rankdir=LR;')
        for i in listaestados:
            n=0
            for z in listaafd[4]:
                if z==i:
                    n+=1
            if n>0:
                archivo.write(f'{i}[label="{i}",shape="doublecircle"];\n')
            else:
                archivo.write(f'{i}[label="{i}"];\n')
        archivo.write(f'apuntador[label="",shape="point"];\n')
        archivo.write(f'apuntador->{listaafd[3]};\n')
        for i in listatransiciones:
            archivo.write(f'{i[0]}->{i[2]}[label="{i[1]}"];\n')
        archivo.write("}")
        archivo.close()
        os.system(f"dot -Tpng {listaafd[0]}.dot -o {listaafd[0]}.png ")

    def Cadenavalida(listaafd):
        cadena=""
        transiciones=listaafd[5]
        estadosfinales=listaafd[4]
        estados=listaafd[1]
        estadoinicial=listaafd[3]
        estadoactual=estadoinicial
        n=0
#cadena de

        for i in range(len(transiciones)):
            if transiciones[i][0]==estadoinicial:
                cadena=transiciones[i][1]
                estadoactual=transiciones[i][2]
        print(estadoactual)
        while estadoactual!=estadosfinales[len(estadosfinales)-1]:
            if transiciones[n][0]==estadoactual:
                cadena=cadena+transiciones[n][1]
                estadoactual=transiciones[n][2]
            n+=1

        return cadena










