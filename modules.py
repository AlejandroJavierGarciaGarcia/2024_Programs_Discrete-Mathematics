

def mcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b 
    return b


a = int(input("Ingrese un número a: "))
b = int(input("Ingrese un número b: "))
print("El mdc de", a, "y", b, "es", mcd(a, b))


