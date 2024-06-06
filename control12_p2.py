lista=[]
carácter = "bcdefghijklmnñopqrstuvwxyz"
nombre=str(input("ingrese nombre (enter para terminar ingreso:):"))

while nombre!="":
    lista.append(nombre)
    nombre=str(input("ingrese nombre (enter para terminar ingreso):"))

for nombre in lista:
    L=0
    print(nombre)
    for letra in nombre:
        if letra in carácter:
            L=L+1
            lista.remove()
    print(lista)