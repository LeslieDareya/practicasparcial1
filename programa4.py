
# hacer un programa que lea 10 numeros y los almacene en una lista 
# / Create a program that reads 10 numbers and stores them in a list

a = []  
# Crea una lista vacía para guardar los números / Creates an empty list to store the numbers

s = 0  
# Inicializa la variable 's' para almacenar la suma / Initializes the variable 's' to store the sum

n = 0  
# Inicializa la variable 'n' para contar cuántos números válidos se han ingresado 
# / Initializes 'n' to count how many valid numbers have been entered

numeros = "0,1,2,3,4,5,6,7,8,9";  
# Define una cadena con los caracteres numéricos válidos 
# / Defines a string with the valid numeric characters

while(n < 10):  
    # Bucle que se repite hasta que se hayan ingresado 10 números válidos 
    # / Loop that repeats until 10 valid numbers have been entered

    b = input('Ecribe un numero')  
    # Pide al usuario que ingrese un número y lo guarda en 'b' 
    # / Asks the user to enter a number and stores it in 'b'

    x = 0  
    # Inicializa un contador 'x' para verificar si todos los caracteres son dígitos 
    # / Initializes a counter 'x' to check if all characters are digits

    for i in b:  
        # Recorre cada carácter en la entrada 'b' 
        # / Iterates over each character in the input 'b'
       
        # if (ord(i) >= 48 and ord(i) <=57):  
        if i in numeros:  
            # Verifica si el carácter está en la lista de números válidos 
            # / Checks if the character is in the list of valid numbers
            x += 1  
            # Si es válido, aumenta el contador 'x' 
            # / If valid, increments the counter 'x'

    if len(b) == x:  
        # Si todos los caracteres son dígitos, se considera un número válido 
        # / If all characters are digits, it is considered a valid number
        a.append(int(b))  
        # Convierte la entrada a entero y la agrega a la lista 'a' 
        # / Converts the input to an integer and appends it to the list 'a'
        n += 1  
        # Aumenta el contador de números válidos ingresados 
        # / Increments the count of valid numbers entered
    else:  
        print('el valor no es un numero')  
        # Si algún carácter no es dígito, muestra un mensaje de error 
        # / If any character is not a digit, shows an error message

for i in a:  
    # Recorre cada número de la lista 'a' / Iterates over each number in the list 'a'
    print(i)  
    # Imprime el número actual / Prints the current number
    s += i  
    # Suma el número actual a la variable 's' / Adds the current number to the variable 's'

print(f'La suma es {s}')  
# Imprime la suma total de los números ingresados / Prints the total sum of the entered numbers

