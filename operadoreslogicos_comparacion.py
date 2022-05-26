""" OPERADORES LOGICOS """

es_estudiante = True
trabaja = False

# AND
""" El operador AND devuelve VERDADERO si y solo si TODAS las variables son verdaderas
    y devolvera falso cuando al menos una variable es falsa"""
pivot = es_estudiante and trabaja
print(f'Es estudiante Y trabaja: {pivot}')

# OR
""" El operador OR devuelve VERDADERO si y solo una de las variables es verdadera
     y devolvera falso cuando todas una variables sean falsas"""
pivot = es_estudiante or trabaja
print(f'Es estudiante O trabaja: {pivot}')

# NOT
""" NOT invierte el valor logico de una variable, de verdadero a falso y de falso a verdadero """
pivot = not es_estudiante
print(f'Estudia? invertido -> {pivot}')

pivot = not trabaja
print(f'Trabaja? invertido -> {pivot}')

""" OPERADORES DE COMPARACION """

numero1 = 5
numero2 = 5
numero3 = 7

#IGUALDAD
pivot = numero1 == numero2
print(f'Es n1 igual a n2 -> {pivot}')
pivot = numero1 == numero3
print(f'Es n1 igual a n3 -> {pivot}')

#DISTINTO
pivot = numero1 != numero3
print(f'Es n1 distinto a n3 -> {pivot}')

#MAYOR
pivot = numero1 > numero3
print(f'Es n1 mayor a n3 -> {pivot}')

#MENOR
pivot = numero1 < numero3
print(f'Es n1 menor a n3 -> {pivot}')

#MAYOR-IGUAL
pivot = numero1 >= numero2
print(f'Es n1 mayor o igual a n2 -> {pivot}')

#MENOR-IGUAL
pivot = numero1 <= numero2
print(f'Es n1 menor o igual a n2 -> {pivot}')