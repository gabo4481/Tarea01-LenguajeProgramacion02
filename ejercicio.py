#Desarrolla un programa en Python que presente un menú de opciones al usuario.
#El programa debe permitir al usuario ingresar y guardar nombres en un archivo de texto.
#Requisitos:
#1. Menú de Opciones: El programa debe mostrar un menú con las siguientes opciones:
#a) Agregar nombre.
#b) Mostrar nombres.
#c) Buscar un nombre
#d) Salir.
#Nombre: Gabriel Mendoza



#creacion de funciones necesarias para el menu.

#funcionalidad 1
def agregar_nombres(contador):
    if contador > 0:
        with open("nombres.txt", "a") as archivo:
            nombre = input("\nIngresa nombre para agregar: ")
            archivo.write(f"{nombre} \n")
    else:
        with open("nombres.txt", "w") as archivo:
            nombre = input("\nIngresa nombre para agregar: ")
            archivo.write(f"{nombre} \n")
            
#funcionalidad 2
def mostrar_nombres():
    with open("nombres.txt","r") as archivo:
        nombres = archivo.readlines()
        for nombre in nombres:
            print(nombre.strip())
            
#funcionalidad 3
def buscar_nombres():
    with open("nombres.txt","r") as archivo:
        nombre_buscado = input("\nIngresa el nombre que deseas buscar: ")
        nombres = archivo.readlines()
        for linea_numero,nombre in enumerate(nombres,start=1):
            if nombre_buscado.lower() == nombre.strip().lower():
                print(f"El nombre {nombre_buscado} se encuentra en la linea {linea_numero}")


#creacion de funcion de control para la llamada de funciones
def control_de_archivos(seleccion,contador):
    if seleccion == 1:
        agregar_nombres(contador)
        
    elif seleccion == 2 or seleccion == 3:
        try:
            if seleccion == 2 :
                mostrar_nombres()
            else:
                buscar_nombres() 
        except:
            print("\nArchivo de texto no encontrado...")
    else:
        print("Saliendo del programa.")
    
        
#inicio del bucle inicial
    
i = True
contador = 0
while i:

    print("\nSelecciona una opcion: ")
    print("1) Agregar nombre. ")
    print("2) Mostrar nombres. ")
    print("3) Buscar un nombre. ")
    print("4) Salir. \n")
    opcion = int(input("Ingresa tu opcion: "))
    
    #llamada a funcion de control
    control_de_archivos(opcion,contador)
    
    contador += 1
    #iterador cambia a falso si el usuario elige la opcion 4
    if opcion == 4:
        i = False
    
    


