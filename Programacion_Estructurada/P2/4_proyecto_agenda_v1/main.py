import agenda

agenda_contactos = {}

opcion = True

while opcion:
    
    print("\n\t\t\t .:::Gestion de peliculas::: \n\n\t "
          "1.-agregar\n\n\t 2.-mostra \n\t 3.-buscar\n\t 4.-borrar c \n\t")
    eleccion = input("\n\n\t Elige una opción: ").upper()

    if eleccion == "1":
        agenda.agregar_contacto(agenda_contactos)
        agenda.espereTecla()
    elif eleccion == "2":
        agenda.mostrar_contactos(agenda_contactos)
        agenda.espereTecla()
    elif eleccion == "3":
        agenda.buscar_contactos(agenda_contactos)
        agenda.espereTecla()
    elif eleccion == "4":
        agenda.buscar_contacto(agenda_contactos)
        agenda.espereTecla()
    elif eleccion == "5":
        opcion = False
        print("\n\t Terminaste la ejecución del sistema. Gracias")

# CORRECCIÓN DE ERROR en print y nombre mal escrito:
print("📒 ::: Sistema de gestión de agenda de contactos ::: 📒")
print("1️⃣ Agregar contacto")
print("2️⃣ Mostrar todos los contactos")
print("3️⃣ Buscar contacto por nombre")
print("4️⃣ Salir")
print("👉 Elige una opción (1-4): ")

opcion = input("👉 Elige una opción (1-4): ")
print("agregar contactos")
nombre = input("Nombre: ").upper().strip()
tel = input("Telefono: ").upper().strip()
email = input("Email: ").lower().strip()

