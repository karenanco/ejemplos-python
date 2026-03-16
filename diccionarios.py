import os

## diccionarios
#una estructura de datos

#que guarda datos en formato clave , valor

#  clave  :    valor
# "nombre":"cristian"


persona = {
    "nombre" : "carlos",
    "edad" : 28,
    "direccion": "calle falsa 123",
    "ciudad" : "valparaiso"
}


# acceder a los valores de nuestro diccionario con ["keys"]
#print(persona["ciudad"])

#modificar valores

persona["edad"] = 35
persona["nombre"] = "carla"



#agregar un dato nuevo 

persona["pais"] = "chile"
persona["altura"] = 190

#print(persona)


#  recorrer el diccionario
# iterar keys
""" for k in persona:
    print(k)

##iterar values
for v in persona.values():
    print(v)

# iterar todo 
for k , v in persona.items():
    print(k,v) """


""" #lista de diccionarios de alumnos 
alumnos = []


while True:

    print("--------menu--------")
    print("1. agregar alumno")
    print("2. ver alumnos")
    print("3. salir")

    opcion = input("elige una opcion")
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcion == "1":
        nombre = input("nombre de alumno")
        edad = input("edad del alumno")

        alumno = {
            "nombre":nombre,
            "edad": edad
        }
        alumnos.append(alumno)

        print("alumno agragado!!!!")

    elif opcion == "2":

        print("------lista de alumnos-----")

        for alumno in alumnos:
            print(alumno["nombre"], "--",alumno["edad"])
    
    elif opcion == "3":
        print("programa cerrado")
        break

    else:
        print("opcion no correcta solo se acepta 1,2 y 3 programa cerrado")
        break

     """



# proyecto de lista de peliculas netflix 

""" pelicula = {
    nombre : nombre
    anio:anio
    actores: [actor1,actor2...]
    } """

#peliculas=[{pelicula1},{pelicula2}...]


#flujo del programa
'''

generar la lista vacia
peliculas=[]


MIENTRAS EL PROGREAMA ESTE CORRIENDO
imprimir 
menu 
1. agregar pelicula a la lista
2. borrar
3. ver
4. salir

que el usuario entrege la opcion 

si el usuario eligio 1
        ingresamos nombre de la pelicula
        ingresamos al anio
        ingresar genero 
        pelicula = {
            nombre : nombre
            anio:anio
            genero:genero]
            }
        agregar la pelicula a la lista(append)
        mesaje que la pelicula esta guardada

si el usuario eligio 2 
           ingresar la pelicula a borrar 
           buscamos la pelicula a borrar
           borramos
   
si el usuario eligio 3
        ver listado
si el usuario eligio
        mensaje de salida 
        break
        
si el usuario puso otra cosa el program se cierra

'''

peliculas=[]

while True:
    print("menu")
    print("1. agregar pelicula a la lista")
    print("2. borrar")
    print("3. ver lista de pelis pelis")
    print("salir")

    opcion = input("ingrese la opcion")

    if opcion == "1":
        nombre = input("ingresar nombre de la pelicula")
        genero = input("ingresar genero de la pelicula")
        anio = input("ingresar anio de la pelicula")

        pelicula = {
            "nombre" : nombre,
            "anio":anio,
            "genero":genero
            }
        peliculas.append(pelicula)
        print("pelicula esta guardada")    
    elif opcion == "2":
        peli_borrar = input("ingresa la peli a borrar")
         
        for peli in peliculas:
            
            if peli["nombre"] == peli_borrar:
                peliculas.remove(peli)
                print("peli borrada")
                break
    elif opcion == "3":
        print(peliculas)

        

    elif opcion == "4":
        print("programa terminado!!!")
        break


    else:
        print("opcion no valida terminando programa")
        break








#quiero guardar datos de google maps en una base de datos




 




















