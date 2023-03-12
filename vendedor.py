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
    
    def vender(self, cant, producto, cliente): # éste es el nuevo método.
        disminuir = producto.calcular_total(cant)
        if cliente.verificar_saldo(disminuir):
            cliente.disminuir_saldo(disminuir)
            self.__comision += (producto.valor_neto * cant) * 0.05
            producto.stock -= cant
            print(gen.success("¡Venta Realizada Correctamente!"))
            print(gen.color("Detalle: "), f"Vendedor: {self.nombre} {self.apellido} | Cliente: {cliente.nombre} {cliente.apellido} | Producto: {producto.nombre} {producto.valor_neto*1.19} x {cant} | Total: {disminuir}")
        else:
            print(gen.warning("Cliente no tiene saldo suficiente para realizar la compra."))

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
                for index, vendedor in enumerate(lista_vendedores, start=1):
                    print(f"{gen.color(f'{index})')} {vendedor}")


                while True:                        
                    vendedor_venta = int(input(gen.color("Seleccionar Vendedor\n>> ")))

                    if gen.validar(vendedor_venta, lista_vendedores)==True:
                        break
                    else: 
                        print(gen.validar(vendedor_venta, lista_vendedores))


                select_vendedor = f"Vendedor: {lista_vendedores[int(vendedor_venta)-1].nombre} {lista_vendedores[int(vendedor_venta)-1].apellido}"
                print(gen.color(select_vendedor))


                cont_p=0
                for producto in lista_productos:
                    cont_p+=1
                    nro_producto = f"{cont_p})"
                    print(f"{gen.color(nro_producto)} {producto.nombre} ${producto.valor_neto} Stock:{producto.stock}")

                while True:                        
                    producto_venta = int(input(gen.color("Seleccionar Producto\n>> ")))
                    if gen.validar(producto_venta, lista_productos)==True:
                        break
                    else: 
                        print(gen.validar(producto_venta, lista_productos))

                cantidad = int(input(gen.color("Ingrese la cantidad\n>> ")))
                if cantidad <= lista_productos[producto_venta-1].stock:
                    print(gen.success("¡Si hay Stock!"))
                else:
                    print(gen.warning("!No hay Stock Suficiente!"))
                    break

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
                lista_vendedores[int(vendedor_venta)-1].vender(cantidad, lista_productos[producto_venta-1], lista_clientes[cliente_venta-1])

