def par(n):
    if n == 0:
        return True
    else:
        return impar(n - 1)

def impar(n):
    if n == 0:
        return False
    else:
        return par(n - 1)

numero = 10

if par(numero):
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")
