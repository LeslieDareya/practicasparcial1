# Hacer un programa que lea 10 números y los almacene en un arreglo  

a = [0,0,0,0,0,0,0,0,0,0]  
# Crea una lista de 10 elementos inicializados en 0 / Creates a list of 10 elements initialized to 0

for i in range(0,10):  
    # Repite las instrucciones 10 veces, con 'i' desde 0 hasta 9 
    # / Repeats the instructions 10 times, with 'i' from 0 to 9
    a[i] = int(input('Escribe un numero \n'))  
    # Pide al usuario un número, lo convierte a entero y lo guarda en la posición i de la lista 
    # / Asks the user for a number, converts it to integer, and stores it at position i in the list

for i in a:  
    # Recorre cada elemento de la lista / Iterates through each element in the list
    print(i)  
    # Imprime el valor de cada elemento / Prints the value of each element



#float(input
