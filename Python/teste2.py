c = input("insira o nome do cliente:")
v = input("insira qual foi o produto comprado:")
p = float(input("insira o preço do produto:"))
q = float(input("insira quantos produtos ele comprou:"))

p = p * q

print(c)
print(v)
print(p)
print(q)

ve = input("insira o nome do vendedor:")

CO = 40 * p / 100

print("você acaba de receber uma comissão de R$", CO)
