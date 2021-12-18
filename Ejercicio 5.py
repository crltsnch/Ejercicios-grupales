#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#
def gameOfStones(n):
# Write your code here
    ganador=""
    if(jugadaoptima(n)!=0):
        ganador="P1 is the winner"
    else:
        ganador ="P2 is the winner"
    return ganador


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        fptr.write(result + '\n')
    fptr.close()