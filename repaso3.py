# Hacer un programa que lea números y defina si es un número decimal o un número entero
# Make a program that reads numbers and defines if it is a decimal or an integer

def validar(a):  # Definición de la función validar que recibe un parámetro 'a'
    # Definition of the function validar that takes one parameter 'a'
    c = 0  # Variable entera inicializada en 0
    # Integer variable initialized to 0
    d = 0.0  # Variable decimal inicializada en 0.0
    # Float variable initialized to 0.0
    try:  # Intentar convertir 'a' en un número entero
        # Try to convert 'a' into an integer
        c = int(a)  
        print('Es un número entero sin decimales')  
        # It is an integer without decimals
        print('Es un número entero')  
        # It is an integer
    except ValueError:  # Si ocurre un error, significa que no es entero
        # If an error occurs, it means it's not an integer
        try:  # Intentar convertir 'a' en un número decimal (float)
            # Try to convert 'a' into a decimal (float)
            d = float(a)  
            print('Es un número entero con decimales')  
            # It is a number with decimals
            print('Es un número decimal\n')  
            # It is a decimal number
        except ValueError:  # Si tampoco se puede, no es un número válido
            # If it also fails, then it is not a valid number
            print('No es un número válido')  
            # It is not a valid number

def leer():  # Función que pide al usuario un dato
    # Function that asks the user for a value
    a = input('Escribe un dato o valor\n')  
    # Read input from the user
    validar(a)  
    # Call the function validar with the input

if __name__ == '__main__':  # Punto de entrada principal del programa
    # Main entry point of the program
    leer()  
    # Call the function leer

# ord obtiene el ASCII del carácter
# ord gets the ASCII value of a character

# isalpha verifica si es un carácter alfabético
# isalpha checks if it is an alphabetic character

# isdigit verifica si es un número
# isdigit checks if it is a digit

# try-except ValueError se usa para manejar errores en conversiones
# try-except ValueError is used to handle errors in conversions
