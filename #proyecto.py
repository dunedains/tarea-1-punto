#proyecto
paciente = {} #codigo:descripcion
farmacos = {} #codigo:descripcion
insumos_clinicos = {} #codigo:descripcion
productos_terminados = {} #codigo:descripcion
prestaciones_medicas = {} #codigo:descripcion
proveedores = {} #codigo:descripcion
inventario = {}
composiciones = {}  # codigo_producto: lista de (codigo_item, cantidad)
productos_stock = {}  # codigo_producto: cantidad
ordenes_produccion = []  # lista de tuplas (codigo_producto, cantidad)

def produccion_menu():
    print('1) Crear composicion de producto terminado')
    print('2) Crear orden de produccion')
    print('3) Ejecutar orden de produccion')
    print('4) Ver stock de productos terminados')
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


episodios = []  # lista de episodios (cada uno es un diccionario)
atenciones = []  # lista de atenciones (cada una esta ligada a un episodio por codigo)

def ventas_menu():
    print('1) Crear episodio')
    print('2) Agregar atencion a episodio')
    print('3) Calcular precio de atencion')
    print('4) Ver reporte de ventas')
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

    