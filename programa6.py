#
def resultados():
    c2 = 0  # contador para elementos numéricos en el arreglo 
    #/ counter for numeric elements in the array
    print(f'la lista tiene {len(carc)}')  # mostrar la cantidad de elementos en la lista 
    #/ show the number of elements in the list
    for i in arr:  # recorrer el arreglo / loop through the array
        if i != -1:  # verificar si el valor es válido / check if the value is valid
            c2 += 1  # incrementar el contador / increment the counter
    print(f'el arreglo tiene {c2}')  # mostrar la cantidad de números en el arreglo 
    #/ show the number of numbers in the array
    print(carc)  # mostrar la lista de caracteres / show the character list
    print(arr)  # mostrar el arreglo de números / show the array of numbers


def hola():  # DEFINICIÓN DE MÉTODO O FUNCIÓN / FUNCTION DEFINITION
    c = 0  # contador para el arreglo / counter for the array
    while True:  # CICLO INFINITO / INFINITE LOOP
        a = input('Escribe un dato: ')  # solicitar dato al usuario / request input from the user
        if a.isdigit():  # VALIDAR DIGITOS / CHECK DIGITS
            arr[c] = int(a)  # guardar número en el arreglo / store number in the array
        elif a.isalpha():  # VALIDAR LETRAS / CHECK LETTERS
            carc.append(a)  # agrega elemento al final de la lista / add element to the end of the list
        c += 1  # incrementar contador / increment counter

        if c >= 10:  # verificar si se alcanzaron 10 elementos / check if 10 elements are reached
            break  # salir del bucle / exit the loop
        resultados()  # llamar a la función resultados / call the resultados function

carc = []  # lista para caracteres / list for characters
arr = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]  # arreglo inicializado con -1 / array initialized with -1

if __name__ == '__main__':  # MÉTODO PRINCIPAL / MAIN METHOD
    hola()  # llamar a la función hola / call the hola function
