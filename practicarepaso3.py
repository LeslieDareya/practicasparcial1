#Hacer un programa que lea numeros enteros y que los almacene en una lista. Si el numero no es decimal volvera a pedirlo hasta 
#que sea un entero. Los numeros se seguiran almacenando hasta que el usuario decida que no quiere agregar mas datos.

def validar(a):
    ne = 0
    try:
        ne = int(a)
        
        return ne
    except ValueError:
        print('No es un entero')
    try:
        nf = float(a)
        return nf
    except ValueError:
        print('No es un numero con decimales')
    return a
def leer():
    a = input('Escribe un dato \n')
    dato = validar(a)
    lista.append(dato)

lista = []
if __name__ == '__main__':
    while(True):
      leer()
      res = input('Deseas otro s/n')
      if res == 'n' or res == 'N':
        print(lista)
        break
