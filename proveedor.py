from generador import generar_rut, color, warning, success

class Proveedor(): # ésta es la nueva clase y sus atributos.
    run: str
    rut: str
    nombre_legal: str
    razon_social: str
    pais: str
    p_juridica: bool

    def __init__(self, nombre_legal, razon_social, pais, p_juridica): # constructor de la clase.
        self.rut = generar_rut(1,77)
        self.nombre_legal = nombre_legal.title()
        self.razon_social = razon_social.title()
        self.pais = pais.title()

        if p_juridica == True:
            p_juridica = 'persona jurídica'
            
        else:
            p_juridica = 'persona natural'

        self.p_juridica = p_juridica.title()

    def mostrar_proveedores(self): # método.
        return self.rut, self.nombre_legal, self.razon_social, self.pais, self.p_juridica

proveedor_1 = Proveedor('Levis', 'venta de pantalones', 'usa', True)
proveedor_2 = Proveedor('Skiway', 'fabricacion de camisas', 'chile', False)
proveedor_3 = Proveedor('Poloni', 'venta de zapatos', 'chile', True)
proveedor_4 = Proveedor('Nike', 'importacion de zapatillas', 'china', False)
proveedor_5 = Proveedor('Diesel', 'importacion de cinturones', 'brasil', True)

proveedores = [proveedor_1, proveedor_2, proveedor_3, proveedor_4, proveedor_5]

def menu_proveedores():
    while True:
        print(success("Menú Proveedores:"))
        opcion = input(f'{color("1)")} Proveedores\n{warning("0)")} Regresar\n>> ')
        if opcion == '0':
            break
        elif opcion == '1':
            for proveedor in proveedores:
                print(proveedor.mostrar_proveedores())
        else:
            print(warning('Ingresar una opción válida.'))