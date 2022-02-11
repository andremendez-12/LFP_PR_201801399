import os
#uso de ASCII para el conteo de numeros, letras y simbolos
def leer(var):
    numero = 0
    letra = 0
    simbolo = 0
    for i in var:
        if ((ord(i)>=48) and (ord(i)<=57)):
            numero += 1
        elif ((ord(i)>=65) and (ord(i)<=90)):
            letra += 1
        elif ((ord(i)>=97) and (ord(i)<=122)):
            letra += 1
        elif ((ord(i)>=32) and (ord(i)<=47)):
            simbolo += 1
        totalcarac = numero + letra + simbolo
        var = "Total de Números: " + str(numero) + " Total de letras: " + str(letra) + " Total de símbolos: " + str(simbolo) + " Total de caracteres: " + str(totalcarac)
    print(var)

#archivo main para leer la entrada de la tarea 1

archivoenter = open('C:\\Users\\unicomer\\Desktop\\Tarea 1\\entrada.txt', "r")
archivoenter = archivoenter.read()
print(leer(archivoenter))
    
