"""
6. Elaborar un algoritmo que permita realizar el inventario de una tienda, es decir cuántas unidades de
cada tipo de producto existen actualmente en la tienda. Se debe imprimir una lista ordenada de
productos de menor a mayor cantidad.
"""
import operator
a=int(input("Cantidad Aceite:"))
b=int(input("Cantidad Arroz:"))
c=int(input("Cantidad Cerveza:"))
d=int(input("Cantidad Gaseosa:"))
e=int(input("Cantidad Panela:"))
f=int(input("Cantidad Azucar:"))
g=int(input("Cantidad Cafe:"))
nombres={"Aceite:":a,"Arroz:":b,"Cerveza:":c,"Gaseosa:":d,"Panela:":e,"Azucar:":f,"Cafe:":g}
clients_sort = sorted(nombres)
clients_sort
clients_sort = sorted(nombres.items())
clients_sort
clients_sort = sorted(nombres.items(), key=operator.itemgetter(1), reverse=False)
print("INVENTARIO")
for name in enumerate(clients_sort):
    print(name[1][0],nombres[name[1][0]])

t=int(input("Ingrese el promedio: ",i))
