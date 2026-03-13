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

# Proyecto de lista de películas netflix

pelicula = {
    nombre : nombre
    anio : anio
    actores : [actor1,actor2...]
}

# peliculas=[{pelicula1},{pelicula2}...]
# int()  

#flujo del programa
'''
generar lista vacia
peliculas=[]
imprimir
-----Menú-----
1. Agregar
2. Borrar
3. Ver
4. Salir

que el usuario entregue la opción

si el usuario eligió 1
        ingresar nombre de la pelicula
        ingresar anio de la pelicula
        ingresar género
        pelicula = {
            nombre : nombre
            anio :anio
            actores : [actor1,actor2...]
            }
        agregar la película a la lista (append)
        mensaje que la película está guardada

si el usuario eligió 2
        ingresar la pelicula a borrar
        buscamos la pelicula a borrar
        borramos

si el usuario eligió 3
        ve el listado

si el usuario eligió 4
        mensaje de salida
        break

si el usuario puso otra cosa, el progama se cierra

'''

peliculas = []

while True:
    print("-----------Menú----------")
    print("1. Agregar")
    print("2. Borrar")
    print("3. Ver")
    print("4. Salir")

    opcion = input(ingrese la opcion)

    if opcion == "1":
        nombre = input("Ingresar nombre de la película")
        nombre = input("Ingresar anio de la película")
        nombre = input("Ingresar género de la película")

        pelicula = {
            "nombre" : nombre,
            "anio" :anio,
            "genero" : genero
            }
        peliculas.append(pelicula)
        print("la pelicula esta guardada")
    elif opcion == "2":
        peli_borrar = input("ingresa la peli a borrar")

        for peli in peliculas:

            if peli["nombre"] == peli_borrar:
    elif opcion == "3":
    elif opcion == "4":
    else: 
        print("opcion no valida")
    