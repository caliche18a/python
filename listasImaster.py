nombres = []
edades = []
cantidad = int(input("Ingrese la cantidad de personas: "))
for i in range(cantidad):
    nom = input("Ingrese el nombre de la persona: ")
    nombres.append(nom)
    edad = int(input("Ingrese la edad de dicha persona: "))
    edades.append(edad)

print("Nombre de las personas mayores de edad: ")

for i in range(cantidad):
    if edades[i] >= 18:
        print(nombres[i]+" de "+ str(edades[i])+ " años.")