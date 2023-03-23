n1 = float(input("Insira a Primeira Nota: "))
n2 = float(input("Insira a Segunda Nota: "))
n3 = float(input("Insira a Terceira Nota: "))
a = input("Insira sua Matricula: ")

if n1 > n2 > n3:

    m = ((n1 * 4) + (n2 * 3) + (n3 * 3)) / 10

elif n2 > n1 > n3:

    m = ((n2 * 4) + (n1 * 3) + (n3 * 3)) / 10

else:

    m = ((n3 * 4) + (n2 * 3) + (n1 * 3)) / 10

if m >= 5:
    print("Aprovado")
else:
    print("reprovado")

print(f"Você Foi Aprovado Com média: {m:.2f}")
