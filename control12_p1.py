lista=[]
alumnoPuntaje=int(input("ingrese el puntaje diario del alumno (enter para terminar ingreso:):"))
while alumnoPuntaje!="" and lista:
    lista.append(alumnoPuntaje)
    alumnoPuntaje=int(input("ingrese el puntaje diario del alumno (enter para terminar ingreso):"))
print ("puntaje diario del alumno del día 1 a día 15")
print (lista)

if alumnoPuntaje > 59 and alumnoPuntaje < 101:
    print(lista)
else:
    if alumnoPuntaje < 60:
        print(lista)
