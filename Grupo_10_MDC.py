"""
* Universidad del Valle de Guatemala
* Matemática Discreta - 10 
* Ingeniero Mario Castillo
* Programa: MCD
* Integrantes: 
*  - Diego López
*  - Alejandro García
*  - Ricardo Godínez 
"""

def mcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b 
    return b
print(" ------------------------------------------------")
print(" |                    MCD                       |")
print(" ------------------------------------------------")
a = int(input("Ingrese un entero positivo a: "))
b = int(input("Ingrese un entero positivo b: "))
print("El mdc de", a, "y", b, "es", mcd(a, b))


