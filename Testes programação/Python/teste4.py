n1 = float(input("Insira o Primeiro Numero: "))
n2 = float(input("Insira o Segundo Numero: "))
n3 = float(input("Insira o Terceiro Numero: "))

if n1 > n2 > n3:
    print(n1)
elif n2 > n1 > n3:
    print(n2)
else:
    print(n3)
