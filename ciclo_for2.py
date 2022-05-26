datos_basicos ={
    "nombre":"Carlos",
    "apellidos":"Jiménez Avendaño",
    "cedula":"8010650240",
    "fechanacimiento":"14 de enero de 1986",
    "lugarnacimiento":"Amalfi Antioquia",
    "nacionalidad":"Colombiano",
    "estadocivil":"Soltero"
}
clave = datos_basicos.keys()
valor = datos_basicos.values()
cantidadDatos = datos_basicos.items()
#print(clave)
#print(valor)
#print(cantidad)

for clave,valor in cantidadDatos:
    print(clave +": "+valor)
