R = float(input("Insira o Valor EM Reais:"))
D = float(input("Insira a Cotação Do Dolar Hoje:"))
E = float(input("Insira a Cotação Do Euro Hoje:"))

D = R / D
E = R / E

U = "Ola"

print("Seu Valor EM Dolar é:", D)
print("Seu Valor Em Euro é:", E)

print(type(U))

U = "Mundo"

print(U)
