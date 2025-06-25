#proyecto
paciente = {} #codigo:descripcion
farmacos = {} #codigo:descripcion
insumos_clinicos = {} #codigo:descripcion
productos_terminados = {} #codigo:descripcion
prestaciones_medicas = {} #codigo:descripcion
proveedores = {} #codigo:descripcion
inventario = {}
composiciones = {}
productos_stock = {}
ordenes_produccion = []

def produccion_menu():
    print('1.- Crear composicion de producto terminado')
    print('2.- Crear orden de produccion')
    print('3.- Ejecutar orden de produccion')
    print('4.- Reporte de stock de productos terminados')
    opcion = input('Seleccione una opcion: ')

    if opcion == '1':
        codigo = input('Codigo del producto terminado: ')
        composiciones[codigo] = []
        cantidad_items = int(input('¿Cuantos insumos o farmacos usara este producto?: '))
        for i in range(cantidad_items):
            item = input(f'Codigo del insumo o farmaco, numero {i+1}: ')
            cantidad = int(input(f'Cantidad a usar del item, numero{i+1}: '))
            composiciones[codigo].append((item, cantidad))
        print('Composición realizada')
    elif opcion == '2':
        producto = input('Codigo del producto terminado a producir: ')
        cantidad = int(input('Cantidad a producir: '))
        ordenes_produccion.append((producto, cantidad))
        print('Orden de produccion realizada')
    elif opcion == '3':
        for producto, cantidad in ordenes_produccion:
            if producto in composiciones:
                for codigo_insumo, cant in composiciones[producto]:
                    for tipo in ["farmacos", "insumos"]:
                        if codigo_insumo in inventario[tipo]:
                            inventario[tipo][codigo_insumo]['cantidad'] -= cant * cantidad
                if producto in productos_stock:
                    productos_stock[producto] += cantidad
                else:
                    productos_stock[producto] = cantidad
                print(f"Fabricados {cantidad} de {producto}.")
            else:
                print(f"No hay composición definida para {producto}.")
        ordenes_produccion.clear()
    elif opcion == '4':
        print('Stock de productos terminados:')
        for codigo, cantidad in productos_stock.items():
            print(f"{codigo}: {cantidad} unidades")
