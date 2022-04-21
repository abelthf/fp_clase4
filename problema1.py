# Escriba un algoritmo que lea 2 valores a, b, y los intercambie, por ejemplo si a=2 y b=5, el algoritmo debe hacer que a=5 y b=2


a: int
b: int
t: int
a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")

t = a
a = b
b = t

print("el valor de a: ", a)
print("el valor de b: ", b)
print("el valor de t: ", t)
