import generador as gen

class Proveedor():
    rut: str
    nombre_legal: str
    razon_social: str
    pais: str
    persona_juridica: bool

    def __init__(self, nombre_legal, razon_social, pais, persona_juridica):
        self.rut = gen.generar_rut(1,77)
        self.nombre_legal = nombre_legal.title()
        self.razon_social = razon_social.title()
        self.pais = pais.title()
        self.persona_juridica = persona_juridica
    
    def __str__(self) -> str:
        return f'RUT: {self.rut} / Nombre Legal: {self.nombre_legal} / Razón Social: {self.razon_social} / Pais: {self.pais} / Persona Jurídica: {"Si" if self.persona_juridica else "No"}'

    def mostrar_proveedores(self):
        return self.rut, self.nombre_legal, self.razon_social, self.pais, self.persona_juridica

lista_proveedores = [Proveedor('Levis', 'venta de pantalones', 'usa', True), 
                     Proveedor('Skiway', 'fabricacion de camisas', 'chile', False), 
                     Proveedor('Poloni', 'venta de zapatos', 'chile', True), 
                     Proveedor('Nike', 'importacion de zapatillas', 'china', False), 
                     Proveedor('Diesel', 'importacion de cinturones', 'brasil', True)]

def menu_proveedores():

    while True:
        print(gen.success("Menú Proveedores:"))

        opcion = input(f'{gen.color("1)")} Proveedores\n{gen.warning("0)")} Regresar\n>> ')

        if opcion == '0': break

        elif opcion == '1': 
            for proveedor in lista_proveedores: print(proveedor)

        else:
            print(gen.warning('Ingresar una opción válida.'))