import generador as gen
from producto import lista_productos
from cliente import lista_clientes

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
    
    def vender(self, cantidad_productos, producto, cliente): 

        precio_total = producto.calcular_total(cantidad_productos) # Se calcula el precio total de la compra

        if not cliente.verificar_saldo(precio_total): return gen.warning("Cliente no tiene saldo suficiente para realizar la compra.") # Se verifíca si el cliente tiene el saldo necesario

        cliente.disminuir_saldo(precio_total) # Se resta el total de la compra al saldo del cliente
        self.agregar_comision(producto.valor_neto * cantidad_productos) # Se le suma la comisión de la venta al vendedor
        producto.disminuir_stock(cantidad_productos) # Se resta las unidades vendidas al stock del producto

        return f'{gen.success("¡Venta Realizada Correctamente!")} \n {gen.color("Detalle: ")} \n Vendedor: {self.nombre} {self.apellido} \n Cliente: {cliente.nombre} {cliente.apellido} \n Producto: {producto.nombre} ${producto.precio_total()} x {cantidad_productos} \n Total: {precio_total}'



lista_vendedores= [Vendedor('Denis', 'Medina', 'Vestuario', False), 
                   Vendedor('Clemente', 'Medina', 'Vestuario', True), 
                   Vendedor('Mohammed', 'Laoudini', 'Calzado', True), 
                   Vendedor('Ignacio', 'Vera', 'Calzado', False), 
                   Vendedor('Francisco', 'Allende', 'Accesorios', True)]

def menu_vendedores():

    while True:
        print(gen.success("Menú Vendedores:"))

        opcion = input(f'{gen.color("1)")} Vendedores\n{gen.color("2)")} Venta\n{gen.warning("0)")} Regresar\n>> ')

        if opcion == '0': break

        elif opcion == '1':
            for vendedor in lista_vendedores:
                print(vendedor.mostrar_datos())

        elif opcion == '2':
                vendedor : Vendedor

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


                cont=0
                for cliente in lista_clientes:
                    cont+=1
                    nro_cliente = f"{cont})"
                    print(f"{gen.color(nro_cliente)} {cliente.nombre} {cliente.apellido}")


                while True:                        
                    cliente_venta = int(input(gen.color("Seleccione el cliente para realizar la venta\n>> ")))
                    if gen.validar(cliente_venta, lista_clientes)==True:
                        break
                    else: 
                        print(gen.validar(cliente_venta, lista_clientes))

                print(vendedor.vender(cantidad_productos, producto, lista_clientes[cliente_venta-1]))

