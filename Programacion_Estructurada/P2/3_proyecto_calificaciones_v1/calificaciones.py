lista={
  ["ruben"], 10.0, 10.0, 10.0,
   ["andres"], 8.0, 9.0, 6.0,
}

def borrarPantalla():
  import os  
  os.system("cls")
  
def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input() 

def menu_principal():
    print("\n\t\t\t .:::Gestion de peliculas::: \n\n\t "
    "¨1.-Crear \n\n\t 2.-Borrar \n\t 3.-Mostrar \n\t 4.-Agregar caracteristicas \n\t"
    "5.-modificar caracteristica \n\t 6.-borrar caracteristica \n\t 7.-Salir")
    opcion=input("\n\n\t Elige una opción: ").upper()
    return opcion
  
