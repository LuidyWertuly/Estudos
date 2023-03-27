contador = 0
contadorRP = 0
contadorAP = 0

total = int(input('digite o total de alunos: '))

while True:
    n1 = float(input('digite a nota 1: '))
    n2 = float(input('digite a nota 2: '))
    n3 = float(input('digite a nota 3: '))
    matri = int(input('digite a matricula: '))
    media = ((n1 * 4) + (n2 * 3) + (n3 * 3)) / 10
    if media >= 6:
        print("aprovado")
        contador = contador + 1
        contadorAP = contadorAP + 1
    else:
        print("reprovado")
        contador = contador + 1
        contadorRP = contadorRP + 1
    if contador == total:
        break
print("O Número De Aprovados: ", contadorAP)
print("O Número De Reprovados: ", contadorRP)
