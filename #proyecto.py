#proyecto
dic_pacientes = {} #codigo:descripcion
dic_farmacos = {} #codigo:descripcion
dic_insumos_clinicos = {} #codigo:descripcion
productos_terminados = {} #codigo:descripcion
prestaciones_medicas = {} #codigo:descripcion
proveedores = [] #codigo:descripcion
inventario = {}
composiciones = {}  # codigo_producto: lista de (codigo_item, cantidad)
productos_stock = {}  # codigo_producto: cantidad
ordenes_produccion = []  # lista de tuplas (codigo_producto, cantidad)
episodios = []  # lista de episodios (cada uno es un diccionario)
atenciones = []  # lista de atenciones (cada una esta ligada a un episodio por codigo)
op = True

def pacientes():
    print("1) agregar paciente")
    print("2) eliminar paciente")
    print("3) modificar paciente")
    print("4) listar pacientes")
    print("5) buscar paciente")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        edad = input("Ingrese la edad del paciente: ")
        genero = input("Ingrese el genero del paciente: ")
        agregar_a_diccionario(dic_pacientes, nombre, {'edad': edad, 'genero': genero})
    elif opcion == "2":
        nombre = input("Ingrese el nombre del paciente a eliminar: ")
        eliminar_de_diccionario(dic_pacientes, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del paciente a modificar: ")
        nuevonombre  = input("Ingrese el nuevo nombre del paciente: ")
        if nombre in dic_pacientes:
            edad = input("Ingrese la nueva edad del paciente: ")
            genero = input("Ingrese el nuevo genero del paciente: ")
            modificar_en_diccionario(dic_pacientes, nombre, {'edad': edad, 'genero': genero})
        else:
            print(f"Paciente {nombre} no encontrado.")
    elif opcion == "4":
        print("Lista de pacientes:")
        for nombre, datos in dic_pacientes.items():
            print(f"Nombre: {nombre}, Edad: {datos['edad']}, Genero: {datos['genero']}")
    elif opcion == "5":
        nombre = input("Ingrese el nombre del paciente a buscar: ")
        buscar_en_diccionario(dic_pacientes, nombre)
    else:
        print("Opcion no valida. Intente de nuevo.")

def farmacos():
    print("1) agregar farmaco")
    print("2) eliminar farmaco")
    print("3) modificar farmaco")
    print("4) listar farmacos")
    print("5) buscar farmaco")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del farmaco: ")
        cantidad = input("Ingrese la cantidad del farmaco: ")
        agregar_a_diccionario(dic_farmacos, nombre, cantidad)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del farmaco a eliminar: ")
        eliminar_de_diccionario(dic_farmacos, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del farmaco a modificar: ")
        nuevonombre  = input("Ingrese el nuevo nombre del farmaco: ")
        if nombre in dic_farmacos:
            cantidad = input("Ingrese la nueva cantidad del farmaco: ")
            modificar_en_diccionario(dic_farmacos, nombre, cantidad)
        else:
            print(f"Farmaco {nombre} no encontrado.")
    elif opcion == "4":
        print("Lista de farmacos:")
        for nombre, cantidad in dic_farmacos.items():
            print(f"Nombre: {nombre}, Cantidad: {cantidad}")
    elif opcion == "5":
        nombre = input("Ingrese el nombre del farmaco a buscar: ")
        buscar_en_diccionario(dic_farmacos, nombre)
    else:
        print("Opcion no valida. Intente de nuevo.")

def insumos_clinicos():
    print("1) agregar insumo clinico")
    print("2) eliminar insumo clinico")
    print("3) modificar insumo clinico")
    print("4) listar insumos clinicos")
    print("5) buscar insumo clinico")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del insumo clinico: ")
        cantidad = input("Ingrese la cantidad del insumo clinico: ")
        agregar_a_diccionario(dic_insumos_clinicos, nombre, cantidad)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del insumo clinico a eliminar: ")
        eliminar_de_diccionario(dic_insumos_clinicos, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del insumo clinico a modificar: ")
        nuevonombre  = input("Ingrese el nuevo nombre del insumo clinico: ")
        if nombre in dic_insumos_clinicos:
            cantidad = input("Ingrese la nueva cantidad del insumo clinico: ")
            modificar_en_diccionario(dic_insumos_clinicos, nombre, cantidad)
        else:
            print(f"Insumo clinico {nombre} no encontrado.")
    elif opcion == "4":
        print("Lista de insumos clinicos:")
        for nombre, cantidad in dic_insumos_clinicos.items():
            print(f"Nombre: {nombre}, Cantidad: {cantidad}")
    elif opcion == "5":
        nombre = input("Ingrese el nombre del insumo clinico a buscar: ")
        buscar_en_diccionario(dic_insumos_clinicos, nombre)
    else:
        print("Opcion no valida. Intente de nuevo.")

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
    op = True
    while op:
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
            op = False
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

def agregar_a_diccionario(diccionario, clave, valor):
    if clave not in diccionario:
        diccionario[clave] = valor
        print(f"{clave} agregado correctamente.")
    else:
        print(f"{clave} ya existe en el diccionario.")

def eliminar_de_diccionario(diccionario, clave):
    if clave in diccionario:
        del diccionario[clave]
        print(f"{clave} eliminado correctamente.")
    else:
        print(f"{clave} no se encuentra en el diccionario.")

def modificar_en_diccionario(diccionario, clave, nuevo_valor):
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        print(f"{clave} modificado a {nuevo_valor} correctamente.")
    else:
        print(f"{clave} no se encuentra en el diccionario.")

def buscar_en_diccionario(diccionario, clave):
    if clave in diccionario:
        print(f"{clave} encontrado con valor: {diccionario[clave]}")
    else:
        print(f"{clave} no encontrado en el diccionario.")

def listar_diccionario(diccionario):
    if diccionario:
        print("Contenido del diccionario:")
        for clave, valor in diccionario.items():
            print(f"{clave}: {valor}")
    else:
        print("El diccionario está vacío.")

def reporte_farmacos():
    print("Reporte de farmacos:")
    if dic_farmacos:
        for nombre, cantidad in dic_farmacos.items():
            print(f"Nombre: {nombre}, Cantidad: {cantidad}")
    else:
        print("No hay farmacos registrados.")

def obtener_bajo_stock(diccionario):
    bajo_stock = []
    for clave, valor in diccionario.items():
        try:
            if int(valor) < 20:
                bajo_stock.append(clave)
        except ValueError:
            print(f"El valor de {clave} no es un número válido.")
    return bajo_stock

def reporte_bajo_stock():
    print("Fármacos con stock menor a 20:")
    bajos = obtener_bajo_stock(dic_farmacos)
    if bajos:
        for nombre in bajos:
            print(f"- {nombre}")
    else:
        print("No hay fármacos con stock bajo.")

    print("\nInsumos clínicos con stock menor a 20:")
    bajos_insumos = obtener_bajo_stock(dic_insumos_clinicos)
    if bajos_insumos:
        for nombre in bajos_insumos:
            print(f"- {nombre}")
    else:
        print("No hay insumos clínicos con stock bajo.")

def produccion_menu():
    op = True
    while op:
        print('1) Crear composicion de producto terminado')
        print('2) Crear orden de produccion')
        print('3) Ejecutar orden de produccion')
        print('4) Ver stock de productos terminados')
        print('5) Salir')
        opcion = input('Seleccione una opcion: ')

        if opcion == '1':
            codigo = input('Ingrese el codigo del producto terminado: ')
            composiciones[codigo] = []
            cantidad_items = int(input('Cuantos insumos o farmacos usara este producto?: '))
            for i in range(cantidad_items):
                item = input(f'Codigo del item #{i+1}: ')
                cantidad = int(input(f'Cantidad del item #{i+1}: '))
                composiciones[codigo].append((item, cantidad))
            print('Composicion registrada correctamente.')

        elif opcion == '2':
            codigo = input('Ingrese el codigo del producto terminado a producir: ')
            cantidad = int(input('Cantidad a producir: '))
            ordenes_produccion.append((codigo, cantidad))
            print('Orden de produccion registrada.')

        elif opcion == '3':
            for orden in ordenes_produccion:
                codigo_producto = orden[0]
                cantidad_producir = orden[1]

                if codigo_producto in composiciones:
                    for codigo_item, cantidad_usar in composiciones[codigo_producto]:
                        for tipo in ['farmacos', 'insumos']:
                            if codigo_item in inventario[tipo]:
                                inventario[tipo][codigo_item]['cantidad'] -= cantidad_usar * cantidad_producir

                    if codigo_producto in productos_stock:
                        productos_stock[codigo_producto] += cantidad_producir
                    else:
                        productos_stock[codigo_producto] = cantidad_producir

                    print(f'Fabricados {cantidad_producir} de {codigo_producto}.')
                else:
                    print(f'No existe composicion para el producto {codigo_producto}.')

            ordenes_produccion[:] = []  # limpia la lista sin usar .clear()

        elif opcion == '4':
            print('Stock actual de productos terminados:')
            for codigo, cantidad in productos_stock.items():
                print(f'{codigo}: {cantidad} unidades')
        elif opcion == '5':
            print('Volviendo al menu principal')
            op = False




def ventas_menu():
    op = True
    while op:
    print('1) Crear episodio')
    print('2) Agregar atencion a episodio')
    print('3) Calcular precio de atencion')
    print('4) Ver reporte de ventas')
    print('5) Salir')
    opcion = input('Seleccione una opcion: ')

    if opcion == '1':
        codigo = input('Ingrese un codigo unico para el episodio: ')
        paciente = input('Nombre del paciente: ')
        fecha = input('Fecha (dd-mm-aaaa): ')
        episodio = {
            'codigo': codigo,
            'paciente': paciente,
            'fecha': fecha
        }
        episodios.append(episodio)
        print('Episodio creado exitosamente.')

    elif opcion == '2':
        codigo = input('Ingrese el codigo del episodio: ')
        encontrado = False
        for episodio in episodios:
            if episodio['codigo'] == codigo:
                encontrado = True
                cantidad = int(input('Cuantos items desea agregar?: '))
                for i in range(cantidad):
                    print('Tipos disponibles: p=Producto Terminado, f=Farmaco, i=Insumo, m=Prestacion Medica')
                    tipo = input(f'Ingrese tipo del item #{i+1}: ').lower()
                    nombre = input(f'Ingrese nombre del item #{i+1}: ')
                    costo = float(input(f'Ingrese costo del item #{i+1}: '))
                    atencion = {
                        'codigo_episodio': codigo,
                        'tipo': tipo,
                        'nombre': nombre,
                        'costo': costo
                    }
                    atenciones.append(atencion)
                print('Atencion agregada correctamente.')
        if not encontrado:
            print('Episodio no encontrado.')

    elif opcion == '3':
        codigo = input('Ingrese el codigo del episodio: ')
        total_costo = 0
        total_venta = 0

        for atencion in atenciones:
            if atencion['codigo_episodio'] == codigo:
                tipo = atencion['tipo']
                costo = atencion['costo']
                if tipo == 'p':
                    precio = costo / 0.60
                elif tipo == 'f':
                    precio = costo / 0.50
                elif tipo == 'i':
                    precio = costo / 0.40
                elif tipo == 'm':
                    precio = costo / 0.55
                else:
                    precio = 0  # tipo desconocido
                total_costo += costo
                total_venta += precio

        margen = total_venta - total_costo
        print('Costo total: $', round(total_costo, 2))
        print('Precio de venta: $', round(total_venta, 2))
        print('Margen de ganancia: $', round(margen, 2))

    elif opcion == '4':
        fecha_inicio = input('Ingrese fecha de inicio (dd-mm-aaaa): ')
        fecha_fin = input('Ingrese fecha de fin (dd-mm-aaaa): ')

        print('REPORTE DE VENTAS:')
        for episodio in episodios:
            fecha = episodio['fecha']
            if fecha_inicio <= fecha <= fecha_fin:
                codigo = episodio['codigo']
                paciente = episodio['paciente']
                total_costo = 0
                total_venta = 0
                for atencion in atenciones:
                    if atencion['codigo_episodio'] == codigo:
                        tipo = atencion['tipo']
                        costo = atencion['costo']
                        if tipo == 'p':
                            precio = costo / 0.60
                        elif tipo == 'f':
                            precio = costo / 0.50
                        elif tipo == 'i':
                            precio = costo / 0.40
                        elif tipo == 'm':
                            precio = costo / 0.55
                        else:
                            precio = 0
                        total_costo += costo
                        total_venta += precio
                margen = total_venta - total_costo
                print('Codigo:', codigo)
                print('Paciente:', paciente)
                print('  Costo: $', round(total_costo, 2))
                print('  Venta: $', round(total_venta, 2))
                print('  Margen: $', round(margen, 2))
    elif opcion == '5':
            print('Volviendo al menu principal')
            op = False
                
while op:   
    print('Bienvenido')
    print('1.- Menu de mantencion e inventario')
    print('2.- Menu de produccion')
    print('3.- Menu de ventas')
    print('4.- Salir')
    opcion = input('Ingrese su opcion: ')
    match opcion:
        case '1':
            menu()
        case '2':
            produccion_menu()
        case '3':
            ventas_menu()
        case '4':
            print('Gracias por usar nuestros servicios!')
            op = False