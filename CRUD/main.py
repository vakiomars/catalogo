# La libreria os es para funciones del sistema
# La libreria time es para fechas
import os
import time
from classes.validacion import Validacion
validator = Validacion()

def print_options():
    print('Cátalogo Productos')
    print('*'* 50)
    print('Selecciona una opción:')
    print('[C]rear producto')
    print('[L]istado de productos')
    print('[M]odificar producto')
    print('[E]liminar producto')
    print('[B]uscar producto')
    print('[S]alir')

#Se llama la función print_options(). Con la función input() se recupera
#el texto escrito en la consola por el usuario, luego, se convierte en mayúsculas
#el texto intropducido para que el script acepte un comando tanto en mayúsculas como en minúsculas.
#Acto seguido, se comprueba que comando ha introducido el usuario y si no es un comando válido,
#se muestra un mensahe, se duerme el script durante un segundo con time.sleep(1)
#y se vuelve a llamar a la función run() para mostrar el menú de nuevo.

#Como se puede notar en la cadena de ifs la mayoria de funcionalidades
#tienen la palabra pass, esto significa una operación nula. Con el comando 'S' llama la función
#os._exit(1) que parará la ejecución del script y volvera a consola.

def run():
    print_options()

    command = input()
    command = command.upper()

    if command == 'C':
        crear_producto()
    elif command == 'L':
        pass
    elif command == 'M':
        pass
    elif command == 'E':
        pass
    elif command == 'B':
        pass
    elif command == 'S':
        os._exit(1)
    else:
        print('Comando inválido')
        time.sleep(1)
        run()

def crear_producto():
    print('Creación de producto')
    print('*' * 50)
    codigoProducto = check_codigoProducto()
    nombreProducto = check_nombreProducto()
    descripcionProducto = check_descripcionProducto()
    tipoProducto = check_tipoProducto()
    saborProducto = check_saborProducto()
    marca = check_marca()
    presentacion = check_presentacion()
    gramaje = check_gramaje()
    valor = check_valor()

def check_codigoProducto():
    print('Digitar el código del producto: ')
    codigoProducto = input()
    try:
        validator.validateCodigoProducto(codigoProducto)
        return codigoProducto
    except ValueError as err:
        print(err)
        check_codigoProducto()

def check_nombreProducto():
    print(f'Digitar el nombre del producto: ')
    nombreProducto = input()
    try:
        validator.validateNombreProducto(nombreProducto)
        return nombreProducto
    except ValueError as err:
        print (err)
        check_nombreProducto()

def check_descripcionProducto(descripcionProducto):
    print(f'Digitar la descripción del producto: ')
    descripcionProducto = input()
    try:
        validator.validateDescripcionProducto(descripcionProducto)
        return descripcionProducto
    except ValueError as err:
        print (err)
        check_descripcionProducto()

def check_tipoProducto(tipoProducto):
    print(f'Digitar el tipo del producto: ')
    tipoProducto = input()
    try:
        validator.ValidateTipoProducto(tipoProducto)
        return tipoProducto
    except ValueError as err:
        print (err)
        check_tipoProducto()

def check_saborProducto(saborProducto):
    print(f'Digitar el sabor del producto: ')
    saborProducto = input()
    try:
        validator.validateSaborProducto(saborProducto)
        return saborProducto
    except ValueError as err:
        print(err)
        check_saborProducto()

def check_marca(marca):
    print(f'Digitar la marca del producto: ')
    marca = input()
    try:
        validator.ValidateMarca(marca)
        return marca
    except ValueError as err:
        print(err)
        check_marca

def check_presentacion(presentacion):
    print(f'Digitar la presentación del producto: ')
    presentacion = input()
    try:
        validator.ValidatePresentacion(presentacion)
        return presentacion
    except ValueError as err:
        print(err)
        check_presentacion

def check_gramaje(gramaje):
    print(f'Digitar el peso en gramos del producto: ')
    gramaje = input()
    try:
        validator.validateGramaje(gramaje)
        return gramaje
    except ValueError as err:
        print(err)
        check_gramaje

def check_valor(valor):
    print(f'Digitar el valor en pesos del producto sin signos de puntación: ')
    valor = input()
    try:
        validator.ValidateValor(valor)
        return valor
    except ValueError as err:
        print(err)
        check_valor



# Lo que se hace a continuación es indicarle al intérprete de Python, que debe ejecutar python main.py
# al lanzarse por consola, es lo que hay dentro de ello, en este caso la función run() que es la función
# principal del programa.

if __name__ == "__main__":
    run()
