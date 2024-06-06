lista=[]
palabra=str(input("ingrese palabra (enter para terminar ingreso:):"))
while palabra!="":
    lista.append(palabra)
    palabra=str(input("ingrese palabra (enter para terminar ingreso):"))
print(lista)

for i in range(len(palabra)):
    print(lista[i])

for palabra in lista:
    l=0
    for carácter in palabra:
        l=l+1
print("el número de carácteres es de:", l)
