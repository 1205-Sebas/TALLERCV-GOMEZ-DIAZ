"""
EJERCICIO 7
"""
nombreMayor=" "
nombreMenor=" "
i=1
ns=int(input("¿Cuantos numeros ingresara?"))
while i<=ns:
    print("Ingrese el promedio: ",i)
    t=eval(input())
    print("Ingrese el nombre: ",i)
    nombre=input()
    if (i==1):
        may=t
        men=t
        nombreMenor=nombre
        nombreMayor=nombre
    elif (t>may):
        nombreMayor=nombre
        may=t
    elif (t<men):
        nombreMenor=nombre
        men=t
    i=i+1
print("---RESULTADO---")
print("El menor promedio de los ingresados es: ",men," y lo tiene el estudiante de nombre:",nombreMenor)
print("El mayor promedio de los ingresados es: ",may, " y lo tiene el estudiante de nombre:",nombreMayor)
