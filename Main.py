import Menus

Menus.Bienvenida.impbienvenida("")
Menus.Bienvenida.Menuprincipal("")
n=int(input("Ingrese una opcion: "))
if n>4 or n<1:
    print("\n------------------Opcion incorrecta--------------------")
else:
    while n!=4:
        if n==1:
            Menus.Bienvenida.Menuafd("")
        elif n==2:
            Menus.Bienvenida.Menugramaticas("")
