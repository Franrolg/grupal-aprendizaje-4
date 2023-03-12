import random, colorama as colo

def generar_id(length):
    rango_inferior = 10**(length-1)
    rango_superior = (10**length)-1
    return random.randint(rango_inferior, rango_superior)


def generar_rut(inicio, fin):
    dv = [1,2,3,4,5,6,7,8,9,0,'K']
    rut = str(random.randint(inicio, fin)) + '.' + str(generar_id(3)) + '.' + str(generar_id(3))+'-'+ str(dv[random.randint(0,10)])
    return rut


def validar(seleccion, lista):
    return True if 0 < seleccion <= len(lista) else warning(f"Selección fuera de rango, presiona un número entre 1 y {len(lista)}")


# Inicializar colorama
colo.init()

def color(chars):
    return f"{colo.Fore.GREEN}{chars}{colo.Style.RESET_ALL}"

def warning(chars):
    return f"{colo.Fore.YELLOW}{chars}{colo.Style.RESET_ALL}"

def success(chars):
    return f"{colo.Fore.MAGENTA}{chars}{colo.Style.RESET_ALL}"


