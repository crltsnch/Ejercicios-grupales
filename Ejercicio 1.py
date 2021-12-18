
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