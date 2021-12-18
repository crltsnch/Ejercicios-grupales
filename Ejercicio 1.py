
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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()