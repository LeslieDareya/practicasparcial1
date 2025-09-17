# Hacer un programa que lea numeros enteros y que los almacene en una lista. 
# Si el numero no es decimal volvera a pedirlo hasta que sea un entero. 
# Los numeros se seguiran almacenando hasta que el usuario decida que no quiere agregar mas datos.
# Make a program that reads integers and stores them in a list. 
# If the number is not an integer, it will ask again until it is. 
# The numbers will keep being stored until the user decides not to add more data.

def validar(a):
    ne = 0
    try:
        ne = int(a)  # Intenta convertir el dato a entero / Try to convert the input into an integer
        return ne
    except ValueError:
        print('No es un entero')  # Muestra mensaje si no es un número entero / Shows a message if it's not an integer
    try:
        nf = float(a)  # Intenta convertir el dato a decimal / Try to convert the input into a float
        return nf
    except ValueError:
        print('No es un numero con decimales')  # Muestra mensaje si no es decimal / Shows a message if it's not a decimal
    return a  # Devuelve el dato original si no es número / Returns the original input if it's not a number

def leer():
    a = input('Escribe un dato \n')  # Pide al usuario un dato / Asks the user for an input
    dato = validar(a)  # Valida el dato ingresado / Validates the entered input
    lista.append(dato)  # Agrega el dato a la lista / Appends the data to the list

lista = []  # Lista vacía para guardar los datos / Empty list to store the data
if __name__ == '__main__':
    while(True):  # Ciclo infinito hasta que el usuario decida salir / Infinite loop until the user decides to exit
      leer()  # Llama a la función para leer y validar datos / Calls the function to read and validate data
      res = input('Deseas otro s/n')  # Pregunta si quiere continuar / Asks if the user wants to continue
      if res == 'n' or res == 'N':  # Si la respuesta es 'n' o 'N' termina / If response is 'n' or 'N', it ends
        print(lista)  # Muestra la lista de datos capturados / Prints the list of captured data
        break  # Rompe el ciclo y finaliza el programa / Breaks the loop and ends the program
