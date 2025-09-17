# Instrucciones de entrada y salida
# print() o print(f)
#print('Hola mundo')
#print(f'Hola mundo numeros {10}')
#Entrada de datos
#input('Escribe un numero') #se introducen solo letras
#casting para convertir a valores especificos
#f = 0.0
#f = float(input('Escribe un numero con decimales'))
#a = 0
#a = int(input('Escribe un numero'))
#c = 120
#print(str(c))
#v = ""
#v = str(c)
# Nota: solo las variables que no se introducen por teclado se obliga a inicializarlas.

# Hacer un programa que lea nombre y precio de un producto, el programa calculará el costo y el precio de venta
# Create a program that reads the name and price of a product, the program will calculate the cost and selling price
# Costo involucra el 12% y el IVA 16%
# Cost involves 12% and VAT 16%

for i in range(1,5):  # Repite 4 veces: desde 1 hasta 4 (el 5 no se incluye)
                       # Repeat 4 times: from 1 to 4 (5 is not included)
    # precio = 12.55  # Inicialización de ejemplo, se sobreescribe después
                       # Example initialization, overwritten later
    nombre = input('Escribe el nombre del producto\n')  
    # Pide al usuario el nombre del producto
    # Ask the user for the product name
    precio = float(input("Escribe el precio del producto\n"))  
    # Pide al usuario el precio del producto y lo convierte a flotante
    # Ask the user for the product price and convert it to float
    costo = precio * 1.12  
    # Calcula el costo agregando 12% (sobreprecio o gastos)
    # Calculate the cost adding 12% (overhead or expenses)
    precioventa = costo * 1.16  
    # Calcula el precio de venta agregando IVA del 16%
    # Calculate the selling price adding 16% VAT
    print(f'el costo es {costo:.2f} y el precio de venta {precioventa:.2f}\n')  
    # Imprime el costo y precio de venta con 2 decimales
    # Print the cost and selling price with 2 decimals
    print(f'el costo es {costo} y el precio de venta {precioventa}\n')  
    # Imprime el costo y precio de venta sin limitar decimales
    # Print the cost and selling price without limiting decimals

    # Código comentado para permitir al usuario continuar o terminar
    # Commented code to allow the user to continue or stop
    # res = input('Deseas otro numero (s/n) \n')
    # if res == 'n' or res == 'N':
    #     break






