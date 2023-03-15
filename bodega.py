import generador as gen, time

class Bodega():
    nombre: str
    __stock: int

    def __init__(self, nombre, stock) -> None:
        self.nombre = nombre
        self.__stock = stock
    
    def stock_disponible(self) -> int:
        return self.__stock
    
    def validar_stock(self, cantidad) -> bool:
        return True if cantidad <= self.stock_disponible() else False
            
    def restar_stock(self, cantidad) -> None:
        self.__stock -= cantidad
    
    def agregar_stock(self, cantidad) -> None:
        self.__stock += cantidad

class Sucursal(Bodega):
    direccion: str

    def __init__(self, nombre, stock, direccion) -> None:
        super().__init__(nombre, stock)
        self.direccion = direccion
    
    def validar_stock(self) -> bool:
        return True if self.stock_disponible() >= 50 else False

bodega = Bodega('Bodega A', 823)
sucursal = Sucursal('Sucursal A', 100, 'Avenida Pajaritos')

def menu_sucursal():
    print(gen.success("Menú Sucursal:"))

    if not sucursal.validar_stock(): 
        print(gen.warning('La sucursal cuenta con un stock menor a 50 productos: Se está solicitando productos a bodega'))
        stock_en_bodega = bodega.validar_stock(300)

        time.sleep(2)

        if not stock_en_bodega: print(gen.warning('No existe stock suficiente para reponer'))
        else: 
            print(gen.color('Reponiendo productos..'))

            time.sleep(2)

            bodega.restar_stock(300)
            sucursal.agregar_stock(300)
        
    print(gen.color(f"La sucursal cuenta con un stock de {sucursal.stock_disponible()} productos"))