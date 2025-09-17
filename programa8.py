
# Hacer un programa que lea una cadena y que muestre en pantalla cuantos números tiene, cuantas letras mayúsculas, minúsculas y espacios
# Create a program that reads a string and displays how many numbers, uppercase letters, lowercase letters, and spaces it contains

def inicio():  # DEFINICIÓN DE LA FUNCIÓN / FUNCTION DEFINITION
    mi = 0  # contador de letras minúsculas / counter for lowercase letters
    may = 0  # contador de letras mayúsculas / counter for uppercase letters
    c = 0  # contador de números / counter for numbers
    e = 0  # contador de espacios / counter for spaces
    numeros = "0123456789"  # cadena que contiene los dígitos / string containing digits
    cadena = input('Escribe una cadena')  # solicitar al usuario que ingrese una cadena / ask the user to enter a string
    for i in cadena:  # recorrer cada carácter de la cadena / loop through each character in the string
        if i in numeros:  # verificar si el carácter es un número / check if the character is a number
            print('es numero')  # mostrar mensaje si es número / display message if it is a number
            c += 1  # incrementar contador de números / increment number counter
        if i == ' ':  # verificar si el carácter es un espacio / check if the character is a space
            e += 1  # incrementar contador de espacios / increment space counter
        if ord(i) >= 97 and ord(i) <= 122:  # verificar si es minúscula / check if it is lowercase
            mi += 1  # incrementar contador de minúsculas / increment lowercase counter
        if ord(i) >= 65 and ord(i) <= 90:  # verificar si es mayúscula / check if it is uppercase
            may += 1  # incrementar contador de mayúsculas / increment uppercase counter
    print(f'Los numeros son: {c}\n y los espacios: {e}\n y las minusculas: {mi}\n y las mayusculas: {may}\n')  
    # mostrar resultados / display results
        
if __name__ == "__main__":  # MÉTODO PRINCIPAL / MAIN METHOD
    inicio()  # llamar a la función inicio / call the inicio function



 


    






