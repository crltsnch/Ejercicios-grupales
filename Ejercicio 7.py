import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
    list=[]
    for grade in (grades):
        list.append(finalgrade(grade))
    return list

def finalgrade(grades):
    roundgrade=0
    if(grades<40):
        roundgrade=grades
    else:
        cociente=int(grades/5 + 1)
        multiplo=cociente*5
        if(multiplo-grades<3):
            roundgrade=multiplo
        else:
            roundgrade=grades
    return roundgrade