pesos = float(input("¿Cuántos pesos colombianos tienes:? "))
dolar = 3930.83

dolares = pesos / dolar
dolares = round(dolares, 2)

print("Usted tiene hoy $ "+str(dolares)+" dólares.")

