import math
import os
import random
import re
import sys

class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def comparate(self,x,y):
        if(self.x==x and self.y==y):
            return True
        else:
            return False

class Tunel:
    def __init__(self, x1, y1, x2, y2):
        self.extremo1 = Coordenadas(x1, y1)
        self.extremo2 = Coordenadas(x2, y2)
def buscaTunel(Casillax,Casillay,tuneles):
    coordenadas = Coordenadas(Casillax, Casillay)
    for t in tuneles:
        if(t.extremo1.comparate(Casillax,Casillay)==True):
            coordenadas.x=t.extremo2.x
            coordenadas.y=t.extremo2.y
            break
        elif(t.extremo2.comparate(Casillax,Casillay)==True):
            coordenadas.x=t.extremo1.x
            coordenadas.y=t.extremo1.y
            break
    return coordenadas

def exploracion(Casillax, Casillay, laberinto, n , m, tuneles):
    num=0
    den=0
    probabilidad=0.0
    if(Casillax>0 and laberinto[Casillax-1][Casillay]!="#"):
        den +=1
        if(laberinto[Casillax-1][Casillay]=="%"):
            num+=1
    if(Casillax<n-1 and laberinto[Casillax+1][Casillay]!="#"):
        den +=1
        if(laberinto[Casillax+1][Casillay]=="%"):
            num+=1
    if(Casillay<m-1 and laberinto[Casillax][Casillay+1]!="#"):
        den +=1
        if(laberinto[Casillax][Casillay+1]=="%"):
            num+=1
    if(Casillay>0 and laberinto[Casillax][Casillay-1]!="#"):
        den +=1
        if(laberinto[Casillax][Casillay-1]=="%"):
            num+=1
    if(den==0):
        return probabilidad
    probabilidad=num/den
    if(Casillax>0 and laberinto[Casillax-1][Casillay]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax-1,Casillay,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den
    if(Casillax<n-1 and laberinto[Casillax+1][Casillay]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax+1,Casillay,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den
    if(Casillay<m-1 and laberinto[Casillax][Casillay+1]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax,Casillay+1,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den
    if(Casillay>0 and laberinto[Casillax][Casillay-1]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax,Casillay-1,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=(exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den)
    return probabilidad



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])
    for n_itr in range(n):
        row = input()
# Write your code here
    for k_itr in range(k):
        second_multiple_input = input().rstrip().split()
        i1 = int(second_multiple_input[0])
        j1 = int(second_multiple_input[1])
        i2 = int(second_multiple_input[2])
        j2 = int(second_multiple_input[3])
# Write your code here
# Write your code here