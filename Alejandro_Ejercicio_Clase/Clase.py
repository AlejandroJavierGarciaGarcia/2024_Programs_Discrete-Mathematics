import time

def prime_test1(n):
    # Recorre desde dos hasta el número aumentado en 1
    for i in range(2,n):
        # Si el número es divisible dentro de i, entonces, es primo
        if n % i ==0:
            return False
        # Si no es divisible dentro de nigún i, entonces, es compuesto
    return True

def Criba(n):
    # Lista de primos
    primes = []
    # LIstas de no primos
    not_primes = set()
    # Recorre desde dos hasta el número aumentado en uno
    for i in range(2,n):
        # Verifica si i está en no primos, si ya está salta el índice
        if i in not_primes:
            continue
        # Verifica los múltiplos de i y los agrega en j hasta n
        for j in range(i*2,n,i):
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
            return False
    return True
    
print(" ------------------------------------------------")
print(" |            DIVISIBILIDAD - 231136            |")
print(" ------------------------------------------------")
print(" * Alejandro García")

a = int(input("\n - Introduce un número: "))
start_time = time.time()

print(prime_test2(a))

end_time = time.time()

print("Execution time: ", end_time-start_time)