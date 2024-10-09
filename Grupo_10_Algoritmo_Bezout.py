"""
* Universidad del Valle de Guatemala
* Matemática Discreta
* Ingeniero Mario Castillo
* Programa: Algoritmo de la criba de Eratóstenes
* Integrantes: 
*  - Diego López
*  - Alejandro García
*  - Rocardo Godínez 
"""
import time

# Función que lee un entero positivo y valida que sea mayor que 0
def validacion(num):
    while True:
        if num.isdigit():  
            num = int(num)
            if num > 0:
                return num
            else:
                print(" * Ingrese un entero positivo.")
        else:
            print(" * Entrada inválida. Debe ingresar un número entero positivo.")
        
        num = input("\n - Ingrese nuevamente un número: ")


# Función que calcula los coeficientes de Bézout
def bezout(a,b):
    if(b>a):
        # Validación por si a es menor a b
        c = a
        a = b
        b = c

    # Operaciones matriciales


    return x,y

# Punto de inico del programa
print(" --------------------------------------------------------")
print(" |     ALGORITMO PARA HALLAR COEFICIENTES DE BEZOUT     |")
print(" --------------------------------------------------------")
num1 = validacion(input(" - Ingrese un entero positivo a: "))

num2 = validacion(input(" - Ingrese un entero positivo a: "))

x, y = bezout(num1, num2)
print(" - Los coeficientes de Bézout de ",num1, " y ", num2, " son: ",x, " y ", y, " respectivamente.")
