#Hacer un programa que lea 10 datos, si el dato es un numero se almacenara en un arreglo, si es un caracter o
#caracteres
#se metera a una lista, cuando finalice el programa nos mostrara cuantos elementos numericos y cuantos
#caracteres hay en cada estructura.

arr = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]  # arreglo para almacenar números / array to store numbers
car = []  # lista para almacenar caracteres / list to store characters
c = 0  # contador para el arreglo / counter for the array
c2 = 0  # contador para números en el arreglo / counter for numbers in the array

while(True):
    a = input('Escribe un dato o valor\n')  # pedir al usuario que ingrese un valor / ask the user to enter a value
    if a.isdigit():  # verificar si la entrada es un número / check if the input is a digit
        arr[c] = int(a)  # almacenar el número en el arreglo / store the number in the array
    elif a.isalpha():  # verificar si la entrada es una letra o palabra / check if the input is alphabetic
        car.append(a)  # agregar la entrada a la lista de caracteres / add the input to the character list
    c += 1  # incrementar el contador / increment the counter
    if c >= 10:  # verificar si el arreglo está lleno / check if the array is full
        break  # salir del bucle / exit the loop

print(f'la lista tiene {len(car)}')  # imprimir cuántos caracteres hay en la lista
# / print how many characters are in the list

for i in arr:  # recorrer el arreglo / loop through the array
    if i != -1:  # verificar si el valor es un número válido / check if the value is a valid number
        c2 += 1  # incrementar el contador de números / increment the number counter

print(f'el arreglo tiene {c2}')  # imprimir cuántos números hay en el arreglo / print how many numbers are in the array
print(car)  # imprimir la lista de caracteres / print the list of characters
print(arr)  # imprimir el arreglo de números / print the array of numbers


