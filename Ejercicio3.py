"""
Algoritmo Conversión_celsius_Fahr
celsius<-0
fahrenheit<-0
Escribir "Buen día, bienvenido a este conversor de grados Celsius a Fahrenheit"
Escribir "Por favor ingrese los grados celsius a transformar"
Leer celsius
fahrenheit<-(celsius*1.8)+32
Escribir celsius," grados Celsius equivalen a ", fahrenheit, " grados Fahrenheit."
FinAlgoritmo
"""
print("Buen día, bienvenido a este conversor de grados Celsius a Fahrenheit")
celsius=float(input("Ingrese los grados celsius a transformar: "))
fahr=(celsius*1.8)+32
print(str(celsius),"grados Celsius equivalen a: ",str(fahr),"grados fahrenheit.")
