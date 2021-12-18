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

def jugadaoptima(n):
    jugadabuena=0
    modulo=n%7
    if(modulo>=2 and modulo<=3):
        jugadabuena=2
    elif(modulo==4):
        jugadabuena=3
    elif(modulo>=5 and modulo<=6):
        jugadabuena=5
    return jugadabuena

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        fptr.write(result + '\n')
    fptr.close()