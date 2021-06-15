"""
5. Elaborar un algoritmo casa de cambio, que reciba una cantidad de dinero en pesos colombianos y
realice su equivalente en dolares, yenes y euros, tenga en cuenta que el cambio deberá realizarse a la
tasa representativa de cada moneda (actual) y que la casa de cambio, incluye un 2% de ganancia a ese
valor.
"""
cop=int(input("Ingrese el valor a cambiar: "))
dolares=3623
yenes=33.67
euros=4341
ganancia=0.02
valorDolG=(cop//dolares)*ganancia
valorDol=(cop//dolares)+valorDolG
valorYenG=(cop*yenes)*ganancia
valorYen=(cop*yenes)+valorDolG
valorEurG=(cop//euros)*ganancia
valorEur=(cop//euros)+valorEurG
print("Serian: "+str(valorDol)+" dolares.")
print("Serian: "+str(valorYen)+" yenes.")
print("Serian: "+str(valorEur)+" euros.")
