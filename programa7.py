# hacer un programa que lea nombre, edad y sexo de 5 personas, estos elementos tienen que estar dentro de una lista
# create a program that reads name, age, and gender of 5 people; these elements must be stored in a list

def inicio():  # DEFINICIÓN DE LA FUNCIÓN / FUNCTION DEFINITION
    c = 0  # contador de personas / counter for people
    while True:  # CICLO INFINITO / INFINITE LOOP
        n = input('Escribe el nombre')  # solicitar nombre al usuario / ask the user for the name
        e = input('Escribe la edad')  # solicitar edad al usuario / ask the user for the age
        s = input('Escribe el sexo')  # solicitar sexo al usuario / ask the user for the gender
        lis.append([n, e, s])  # agregar los datos como lista dentro de la lista principal 
        #/ add the data as a list inside the main list
        c += 1  # incrementar el contador / increment the counter
        if c >= 5:  # verificar si ya se ingresaron 5 personas / check if 5 people have been entered
            break  # salir del bucle / exit the loop
    print(lis)  # mostrar la lista completa / print the full list

lis = []  # lista principal para almacenar los datos de las personas / main list to store people's data

if __name__ == "__main__":  # MÉTODO PRINCIPAL / MAIN METHOD
    inicio()  # llamar a la función inicio / call the inicio function

