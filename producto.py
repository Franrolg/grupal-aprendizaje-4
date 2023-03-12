import generador as gen
from proveedor import Proveedor, proveedores

class Producto():
    sku: int
    nombre: str
    categoria: str
    proveedor: Proveedor
    stock: int
    valor_neto: int
    __impuesto: float = 0.19 # Se guarda el % de impuestos que se cobra, para después realizar cálculo
    color: str 

    def __init__(self, nombre, categoria, proveedor, stock, valor_neto, color): 
        self.sku = str(gen.generar_id(10))
        self.nombre = nombre.title()
        self.categoria = categoria.title()
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.color = color.title()

    def mostrar_productos(self): # método.
        return self.sku, self.nombre, self.color, self.categoria, self.proveedor, self.stock, self.valor_neto, self.__impuesto
    
    def calcular_total(self, cantidad):
        return (self.__impuesto*cantidad)

producto_1 = Producto('Pantalones', 'Vestuario', proveedores[0].mostrar_proveedores(), 300, 1500, 'gris')
producto_2 = Producto('Camisas', 'Vestuario', proveedores[1].mostrar_proveedores(), 300, 1000, 'blanco')
producto_3 = Producto('Zapatos', 'Calzado', proveedores[2].mostrar_proveedores(), 250, 2000, 'cafe')
producto_4 = Producto('Zapatillas', 'Calzado', proveedores[3].mostrar_proveedores(), 250, 3000, 'verde')
producto_5 = Producto('Cinturon', 'Accesorios', proveedores[4].mostrar_proveedores(), 400, 1500, 'negro')

productos = [producto_1, producto_2, producto_3, producto_4, producto_5]

def menu_productos():
    while True:
        
        print(gen.success("Menú Productos:"))
        opcion = input(f'{gen.color("1)")} Productos\n{gen.warning("0)")} Regresar\n>> ')
        if opcion == '0':
            break

        elif opcion == '1':
            for producto in productos:
                print(producto.mostrar_productos())

        else:
            print(gen.warning('Ingresar una opción válida.'))