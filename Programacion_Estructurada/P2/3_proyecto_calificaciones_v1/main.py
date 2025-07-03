'''
Crear un proyecto que permita gestionar (administrar) peliculas
Colocar un menú de opciones para agregar, borrar, modificara
mostrar, buscar, limpiar una lista de peliculas

notas:
1.-Utilizar funciones y mandar llamar desde otro 
archivo (modelo)
2.-Utilizar listas par almacenar los nombres de peliculas
3.- Utilizar dict para almacenar los atributos
nombre categoria clasificacion genero idioma de peliculas
'''

import calificaciones

datos=[]


opcion=True

while opcion:
    calificaciones.borrarPantalla()
    calificaciones.menu_principal()
    
    print("\n\t\t\t .:::Gestion de peliculas::: \n\n\t "
    "¨1.-Crear \n\n\t 2.-Borrar \n\t 3.-Mostrar \n\t 4.-Agregar caracteristicas \n\t"
    "5.-modificar caracteristica \n\t 6.-borrar caracteristica \n\t 7.-Salir")
    opcion=input("\n\n\t Elige una opción: ").upper()

    match opcion:
        case"1":
            calificaciones.mostrarCalificaciones()
            calificaciones.espereTecla()
        case"2":
            calificaciones.agregarCalificaciones()
            calificaciones.espereTecla()
        case"3":
            calificaciones.calcularPromedios()
            calificaciones.espereTecla()
        
        case"4":
           opcion=False
           print("\n\t Terminaste la ejecución del sistema. Gracias")
        case    _:
            print("\n\t Opción invalida vuelva a intentar")

