n=int(input("Escriba el tamaño de la escalera: "))
def piramide(i):
    for numbers in range(i):
        print((i-numbers+1) * " " + numbers * "#")
piramide(n)