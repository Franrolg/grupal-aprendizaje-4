import generador as gen

class Cliente(): 
    id: str
    nombre: str
    apellido: str
    correo: str
    fecha_registro: str
    __saldo: int = 100000
    premium: bool 

    def __init__(self, nombre, apellido, fecha_registro, premium):
        self.id = gen.generar_id(8)
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.correo = nombre + '.' + apellido + '@gmail.com'
        self.fecha_registro = fecha_registro
        self.premium = premium
        self.nombre_completo = f'{self.nombre} {self.apellido}'

    def agregar_saldo(self, saldo_agregar): 
        self.__saldo += saldo_agregar

    def disminuir_saldo(self, saldo_disminuir):
        self.__saldo -= saldo_disminuir

    def verificar_saldo(self, saldo_disminuir):
        return True if self.__saldo >= saldo_disminuir else False # True si hay saldo suficiente, False si no hay saldo suficiente
        
    def mostrar_saldo(self): # método.
        print(f"{self.nombre} tiene un saldo de: ${self.__saldo}")
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} {self.apellido} / Registro: {self.fecha_registro} / Saldo: {self.__saldo} / Cliente Premium: {"Si" if self.premium else "No"}'

datos_clientes = [
    {'nombre': 'Eduardo', 'apellido': 'Castro', 'fecha_registro': '11/12/2022', 'premium': True},
    {'nombre': 'Felipe', 'apellido': 'Soto', 'fecha_registro': '11/11/2021', 'premium': False},
    {'nombre': 'Andrea', 'apellido': 'Oyarce', 'fecha_registro': '05/11/2020', 'premium': True},
    {'nombre': 'Esteban', 'apellido': 'Lopez', 'fecha_registro': '06/10/2021', 'premium': True},
    {'nombre': 'Claudio', 'apellido': 'Alarcon', 'fecha_registro': '20/11/2020', 'premium': False} 
    ]

lista_clientes = [Cliente(cliente['nombre'], cliente['apellido'], cliente['fecha_registro'], cliente['premium']) for cliente in datos_clientes]

def buscar_cliente():
    while True: # Ciclo para validar si existe cliente con nombre ingresado
        nombre = input('Ingrese Nombre: ')
        for cliente in lista_clientes: 
             if cliente.nombre == nombre.capitalize(): return cliente # Si encuentra cliente con ese nombre, lo retorna
        print(gen.warning('No se encontró el cliente ingresado.')) # Si no encuentra cliente, envía el print y se repite el ciclo

def menu_clientes():
    while True:

        print(gen.success("Menú Clientes:"))
        opcion = input(f'{gen.color("1)")} Agregar saldo\n{gen.color("2)")} Saldo\n{gen.color("3)")} Clientes\n{gen.warning("0)")} Regresar\n>> ')

        if opcion == '0': break

        elif opcion == '1':
            print(gen.success('Agregar Saldo'))
            
            cliente = buscar_cliente() # Se busca cliente según nombre ingresado

            while True: # Ciclo para validar saldo ingresado
                saldo = input(f'Ingresar saldo para {cliente.nombre}: ') # Se pregunta saldo a ingresar
                if saldo.isnumeric(): break # Si el valor ingresado es un número, termina el ciclo while
                print(gen.warning('Debe ingresar solo números.')) # Si el valor no es número, se imprime este mensaje y hace de nuevo el ciclo

            cliente.agregar_saldo(int(saldo)) # Se agrega saldo a cliente
            
        elif opcion == '2':
            print(gen.success('Saldo'))

            buscar_cliente().mostrar_saldo() # Se busca cliente por nombre y se muestra saldo con método de la clase

        elif opcion == '3':
            for cliente in lista_clientes: print(cliente) # Se imprime lo que retorna __str__ de la clase Cliente

        else:
            print(gen.warning('Ingresar una opción válida.'))