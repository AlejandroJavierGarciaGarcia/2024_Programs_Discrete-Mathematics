"""
* Universidad del Valle de Guatemala
* Matemática Discreta - 10 
* Ingeniero Mario Castillo
* Programa: Algoritmo de la criba de Eratóstenes
* Integrantes: 
*  - Diego López
*  - Alejandro García
*  - Ricardo Godínez 
"""

# Función que lee un entero positivo y valida que sea mayor que 0
def validacion(num):
    while True:
        if num.isdigit():  
            num = int(num)
            if num >=2:
                return num
            else:
                print(" * Ingrese un entero positivo.")
        else:
            print(" * Entrada inválida. Debe ingresar un número entero mayor o igual a 2.")
        
        num = input("\n - Ingrese nuevamente un número: ")


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

# Punto de inico del programa
print(" ------------------------------------------------")
print(" |            CRIBA DE ERATÓSTENES             |")
print(" ------------------------------------------------")
num = validacion(input(" - Introduzca un número: "))
print(" - Los primos menores o iguales a 28 son:", Criba(int(num)))
