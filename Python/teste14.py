while True:
    n1 = float(input("Insira n1: "))

    n2 = float(input("Insira n2: "))

    if n1 % n2 == 0:

        m = (n1 + n2) / 2

    if n1 or n2 == 0:
        break
    print(m)
