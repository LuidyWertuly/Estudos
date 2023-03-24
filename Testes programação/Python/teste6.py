lado = int(input('digite o lado: '))
areacirc = (3.4*((lado/2)*(lado/2)))/2
areadoquadrado = lado * lado
areadotriangulo = ((lado*lado) * 3**0.5)/4
areatotal = areadotriangulo + areacirc + areadoquadrado
pericirc = (((2*3.14)*lado)/2)/2
perimrestante = 4*lado
perimtotal = pericirc + perimrestante
print(f'perimetro total: {perimtotal: .2f}')
print(f'{areatotal: .2f}')
