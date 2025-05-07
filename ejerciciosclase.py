#pedir un numero mayor a 2, imprimir el numero primo con su gemelo
""" numero=int(input("Ingrese un número positivo mayor a 2: "))
if (numero > 2): 
    print("El número es positivo y mayor a 2")
else :
    print("número invalido") """
#while(True):
numero=int(input("Ingrese un número positivo mayor a 2: "))
numero_primo=[]
if(numero > 2): 
    for n in range(2,numero+1):
        es_primo=True
        for i in range(2,int(n**0.5)+1):
            if(n % i == 0):
                es_primo=False
                break 
        if(es_primo):
            numero_primo.append(n)
    numero_gemelo=[]
    for i in range(len(numero_primo)-1):
        if(numero_primo[i+1] - numero_primo[i] == 2):
            numero_gemelo.append((numero_primo[i],numero_primo[i+1]))
    if (numero_gemelo):
        print("pares de primos gemelos: ")
        for par in numero_gemelo:
            print(par)
    else:
            print("no existe pares de primos gemelos en este rango")
else:
    print("número invalido") 