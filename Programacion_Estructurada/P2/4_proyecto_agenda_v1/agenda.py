def agregar_contacto(agenda):
    print("Agregar contactos")
    nombre = input("Nombre: ").upper().strip()
    tel = input("Teléfono: ").upper().strip()
    email = input("Email: ").lower().strip()
    if nombre in agenda:
        print("Este contacto ya existe")
    else:
        agenda[nombre] = (tel, email)
        print("Contacto agregado correctamente")


def mostrar_contacto(agenda):
    print("Mostrar contactos")
    if not agenda:
        print("No hay contactos en la agenda")
    else:
        print(f"{'NOMBRE':<15} {'TELÉFONO':<15} {'EMAIL':<20}")
        for nombre, datos in agenda.items():
            tel, email = datos
            print(f"{nombre:<15} {tel:<15} {email:<20}")


def buscar_contacto(agenda):
    borrarPantalla()
        print("Modififcar contacto")
        if not agenda:
        print("No hay contacctos en la agenda")
        else:
        nombre=input("Nombre del contacto a buscar").upper().strip()
    if nombre in agenda:
        print("Valores actuales")
        print(f"\nNombre: {nombre}\nTeléfono: {tel}\nEmail: {email}" {agenda [nombre][1]}"))
        resp=input("Desea cambiar los calores si no").lower().strip()
        if resp="Si":
    tel=input("Telefono: ").upper().strip()
    email=input("Telefono: ").lower().strip()
    agenda[nombre]=[tel, email]
    print("Accion realizada con exito")
    else:
        print("El contacto no existe")
        

        def borrar_contacto(agenda):
    borrarPantalla()
        print("Modififcar contacto")
        if not agenda:
        print("No hay contacctos en la agenda")
        else:
        nombre=input("Nombre del contacto a buscar").upper().strip()
    if nombre in agenda:
        print("Valores actuales")
        print(f"\nNombre: {nombre}\nTeléfono: {tel}\nEmail: {email}" {agenda [nombre][1]}"))
        resp=input("Desea cambiar los calores si no").lower().strip()
        if resp="Si":
    agenda.pop(nombre)
    print("Accion realizada con exito")
    else:
        print("El contacto no existe")


def modificar_contacto(agenda):
    print("Modificar contacto")
    nombre = input("Nombre del contacto que desea modificar: ").upper().strip()
    if nombre in agenda:
     .   tel, email = agenda[nombre]
        nuevo_nombre = input("Ingrese el nuevo nombre (dejar en blanco si no desea cambiar): ").upper().strip()
        nuevo_tel = input("Ingrese el nuevo teléfono (dejar en blanco si no desea cambiar): ").upper().strip()
        nuevo_email = input("Ingrese el nuevo email (dejar en blanco si no desea cambiar): ").lower().strip()



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
    
