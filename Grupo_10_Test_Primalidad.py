"""
* Universidad del Valle de Guatemala
* Matemática Discreta - 10 
* Ingeniero Mario Castillo
* Programa: Test de primalidad
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
            if num >0:
                return num
            else:
                print(" * Ingrese un entero positivo.")
        else:
            print(" * Entrada inválida. Debe ingresar un número entero mayor a 0.")
        
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

def prime_test(n):
    # Llama a funcion Criba y guarda los número primos en otro arreglo
    prime_list = Criba(int(n**0.5))
    # Verifica divisibilidad del n según la lista de primos
    for i in prime_list:
        # Si el número es divisible dentro de algún primo, entonces, es compuesto
        if n % i==0:
            print("El número ", n, " no es primo, pues lo divide ", i)
            return False
    print("El número ", n, " es primo")
    return True

def dividers(n):
    dividers = []
    prime_list = Criba(int(n))
    # Verifica divisibilidad del n según la lista de primos4
    for i in prime_list:
        # Si el número es divisible dentro de algún primo, entonces, es compuesto
        if n % i==0:
            dividers.append(i)
    print("  - Factorización prima:", ' x '.join(map(str, dividers)))


print(" ------------------------------------------------")
print(" |              TEST DE PRIMALIDAD              |")
print(" ------------------------------------------------")
num = validacion(input(" - Introduce un número: "))
prime_test(num)
dividers(num)



