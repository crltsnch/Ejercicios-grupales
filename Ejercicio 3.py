#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#
def aVeryBigSum(ar):
# Write your code here
    suma = 0
    for i in ar:
        suma+=i
    return suma

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'] + 'solucion3.txt', 'w')
    print("Escribe un número")
    ar_count = int(input().strip())
    print("Escribe la lista de números")
    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()