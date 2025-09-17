a = []
# Crea una lista vacía llamada a donde se guardarán los números válidos que el usuario introduce.
# Creates an empty list called a where the valid numbers entered by the user will be stored.
s = 0
# Inicia la variable s en 0. Se usará como acumulador para sumar los números guardados.
# Initializes the variable s to 0. It will be used as an accumulator to sum the stored numbers.
n = 0
# Contador n en 0. Cuenta cuántos números válidos se han guardado en a
# Counter n set to 0. Counts how many valid numbers have been stored in a
numeros = "0123456789"
# Cadena con los caracteres permitidos para considerar una entrada como número.
# String with the allowed characters to consider an entry as a number.
while(n < 10):
    # Bucle while que se repite mientras n sea menor que 10
    # While loop that repeats while n is less than 10
    b = input('Escribe un numero: ')
    # Pide al usuario que escriba algo y lo guarda como cadena en b
    # Asks the user to enter something and stores it as a string in b
    x = 0
    # x servirá para contar cuántos caracteres de la cadena b son dígitos
    # x will be used to count how many characters of the string b are digits
    for i in b:
        # RECORRE LOS ELEMENTOS B
        # ITERATES THROUGH THE ELEMENTS OF b
        if i in numeros:
            x += 1
            # Si el carácter i está en la cadena numeros se incrementa x
            # If the character i is in the string numeros, x is incremented
    if len(b) == x:
        # Si son iguales, se considera la entrada válida como número entero.
        # If they are equal, the entry is considered valid as an integer number.
        a.append(int(b))
        # Convierte la cadena b a entero con int(b) y la añade a la lista a.
        # Converts the string b to an integer with int(b) and adds it to the list a.
        n += 1
        # Incrementa n porque se guardó un número válido.
        # Increments n because a valid number was stored.
    else:
        print('El valor no es numero ')
        # Si la entrada no está compuesta únicamente por dígitos, muestra el mensaje de error
        # If the entry is not composed only of digits, displays the error message