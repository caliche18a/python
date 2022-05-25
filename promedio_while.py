promedio, total, contar = 0.0, 0, 0

nota = float(input("Ingrese la nota del estudiante (-1 para salir): "))
while nota != -1:
    total += nota
    contar += 1

    if contar == 3:
        break
    nota = float(input("Ingrese la nota del estudiante (-1 para salir): "))

promedio = total / contar
print("El promedio de la nota es: "+str(promedio))