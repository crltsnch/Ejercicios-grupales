# Ejercicios-grupales
Código del ejercicio 1:

```
import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    # Write your code here
    suma=0
    for i in ar:
        suma= suma+i
    return suma

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'] + 'solucion1.txt', 'w')
    print("Escribe el tamaño")
    ar_count = int(input().strip())
    print("Escribe los números separados por espacio")
    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    ```
    
    
 Código del ejercicio 2:
    ```
    def compareTriplets(a, b):
    puntosA=0
    puntosB=0
    for i in range (0,3):
        if a[i]<b[i]:
            puntosB+=1
        elif a[i]>b[i]:
            puntosA+=1

        puntosTotales=[puntosA, puntosB]
    return puntosTotales

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'] + 'solucion2.txt', 'w')
     
    print("Escribe las notas de a")
    a = list(map(int, input().rstrip().split()))

    print("Escribe las notas de b")
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    ```
