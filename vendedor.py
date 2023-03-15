import generador as gen, itertools
from producto import lista_productos, Producto
from cliente import lista_clientes, Cliente
from bodega import bodega, sucursal

class Vendedor(): 
    run: str
    nombre: str
    apellido: str
    seccion: str
    __comision: float = 0
    destacado: bool 
   
    def __init__(self, nombre, apellido, seccion, destacado): 
        self.run = gen.generar_rut(1,26)
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.seccion = seccion.title()
        self.destacado = destacado
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} / RUN: {self.run}'

    def mostrar_datos(self):
        return f'{self.nombre} {self.apellido} / RUN: {self.run} Sección: {self.seccion} / Comisión: {self.__comision}'
    
    def agregar_comision(self, total_neto: int):
        self.__comision += total_neto * 0.05
    
    def vender(self, orden_compra): 

        precio_total = orden_compra.producto.calcular_total(orden_compra.cantidad_producto) # Se calcula el precio total de la compra

        if not orden_compra.cliente.verificar_saldo(precio_total): return gen.warning("Cliente no tiene saldo suficiente para realizar la compra.") # Se verifíca si el cliente tiene el saldo necesario

        orden_compra.cliente.disminuir_saldo(precio_total) # Se resta el total de la compra al saldo del cliente
        self.agregar_comision(orden_compra.producto.valor_neto * orden_compra.cantidad_producto) # Se le suma la comisión de la venta al vendedor
        orden_compra.producto.disminuir_stock(orden_compra.cantidad_producto) # Se resta las unidades vendidas al stock del producto
        sucursal.restar_stock(orden_compra.cantidad_producto) # Se resta unidades de productos vendidas a la sucursal
        lista_compras.append(orden_compra) # Se guarda la compra en una lista

        return f'{gen.success("¡Venta Realizada Correctamente!")} \n {gen.color("Detalle: ")} \n {orden_compra}'

class OrdenCompra():
    id: int
    producto: Producto
    cantidad_producto: int
    vendedor: Vendedor
    cliente: Cliente
    despacho: bool

    nueva_id = itertools.count()

    def __init__(self, producto, cantidad_producto, vendedor, cliente, despacho) -> None:
        self.id = next(self.nueva_id)
        self.producto = producto
        self.cantidad_producto = cantidad_producto
        self.vendedor = vendedor
        self.cliente = cliente
        self.despacho = despacho
    
    def calcular_despacho(self):
        return 5000 if self.despacho else 0
    
    def calcular_total(self):
        return self.producto.calcular_total(self.cantidad_producto) + self.calcular_despacho()

    def __str__(self) -> str:
        return f'Vendedor: {self.vendedor} \n Cliente: {self.cliente.nombre_completo} \n Producto: {self.producto.nombre}\n Cantidad: {self.cantidad_producto} \n Valor Neto: ${self.producto.valor_neto*self.cantidad_producto} \n Impuesto: ${self.producto.calcular_impuesto()*self.cantidad_producto} \n Despacho: ${self.calcular_despacho()} \n Total: ${self.calcular_total()}'
    
    

lista_vendedores= [Vendedor('Denis', 'Medina', 'Vestuario', False), 
                   Vendedor('Clemente', 'Medina', 'Vestuario', True), 
                   Vendedor('Mohammed', 'Laoudini', 'Calzado', True), 
                   Vendedor('Ignacio', 'Vera', 'Calzado', False), 
                   Vendedor('Francisco', 'Allende', 'Accesorios', True)]

lista_compras = []

def menu_vendedores():

    while True:
        print(gen.success("Menú Vendedores:"))

        opcion = input(f'{gen.color("1)")} Vendedores\n{gen.color("2)")} Venta\n{gen.warning("0)")} Regresar\n>> ')

        if opcion == '0': break

        elif opcion == '1':
            for vendedor in lista_vendedores:
                print(vendedor.mostrar_datos())

        elif opcion == '2':
                vendedor: Vendedor
                producto: Producto
                cliente: Cliente

                for index, vendedor in enumerate(lista_vendedores, start=1):
                    print(f"{gen.color(f'{index})')} {vendedor}")

                while True:                        
                    opcion_vendedor = int(input(gen.color("Seleccionar Vendedor\n>> ")))
                    validar_opcion = gen.validar(opcion_vendedor, lista_vendedores)

                    if isinstance(validar_opcion, bool):
                        vendedor = lista_vendedores[opcion_vendedor-1]
                        break

                    print(validar_opcion)

                print(gen.color(f"Vendedor: {vendedor.nombre} {vendedor.apellido}"))


                for index, producto in enumerate(lista_productos, start=1):
                    print(f"{gen.color(index)}) {producto}")

                while True:                        
                    opcion_producto = int(input(gen.color("Seleccionar Producto\n>> ")))
                    validar_opcion = gen.validar(opcion_producto, lista_productos)

                    if isinstance(validar_opcion, bool):
                        producto = lista_productos[opcion_producto-1]
                        break
                    print(validar_opcion)

                while True:    
                    cantidad_productos = int(input(gen.color("Ingrese la cantidad\n>> ")))

                    if producto.verificar_stock(cantidad_productos):
                        print(gen.success("¡Si hay stock!"))
                        break

                    print(gen.warning("!No hay stock suficiente!"))


                for index, cliente in enumerate(lista_clientes, start=1):
                    print(f"{gen.color(index)}) {cliente.nombre} {cliente.apellido}")

                while True:                        
                    opcion_cliente = int(input(gen.color("Seleccione el cliente para realizar la venta\n>> ")))
                    validar_opcion = gen.validar(opcion_cliente, lista_clientes)

                    if isinstance(validar_opcion, bool):
                        cliente = lista_clientes[opcion_producto-1]
                        break
                    print(validar_opcion)
                
                while True:                        
                    opcion_cliente = int(input(gen.color(f"¿Necesita despacho?\n {gen.color(1)}) Si\n {gen.color(2)}) No\n>> ")))
                    validar_opcion = gen.validar(opcion_cliente, [1, 2])

                    if isinstance(validar_opcion, bool): break
                    print(validar_opcion)

                print(vendedor.vender(OrdenCompra(producto, cantidad_productos, vendedor, cliente, True if opcion_cliente == 1 else False)))

