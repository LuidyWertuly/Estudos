# Limite 1558

numero = int(input("Insira Seu Número: "))

fatorial = 1

if numero == 0:

    print("O Fatorial De {numero} é 1 ")

elif numero < 0:

    print("Não Existe Fatorial De Números Negativos ")

else:

    for x in range(1, numero + 1):
        fatorial = fatorial * x
    print(f"O Fatorial De {numero} é {fatorial}")
