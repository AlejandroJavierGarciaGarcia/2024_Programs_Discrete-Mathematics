"""
* Universidad del Valle de Guatemala
* Matemática Discreta
* Ingeniero Mario Castillo
* Programa: MCD
* Integrantes: 
*  - Diego López
*  - Alejandro García
*  - Rocardo Godínez 
"""

def mcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b 
    return b


a = int(input("Ingrese un entero positivo a: "))
b = int(input("Ingrese un entero positivo b: "))
print("El mdc de", a, "y", b, "es", mcd(a, b))


