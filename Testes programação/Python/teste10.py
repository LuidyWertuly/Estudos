numero = int(input("Insira O Número: "))

if numero > 1:
    for x in range(2, numero):
        if (numero % x) == 0:
            print("Ele Não é Primo")
            break
    else:
        print("Ele é Primo")
else:
    print("Ele Não é Primo")
