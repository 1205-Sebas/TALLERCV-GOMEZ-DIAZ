"""
Elaborar un algoritmo para calcular la nota final de un curso con la siguiente distribución de
evaluaciones: 2 parciales (25% cada uno), taller (20%) y proyecto (30%)
"""
def calcularNotaFinal(parcial1,parcial2,taller,proyecto):
    notaFinal=(parcial1*0.25)+(parcial2*0.25)+(taller*0.20)+(proyecto*0.30)
    return notaFinal

def leerDatos():
    parcial1=float(input("Ingrese la nota del parcial #1: "))
    parcial2=float(input("Ingrese la nota del parcial #2: "))
    taller=float(input("Ingrese la nota del taller: "))
    proyecto=float(input("Ingrese la nota del proyecto: "))
    d=calcularNotaFinal(parcial1,parcial2,taller,proyecto)
    print(d)
leerDatos()