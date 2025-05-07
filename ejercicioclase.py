""" Descripción:
La suma persistente de los dígitos de un número consiste en sumar sus cifras 
repetidamente hasta obtener un solo dígito.
Requisitos:
Pedir al usuario un número entero positivo.
Sumar sus dígitos repetidamente hasta obtener un solo dígito.
Contar y mostrar cuántas sumas fueron necesarias para reducir el número a un solo dígito. """
contador= 0
suma = 0
resultado = []
numero=int(input("Ingresa un numero positivo: "))
resultado.append(numero)
while(True):
    suma= 0
    digitos= [int(d) for d in str(numero)]
    for a in digitos:
        suma = suma + a
    numero= suma 
    contador += 1
    resultado.append(suma) 
    if(len(str(numero)) == 1):
        break 
print(f"el proceso es: {resultado}")
print(f"la cantidad de sumas son: {contador}")