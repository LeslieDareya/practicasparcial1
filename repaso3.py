#Hacer un programa que lea numeros y defina si es un numero decimal o un numero entero
def validar(a):
    c = 0
    d = 0.0
    try:
        c = int(a)
        print('Es un número entero sin decimales')
        print('Es un número entero')
    except ValueError:
        try:
            d = float(a)
            print('Es un número entero con decimales')
            print('Es un número decimal\n')
        except ValueError:
            print('No es un número válido')

def leer():
    a = input('Escribe un dato o valor\n')
    validar(a)

if __name__ == '__main__':
    leer()
# ord que obtiene el ascii del caracter
# isalpha para caracteres
# isdigit para numeros
# try except ValueError: