# maiúsculas e minúsculas
# símbolos e espaços

"""
security = Base
5ec&rit1 = senha

"""

chave = input("Digite a Palavra Base Da Sua Senha:")

senha = ""

for letra in chave:
    if letra in "Aa":
        senha = senha + "1"
    elif letra in "Bb":
        senha = senha + "@"
    elif letra in "Cc":
        senha = senha + "Z"
    elif letra in "Dd":
        senha = senha + "%"
    elif letra in "Ee":
        senha = senha + "$"
    elif letra in "Ff":
        senha = senha + "11"
    elif letra in "Gg":
        senha = senha + "9"
    elif letra in "Hh":
        senha = senha + "13"
    elif letra in "Ii":
        senha = senha + "*"
    elif letra in "Jj":
        senha = senha + "15"
    elif letra in "Kk":
        senha = senha + "6"
    elif letra in "Ll":
        senha = senha + "&"
    elif letra in "Mm":
        senha = senha + "18"
    elif letra in "Nn":
        senha = senha + "~"
    elif letra in "Oo":
        senha = senha + "#"
    elif letra in "Pp":
        senha = senha + "21"
    elif letra in "Qq":
        senha = senha + "2"
    elif letra in "Rr":
        senha = senha + "23"
    elif letra in "Ss":
        senha = senha + "B"
    elif letra in "Tt":
        senha = senha + "25"
    elif letra in "Uu":
        senha = senha + "26"
    elif letra in "Vv":
        senha = senha + "27"
    elif letra in "Ww":
        senha = senha + "8"
    elif letra in "Xx":
        senha = senha + "t"
    elif letra in "Yy":
        senha = senha + "3"
    elif letra in "Zz":
        senha = senha + "X"

print(senha)
