import generador as gen
from proveedor import Proveedor, lista_proveedores

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
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} / Categoría: {self.categoria} / Proveedor: {self.proveedor.nombre_legal} / Stock: {self.stock} / Precio: ${self.precio_total()}'

    def precio_total(self):
        return self.valor_neto + int(self.valor_neto * self.__impuesto)
    
    def calcular_total(self, cantidad):
        return self.precio_total() * cantidad
    
    def disminuir_stock(self, unidades):
        self.stock -= unidades

lista_productos = [Producto('Pantalones', 'Vestuario', lista_proveedores[0], 300, 1500, 'gris'), 
                   Producto('Camisas', 'Vestuario', lista_proveedores[1], 300, 1000, 'blanco'), 
                   Producto('Zapatos', 'Calzado', lista_proveedores[2], 250, 2000, 'cafe'), 
                   Producto('Zapatillas', 'Calzado', lista_proveedores[3], 250, 3000, 'verde'), 
                   Producto('Cinturon', 'Accesorios', lista_proveedores[4], 400, 1500, 'negro')]

def menu_productos():
    while True:
        
        print(gen.success("Menú Productos:"))
        opcion = input(f'{gen.color("1)")} Productos\n{gen.warning("0)")} Regresar\n>> ')
        if opcion == '0': break

        elif opcion == '1':
            for producto in lista_productos: print(producto)

        else:
            print(gen.warning('Ingresar una opción válida.'))