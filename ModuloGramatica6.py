from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import open
import os
import random

class reporte:

    def generarreporte(listagramaticaelegida):
        lista=listagramaticaelegida
        # lista = [nombre, NoTerminales, Terminales, Noterminalinicial, producciones1]
        Noterminales = lista[1]
        w,h=A4
        noterminales = ""
        terminales = ""

        Titulodocumento = f"Nombre:{lista[0]}"
#W WEIDGHT  H ALTURA
        #TITULO
        pdf = canvas.Canvas(f"{lista[0]}.pdf",pagesize=A4)
        pdf.drawString(w-(w/2)-len(Titulodocumento)-10,h-50,Titulodocumento)
        #CUERPO
        cuerpotexto=pdf.beginText(50,h-70)
        cuerpotexto.setFont("Times-Roman", 12)
        for i in range(len(lista)):
            if i==0:
                cuerpotexto.textLine("")
            elif i==1:
                for z in range(len(lista[i])):
                    if z==0:
                        noterminales=lista[i][z]
                    else:
                        noterminales=noterminales+","+lista[i][z]
                cuerpotexto.textLine(f"No Terminales: {noterminales}")
            elif i==2:
                for z in range(len(lista[i])):
                    if z ==0:
                        terminales= lista[i][z]
                    else:
                        terminales = terminales +","+lista[i][z]
                cuerpotexto.textLine(f"Terminales: {terminales}")
            elif i==3:
                cuerpotexto.textLine(f'No terminal inicial: {lista[i]}')
            elif i==4:
                cuerpotexto.textLine("Producciones: ")
                for y in Noterminales:
                    n=0
                    for z in lista[i]:
                        if n==0 and z[0]==y:
                            if len(z)==3:
                                produccion=f"{z[0]} >  {z[1]} {z[2]}"
                                cuerpotexto.textLine(produccion)
                                n+=1
                            else:
                                produccion = f"{z[0]} >  {z[1]}"
                                cuerpotexto.textLine(produccion)
                                n += 1
                        elif n>0 and z[0]==y:
                            if len(z)==3:
                                produccion = f"     |  {z[1]} {z[2]}"
                                cuerpotexto.textLine(produccion)
                            else:
                                produccion = f"     |  {z[1]}"
                                cuerpotexto.textLine(produccion)

        pdf.drawText(cuerpotexto)
#-----------------------------GENERACION DE IMAGEN Y poner esta en pdf---------------------------------------------
        reporte.generarImagen(lista)
        pdf.drawString(w-(w/2)-50,h-80,"Grafo:")
        pdf.drawImage(f"{lista[0]}.png",w-(w/2)-50,h-90-170,width=280,height=170)
#--------------------------------CADENA VALIDA-------------------------------------------------------------
        cadena = reporte.Cadenavalida(lista)
        pdf.drawString(50,h-(h/2),f'Cadena valida de ejemplo: {cadena}')
        pdf.save()
        os.system(f"{lista[0]}.pdf")


#--------------------------------------------------------------------------------------------------------------------------------
    def generarImagen(gramaticaescogida):
        listagramatica=gramaticaescogida
        producciones=listagramatica[4]
        listanoterminales=listagramatica[1]
        nombre=listagramatica[0]
        archivo=open(f"{nombre}.dot","w")
        archivo.write("digraph "+nombre+"{\n")
        archivo.write('node[style="filled", shape=circle, fillcolor="white"];\n')
        archivo.write('rankdir=LR;')
        for i in listanoterminales:
            n=0
            for z in listagramatica[4]:
                if len(z)==2 and z[0]==i:
                    n+=1
            if n>0:
                archivo.write(f'{i}[label="{i}",shape="doublecircle", fillcolor="cyan" ];\n')
            else:
                archivo.write(f'{i}[label="{i}"];\n')
        archivo.write(f'apuntador[label="",shape="point"];\n')
        archivo.write(f'apuntador->{listagramatica[3]};\n')
        for i in producciones:
            if len(i)==3:
                archivo.write(f'{i[0]}->{i[2]}[label="{i[1]}"];\n')
        archivo.write("}")
        archivo.close()
        os.system(f"dot -Tpng {listagramatica[0]}.dot -o {listagramatica[0]}.png ")

    def Cadenavalida(listagramatica):
        cadena=""
        producciones=listagramatica[4]
        Ntf=reporte.noterminalesfinales(producciones)
        noterminales=listagramatica[1]
        noterminalinicial=listagramatica[3]
        ProduccionE=False
        noterminalActual=noterminalinicial
        n=0
#cadena de
        while ProduccionE==False:
            n=random.randint(0,(len(producciones)-1))
            if producciones[n][0]==noterminalActual and producciones[n][1]!="$":
                noterminalActual=producciones[n][2]
                cadena=producciones[n][1]
                ProduccionE=True

        while noterminalActual!=Ntf[len(Ntf)-1]:
            n = random.randint(0, (len(producciones)-1))
            if producciones[n][0]==noterminalActual and len(producciones[n])!=2:
                cadena=cadena+producciones[n][1]
                noterminalActual=producciones[n][2]



        return cadena

    def noterminalesfinales(producciones):
        Ntf=[]
        for i in producciones:
            if len(i)==2:
                Ntf.append(i[0])
        return Ntf