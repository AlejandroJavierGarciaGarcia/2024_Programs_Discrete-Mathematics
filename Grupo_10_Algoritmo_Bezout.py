"""
* Universidad del Valle de Guatemala
* Matemática Discreta
* Ingeniero Mario Castillo
* Programa: Algoritmo de la criba de Eratóstenes
* Integrantes: 
*  - Diego López
*  - Alejandro García
*  - Ricardo Godínez 
"""
import time
import numpy as np

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


# Función que calcula los coeficientes de Bézout y Operaciones matriciales
def bezout(a,b):

    M = np.array([[1,0], [0,1]])

    while b!= 0:
        c = a//b
        T = np.array([[0, 1],
              [1, -c]])

        M = np.dot(M,T)

        a0 = a
        b0 = b

        a = b0
        b = a0 % b0

    x = M[0,0]
    y = M[1,0]
    
    return x,y

# Punto de inico del programa
print(" --------------------------------------------------------")
print(" |     ALGORITMO PARA HALLAR COEFICIENTES DE BEZOUT     |")
print(" --------------------------------------------------------")
num1 = validacion(input(" - Ingrese un entero positivo a: "))

num2 = validacion(input(" - Ingrese un entero positivo b: "))

x, y = bezout(num1, num2)
print(" - Los coeficientes de Bézout de ",num1, " y ", num2, " son: ",x, " y ", y, " respectivamente.")
