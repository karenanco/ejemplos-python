## diccionarios
#una estructura de datos

#que guarda datos en formato clave, valor
#clave:valor
#"nombre:"cristian"

""" persona = {
    "nombre" : "carlos",
    "edad" : 28,
    "dirección" : "calle falsa 123",
    "ciudad" : "valparaiso"
}

print(persona) """

#acceder a los valores de nuestro diccionario con ["keys"]
#print (persona["ciudad"])

#modificar valores 

""" persona["edad"] = 35
persona["nombre"] = "carla"

print(persona) """

#agregar un dato nuevo

""" persona ["pais"] = "chile"
persona["altura"] = 190

print(persona) """

#recorrer el diccionario
#iterar keys
""" for i in persona:
    print(i) """

#iterar values
""" for v in persona.values():
    print(v) """

#iterar todo
""" for k , v in persona.items():
    print(k.v)
 """

#Lista de diccionario de alumnos
alumnos = []

while True:
    print("-----------Menú----------")
    print("1. Agregar alumno")
    print("2. Ver alumnos")
    print("3. Salir")

    opcion = input("Elige una opción")

    if opcion == "1":
        nombre = input("Nombre de alumno:")
        edad = input("Edad del alumno:")

        alumno = {
            "nombre": nombre,
            "edad": edad
        }
        alumnos.append(alumno)

        print("alumno agregado!!!")

    elif opcion == "2":

        print("----------Lista de alumnos----------")

        for alumno in alumnos:
            print(alumno["nombre"], "--" ,alumno["edad"])

    elif opcion == "3":
        print("programa cerrado")
        break
    else:
        print("Opcion no correcta, solo se acepta 1,2 y 3 programa cerrado")

