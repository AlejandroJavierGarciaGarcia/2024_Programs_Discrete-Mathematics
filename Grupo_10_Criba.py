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

def Criba(n):
    # Lista de primos
    primes = []
    # LIstas de no primos
    not_primes = set()
    # Recorre desde dos hasta el número aumentado en uno
    for i in range(2,n+1):

        # Verifica si i está en no primos, si ya está salta el índice
        if i in not_primes:
            continue
        # Verifica los múltiplos de i y los agrega en la lista de no primos de j hasta n
        for j in range(i*2,n+1,i):
            not_primes.add(j)
        # Después de las validaciones añade a i al array de primos
        primes.append(i)
    return primes

def prime_test2(n):
    # Llama a funcion Criba y guarda los número primos en otro arreglo
    prime_list = Criba(int(n**0.5))
    # Verifica divisibilidad del n según la lista de primos
    for i in prime_list:
        # Si el número es divisible dentro de algún primo, entonces, es compuesto
        if n % i==0:
            return prime_list
    return prime_list

# Punto de inico del programa
print(" ------------------------------------------------")
print(" |            CRIBA DE ERATÓSTENES             |")
print(" ------------------------------------------------")

num = int(input(" - Introduce un número: "))
start_time = time.time()
print(" - Los primos menores o iguales a 28 son:", Criba(int(num)))
end_time = time.time()
print("\n  - Execution time: ", end_time-start_time)