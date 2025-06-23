#proyecto
pacientes = {}
farmacos = {}
insumos_clinicos = []
productos_terminados = []
prestaciones_medicas = []
provedores = []
def pacientes():
    print("1) agregar paciente")
    print("2) eliminar paciente")
    print("3) modificar paciente")
    print("4) listar pacientes")
    print("5) buscar paciente")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        agregar_a_lista(pacientes, nombre)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del paciente a eliminar: ")
        eliminar_de_lista(pacientes, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del paciente a modificar: ")
        nuevonombre  = input("Ingrese el nuevo nombre del paciente: ")
        modificar_en_lista(pacientes, nombre, nuevonombre)
    elif opcion == "4":
        print("Lista de pacientes:")
        for paciente in pacientes:
            print(paciente)
    elif opcion == "5":
        nombre = input("Ingrese el nombre del paciente a buscar: ")
        if nombre in pacientes:
            print(f"Paciente {nombre} encontrado.")
        else:
            print(f"Paciente {nombre} no encontrado.")
def farmacos():
    print("1) agregar farmaco")
    print("2) eliminar farmaco")
    print("3) modificar farmaco")
    print("4) listar farmacos")
    print("5) buscar farmaco")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del farmaco: ")
        agregar_a_lista(farmacos, nombre)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del farmaco a eliminar: ")
        eliminar_de_lista(farmacos, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del farmaco a modificar: ")
        nuevonombre  = input("Ingrese el nuevo nombre del farmaco: ")
        modificar_en_lista(farmacos, nombre, nuevonombre)
    elif opcion == "4":
        print("Lista de farmacos:")
        for farmaco in farmacos:
            print(farmaco)
    elif opcion == "5":
        nombre = input("Ingrese el nombre del farmaco a buscar: ")
        if nombre in farmacos:
            print(f"Farmaco {nombre} encontrado.")
        else:
            print(f"Farmaco {nombre} no encontrado.")

def insumos_clinicos():
    print("1) agregar insumo clinico")
    print("2) eliminar insumo clinico")
    print("3) modificar insumo clinico")
    print("4) listar insumos clinicos")
    print("5) buscar insumo clinico")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del insumo clinico: ")
        agregar_a_lista(insumos_clinicos, nombre)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del insumo clinico a eliminar: ")
        eliminar_de_lista(insumos_clinicos, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del insumo clinico a modificar: ")
        nuevonombre  = input("Ingrese el nuevo nombre del insumo clinico: ")
        modificar_en_lista(insumos_clinicos, nombre, nuevonombre)
    elif opcion == "4":
        print("Lista de insumos clinicos:")
        for insumo in insumos_clinicos:
            print(insumo)   
    elif opcion == "5":
        nombre = input("Ingrese el nombre del insumo clinico a buscar: ")
        if nombre in insumos_clinicos:
            print(f"Insumo clinico {nombre} encontrado.")
        else:
            print(f"Insumo clinico {nombre} no encontrado.")

def productos_terminados():
    print("1) agregar producto terminado")
    print("2) eliminar producto terminado")
    print("3) modificar producto terminado")
    print("4) listar productos terminados")
    print("5) buscar producto terminado")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto terminado: ")
        agregar_a_lista(productos_terminados, nombre)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto terminado a eliminar: ")
        eliminar_de_lista(productos_terminados, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto terminado a modificar: ")
        nuevonombre  = input("Ingrese el nuevo nombre del producto terminado: ")
        modificar_en_lista(productos_terminados, nombre, nuevonombre)
    elif opcion == "4":
        print("Lista de productos terminados:")
        for producto in productos_terminados:
            print(producto)
    elif opcion == "5":
        nombre = input("Ingrese el nombre del producto terminado a buscar: ")
        if nombre in productos_terminados:
            print(f"Producto terminado {nombre} encontrado.")
        else:
            print(f"Producto terminado {nombre} no encontrado.")
def prestaciones_medicas():
    print("1) agregar prestacion medica")
    print("2) eliminar prestacion medica")
    print("3) modificar prestacion medica")
    print("4) listar prestaciones medicas")
    print("5) buscar prestacion medica")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre de la prestacion medica: ")
        agregar_a_lista(prestaciones_medicas, nombre)
    elif opcion == "2":
        nombre = input("Ingrese el nombre de la prestacion medica a eliminar: ")
        eliminar_de_lista(prestaciones_medicas, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre de la prestacion medica a modificar: ")
        nuevonombre  = input("Ingrese el nuevo nombre de la prestacion medica: ")
        modificar_en_lista(prestaciones_medicas, nombre, nuevonombre)
    elif opcion == "4":
        print("Lista de prestaciones medicas:")
        for prestacion in prestaciones_medicas:
            print(prestacion)
    elif opcion == "5":
        nombre = input("Ingrese el nombre de la prestacion medica a buscar: ")
        if nombre in prestaciones_medicas:
            print(f"Prestacion medica {nombre} encontrada.")
        else:
            print(f"Prestacion medica {nombre} no encontrada.")
def provedores():
    print("1) agregar provedor")
    print("2) eliminar provedor")
    print("3) modificar provedor")
    print("4) listar provedores")
    print("5) buscar provedor")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del provedor: ")
        agregar_a_lista(provedores, nombre)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del provedor a eliminar: ")
        eliminar_de_lista(provedores, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del provedor a modificar: ")
        nuevonombre  = input("Ingrese el nuevo nombre del provedor: ")
        modificar_en_lista(provedores, nombre, nuevonombre)
    elif opcion == "4":
        print("Lista de provedores:")
        for provedor in provedores:
            print(provedor)
def menu():
    print("Menu de gestion de datos:")
    print("1) Gestionar pacientes")
    print("2) Gestionar farmacos")
    print("3) Gestionar insumos clinicos")
    print("4) Gestionar productos terminados")
    print("5) Gestionar prestaciones medicas")
    print("6) Gestionar provedores")
    print("7) Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        pacientes()
    elif opcion == "2":
        farmacos()
    elif opcion == "3":
        insumos_clinicos()
    elif opcion == "4":
        productos_terminados()
    elif opcion == "5":
        prestaciones_medicas()
    elif opcion == "6":
        provedores()
    elif opcion == "7":
        print("Saliendo del programa.")
        return
    else:
        print("Opcion no valida. Intente de nuevo.")
def agregar_a_lista(lista, item):
    if item not in lista:
        lista.append(item)
        print(f"{item} agregado correctamente.")
    else:
        print(f"{item} ya existe en la lista.")
def eliminar_de_lista(lista, item):
    if item in lista:
        lista.remove(item)
        print(f"{item} eliminado correctamente.")
    else:
        print(f"{item} no se encuentra en la lista.")
def modificar_en_lista(lista, old_item, new_item):
    if old_item in lista:
        index = lista.index(old_item)
        lista[index] = new_item
        print(f"{old_item} modificado a {new_item} correctamente.")
    else:
        print(f"{old_item} no se encuentra en la lista.")
