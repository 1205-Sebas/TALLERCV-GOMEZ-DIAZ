"""
7. Elaborar un algoritmo que permita hallar el estudiante con mejor promedio de un curso de 30
estudiantes
"""
"""Definir i, t, ns, may, men Como Real
may<-0
men<-0
i<-1
nombreMayor<-" "
nombreMenor<-" "
nombre<- " "
Escribir "Cuantos numeros ingresara?"
leer ns
Mientras (i<=ns) Hacer
Escribir "Ingrese el promedio: ",i
leer t
Escribir "Ingrese el nombre: ",i
Leer nombre
Si(i==1) Entonces
may<-t
men<-t
Sino
Si(t>may)Entonces
may<-t
nombreMayor=nombre
FinSi
Si(t<men)Entonces
nombreMenor=nombre
men<-t
FinSi
FinSi
i<-i+1
FinMientras
Escribir "El menor promedio de los ingresados es: ",men," y lo tiene el estudiante de
nombre: ", nombreMenor
Escribir "El mayor promedio de los ingresados es: ",may, " y lo tiene el estudiante de
nombre: ",nombreMayor
FinAlgoritmo"""
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
print("El menor promedio de los ingresados es: ",men," y lo tiene el estudiante de nombre:",nombreMenor)
print("El mayor promedio de los ingresados es: ",may, " y lo tiene el estudiante de nombre:",nombreMayor)