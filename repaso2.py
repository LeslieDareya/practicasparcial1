
# Hacer un programa que tenga el funcionamiento de la fórmula general
# Create a program that implements the quadratic formula

a = 1  
# Coeficiente a de la ecuación cuadrática
# Coefficient a of the quadratic equation
b = 2  
# Coeficiente b de la ecuación cuadrática
# Coefficient b of the quadratic equation
c = -15  
# Coeficiente c de la ecuación cuadrática
# Coefficient c of the quadratic equation
p = 0  
# Variable para b al cuadrado (b^2)
# Variable for b squared (b^2)
m = 0  
# Variable para 4*a*c
# Variable for 4*a*c
r = 0  
# Variable para el discriminante
# Variable for the discriminant
ra = 0.0  
# Variable para la raíz cuadrada del discriminante
# Variable for the square root of the discriminant
d = 0.0  
# Variable para 2*a
# Variable for 2*a
x1 = 0.0  
# Variable para la primera solución
# Variable for the first solution
x2 = 0.0  
# Variable para la segunda solución
# Variable for the second solution

p = b**2  
# Calculamos b al cuadrado
# Calculate b squared
m = a*c*4  
# Calculamos 4*a*c
# Calculate 4*a*c
r = p - m  
# Calculamos el discriminante b^2 - 4ac
# Calculate the discriminant b^2 - 4ac

if r > 0:  
    # Si el discriminante es positivo, existen soluciones reales
    # If the discriminant is positive, real solutions exist
    print('Si se puede')  
    # Indicamos que es posible calcular las soluciones
    # Indicate that it is possible to calculate the solutions
    ra = r **(1/2)  
    # Calculamos la raíz cuadrada del discriminante
    # Calculate the square root of the discriminant
    d = 2*a  
    # Calculamos 2*a para la fórmula general
    # Calculate 2*a for the quadratic formula
    x1 = (-b + ra)/ d  
    # Calculamos la primera solución usando la fórmula general
    # Calculate the first solution using the quadratic formula
    x2 = (-b - ra)/ d  
    # Calculamos la segunda solución usando la fórmula general
    # Calculate the second solution using the quadratic formula
    print(f'El valor de x1 es {x1:.2f} y de x2 {x2:.2f}')  
    # Mostramos los valores de las soluciones con 2 decimales
    # Display the values of the solutions with 2 decimals
else:  
    # Si el discriminante no es positivo, no hay soluciones reales
    # If the discriminant is not positive, there are no real solutions
    print('No se puede')  
    # Indicamos que no es posible calcular soluciones reales
    # Indicate that it is not possible to calculate real solutions

