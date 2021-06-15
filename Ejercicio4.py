"""
Elaborar un algoritmo que permita calcular cuál es el precio final a pagar por una factura de
productos, tenga en cuenta que la factura se imprime con al menos un producto, pero no se sabe al
inicio cuantos productos va a llevar el cliente (el cliente los va pasando uno a uno hasta terminar). La
factura debe imprimir la descripción del artículo, su precio y el iva que corresponde al 8% sobre el
producto, al final se debe indicar el precio total a pagar.
"""
productos={"Azucar":1000,"Panela":850,"Cerveza":1890,"Gaseosa":4200,"Cafe":5000,"Arroz":2500,"Aceite":3890}
iva=0.08
azucar=int(input("Ingrese cuantas bolsas de azucar:"))
panela=int(input("Ingrese cuantas panelas:"))
cerveza=int(input("Ingrese cuantas cervezas:"))
gaseosa=int(input("Ingrese cuantas gaseosas:"))
cafe=int(input("Ingrese cuantas bolsas de cafe:"))
arroz=int(input("Ingrese cuantas bolsas de arroz:"))
aceite=int(input("Ingrese cuantas botellas de aceite:"))
cantidadProductos=azucar+panela+cerveza+gaseosa+cafe+arroz+aceite
pivaA=(azucar*productos["Azucar"])*0.08
totalA=(azucar*productos["Azucar"])+pivaA
pivaB=(panela*productos["Panela"])*0.08
totalB=(panela*productos["Panela"])+pivaB
pivaC=(cerveza*productos["Cerveza"])*0.08
totalC=(cerveza*productos["Cerveza"])+pivaC
pivaD=(gaseosa*productos["Gaseosa"])*0.08
totalD=(gaseosa*productos["Gaseosa"])+pivaD
pivaE=(cafe*productos["Cafe"])*0.08
totalE=(cafe*productos["Cafe"])+pivaE
pivaF=(arroz*productos["Arroz"])*0.08
totalF=(arroz*productos["Arroz"])+pivaF
pivaG=(aceite*productos["Azucar"])*0.08
totalG=(aceite*productos["Aceite"])+pivaG
totalFinal=totalA+totalB+totalC+totalD+totalE+totalF+totalG
if cantidadProductos>=1:
    print("Usted compro:",azucar," bolsas de azucar a ",productos["Azucar"]," c/u el iva es de",pivaA, " y el costo total del productos es:",totalA)
    print("Usted compro:",panela," bolsas de panela a ",productos["Panela"]," c/u el iva es de",pivaB, " y el costo total del productos es:",totalB)
    print("Usted compro:",cerveza," cervezas a ",productos["Cerveza"]," c/u el iva es de",pivaC, " y el costo total del productos es:",totalC)
    print("Usted compro:",gaseosa," botellas de gaseosa a ",productos["Gaseosa"]," c/u el iva es de",pivaD, " y el costo total del productos es:",totalD)
    print("Usted compro:",cafe," bolsas de cafe a ",productos["Cafe"]," c/u el iva es de",pivaE, " y el costo total del productos es:",totalE)
    print("Usted compro:",arroz," bolsas de arroz a ",productos["Arroz"]," c/u el iva es de",pivaF, " y el costo total del productos es:",totalF)
    print("Usted compro:",aceite," botellas de aceite a ",productos["Aceite"]," c/u el iva es de",pivaG, " y el costo total del productos es:",totalG)
    print("Usted compro un total de:",cantidadProductos,"productos")
    print("El total de la compra es de:$",totalFinal)
    print("Gracias por su compra")
else:
    print("NO IMPRIME RECIBO")
  

