#Crear un programa que en una lista se introduzca cadenas de caracteres con las siguientes restricciones:
# 1. las cadenas NO deben tener espacios, 2. la cadena solo puede tener mayuscula la primer letra, 
#3. obligatoriamente debe tener todas las vocales. El programa no termina hasta que la lista tenga 5 elementos.
#Crear un programa que en una lista se introduzca cadenas de caracteres con las siguientes restricciones:
# 1. las cadenas NO deben tener espacios, 2. la cadena solo puede tener mayuscula la primer letra, 
#3. obligatoriamente debe tener todas las vocales. El programa no termina hasta que la lista tenga 5 elementos.
#Perfecto, Leslie, aquí tienes todo junto en una sola frase tipo descripción de tarea:



#Create a program that stores strings in a list, where the strings do not contain spaces, only the first letter is uppercase, must contain all the vowels, and the program does not end until the list has five elements that meet these conditions.



def vocales(cad):
    # Variables booleanas para cada vocal / Boolean variables for each vowel
    ba = False
    be = False
    bi = False
    bo = False
    bu = False
    # Verifica si la cadena contiene cada vocal (mayúscula o minúscula)
    # Checks if the string contains each vowel (uppercase or lowercase)
    if 'a' in cad or 'A' in cad:
            ba = True 
    if 'e' in cad or 'E' in cad:
            be = True 
    if 'i' in cad or 'I' in cad:
            bi = True 
    if 'o' in cad or 'O' in cad:
            bo = True 
    if 'u' in cad or 'U' in cad:
            bu = True 
    # Si todas las vocales están presentes, se agrega la cadena a la lista
    # If all vowels are present, add the string to the list
    if ba == True and be == True and bi == True and bo == True and bu == True:
         lista.append(cad)
    # Imprime la lista acumulada de cadenas válidas
    # Prints the accumulated list of valid strings
    print(lista)



def minusculas(c1):
    # Contador de caracteres en minúscula / Counter for lowercase characters
    cm = 0
    print(c1)  # Imprime la cadena recibida / Prints the received string
    # Recorre la cadena desde el segundo carácter (exceptuando el primero)
    # Loops through the string starting from the second character
    for i in c1[1:]:
        # Verifica si el carácter está en minúscula usando su valor ASCII
        # Checks if the character is lowercase using its ASCII value
        if ord(i) >=97 and ord(i)<=122:
            cm += 1
    # Si todos menos el primero son minúsculas
    # If all except the first are lowercase
    if cm == len(c1)-1:
        print(f'la cadena son minusculas excepto la primera{cm}')
        # Llama a la función vocales (aunque aquí pasa un número, debería ser la cadena)
        # Calls the vowels function (though here it passes a number, should be the string)
        vocales(cm)
    else:
        # Si no se cumple la condición
        # If the condition is not met
        print('Error la cadena no cumple') 
    

def inicio():
    # Contador de caracteres distintos de espacio
    # Counter for characters different from space
    ce = 0
    nc = ""  # Nueva cadena para depuración / New string for debugging
    c = input("Escribe la cadena: \n")  # Pide al usuario una cadena / Asks user for a string
    # Recorre cada carácter de la cadena
    # Loops through each character of the string
    for i in c:
        if ord(i) != 32:  # Si no es espacio / If it's not a space
            ce += 1

    # Si no había espacios en la cadena
    # If there were no spaces in the string
    if ce == len(c):
        if c.isalpha():  # Si la cadena solo tiene letras / If string contains only letters
            # Revisa si son minúsculas con excepción de la primera
            # Checks if they are lowercase except the first one
            minusculas(c)
        else:
            # Si no son todas letras, revisa carácter por carácter
            # If not all are letters, check character by character
            for i in c:
                # Si es un número, lo omite / If it's a number, skip it
                if ord(i) >= 48 and ord(i) <= 57:
                    pass
                else:
                    # Si no es número, lo agrega a la nueva cadena
                    # If not a number, add it to the new string
                    nc += i
                print(nc)  # Imprime la nueva cadena parcial / Prints the new partial string
                minusculas(nc)  # Verifica minúsculas en la nueva cadena / Checks lowercase in new string
    else:
        # Si contiene espacios
        # If contains spaces
        print('Error en la cadena')

# Lista global para almacenar las cadenas válidas
# Global list to store valid strings
lista = []

if __name__ == "__main__":
    # Ciclo infinito hasta que haya al menos 5 cadenas válidas
    # Infinite loop until there are at least 5 valid strings
    while(True):
         inicio()  # Llama al inicio / Calls the main function
         if len(lista) >=5:  # Si ya hay 5 cadenas en la lista / If there are 5 strings in the list
              break  # Rompe el ciclo / Breaks the loop
