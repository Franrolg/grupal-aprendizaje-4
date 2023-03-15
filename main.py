from cliente import menu_clientes
from producto import menu_productos
from proveedor import menu_proveedores
from vendedor import menu_vendedores
from generador import color, warning
from bodega import menu_sucursal

while True:
    opcion = input(f'{color("1)")} Clientes\n{color("2)")} Productos\n{color("3)")} Proveedores\n{color("4)")} Ventas\n{color("5)")} Bodega\n{warning("0)")} Salir\n>> ')
    if opcion == '1':
        menu_clientes()
    
    elif opcion == '2':
        menu_productos()

    elif opcion == '3':
        menu_proveedores()

    elif opcion == '4':
        menu_vendedores()
    
    elif opcion == '5':
        menu_sucursal()
        
    elif opcion == '0':
        break
    else:
        print('Ingresar una opción válida')