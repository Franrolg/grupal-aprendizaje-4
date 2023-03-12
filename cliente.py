import generador as gen


class Cliente(): # definición de la clase y sus atributos.
    id: str
    nombre: str
    apellido: str
    correo: str
    fecha_registro: str
    __saldo: int
    premium: bool # éste es el nuevo atributo.

    def __init__(self, nombre, apellido, fecha_registro, premium): # constructor de la clase.
        self.id = gen.generar_id(8)
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.correo = nombre + '.' + apellido + '@gmail.com'
        self.fecha_registro = fecha_registro
        self.__saldo = 100000

        if premium == True:
            premium = 'cliente premium'

        else:
            premium = ''

        self.premium = premium.title()


    def agregar_saldo(self): # método.
        saldo_agregar = input(f'Ingresar saldo para {self.nombre}: ')
        self.__saldo += int(saldo_agregar)

    def disminuir_saldo(self, saldo_disminuir): # método.
        if self.__saldo < saldo_disminuir:
            print(gen.warning("Cliente no tiene saldo suficiente para realizar la compra."))
            return False
        else:
            self.__saldo -= saldo_disminuir
            return True
        
    def mostrar_saldo(self): # método.
        print(f"{self.nombre} tiene un saldo de: ${self.__saldo}")

    def mostrar_clientes(self): # método.
        cliente = [self.nombre, self.apellido, self.fecha_registro, self.__saldo]

        if self.premium != '':
            cliente.append(self.premium)

        return(cliente)

cliente_1 = Cliente('Eduardo', 'Castro', '11/12/2022', True)
cliente_2 = Cliente('Felipe', 'Soto', '11/11/2021', False)
cliente_3 = Cliente('Andrea', 'Oyarce','05/11/2020', True)
cliente_4 = Cliente('Esteban', 'Lopez', '06/10/2021', True)
cliente_5 = Cliente('Claudio', 'Alarcon', '20/11/2020', False)

clientes = [cliente_1, cliente_2, cliente_3, cliente_4, cliente_5]

def menu_clientes():
    while True:

        print(gen.success("Menú Clientes:"))
        opcion = input(f'{gen.color("1)")} Agregar saldo\n{gen.color("2)")} Saldo\n{gen.color("3)")} Clientes\n{gen.warning("0)")} Regresar\n>> ')

        if opcion == '0':
            break

        elif opcion == '1':
            print(gen.success('Agregar Saldo'))
            nombre = input('Ingrese Nombre: ')

            for x in clientes:

                if x.nombre == nombre.capitalize():
                    x.agregar_saldo()
            
        elif opcion == '2':
            print(gen.success('Saldo'))
            nombre = input('Ingrese Nombre: ')
            for x in clientes:
                if x.nombre == nombre.capitalize():
                    x.mostrar_saldo()  

        elif opcion == '3':
            for cliente in clientes:
                print(cliente.mostrar_clientes())

        else:
            print(gen.warning('Ingresar una opción válida.'))