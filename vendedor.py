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

    def mostrar_vendedores(self):
        vendedor = [self.run, self.nombre, self.apellido, self.seccion, self.__comision]
        
        if self.destacado != '':
            vendedor.append(self.destacado)
        return (vendedor)
    
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

vendedor_1 = Vendedor('Denis', 'Medina', 'Vestuario', False)
vendedor_2 = Vendedor('Clemente', 'Medina', 'Vestuario', True)
vendedor_3 = Vendedor('Mohammed', 'Laoudini', 'Calzado', True)
vendedor_4 = Vendedor('Ignacio', 'Vera', 'Calzado', False)
vendedor_5 = Vendedor('Francisco', 'Allende', 'Accesorios', True)

vendedores= [vendedor_1, vendedor_2, vendedor_3, vendedor_4, vendedor_5]

def menu_vendedores():
    while True:
        print(gen.success("Menú Vendedores:"))
        opcion = input(f'{gen.color("1)")} Vendedores\n{gen.color("2)")} Venta\n{gen.warning("0)")} Regresar\n>> ')
        if opcion == '0':
            break

        elif opcion == '1':
            for vendedor in vendedores:
                objeto = vendedor.mostrar_vendedores()
                print(f"{objeto[1]} {objeto[2]} | RUT:{objeto[0]} | Sección: {objeto[3]} | Comisión: {objeto[4]}")

        elif opcion == '2':
                cont_v = 0
                for vendedor in vendedores:
                    cont_v+=1
                    nro_vendedor = f"{cont_v})"
                    objeto = vendedor.mostrar_vendedores()
                    print(f"{gen.color(nro_vendedor)} {objeto[1]} {objeto[2]} | RUT:{objeto[0]}")


                while True:                        
                    vendedor_venta = int(input(gen.color("Seleccionar Vendedor\n>> ")))

                    if gen.validar(vendedor_venta, vendedores)==True:
                        break
                    else: 
                        print(gen.validar(vendedor_venta, vendedores))


                select_vendedor = f"Vendedor: {vendedores[int(vendedor_venta)-1].nombre} {vendedores[int(vendedor_venta)-1].apellido}"
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
                vendedores[int(vendedor_venta)-1].vender(cantidad, lista_productos[producto_venta-1], lista_clientes[cliente_venta-1])

