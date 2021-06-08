# 1. TAREA: imprimir "Hola mundo"copy
print("Hola Mundo")
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Noelle"
print("Hola", name)	# con una coma
print("Hola " +name)	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
name = 42
print("Hola", name)	# con una coma
print("Hola " + str(name))	# con un + - !Este debería darnos un error!
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Me encanta comer {} y {}".format(fave_food1, fave_food2) ) # con .format()

x="Hola mundo"
print(x.title()) # con una cadena


#####################PRUEBAS EXTRAS################################

nombre= "jimmy duarte"
print("mi nombre en mayuscula",nombre.upper())
print(f"mi nombre es mayuscula {nombre.upper()}")


nombre= "JIMMY DUARTE"
print("mi nombre en mayuscula",nombre.lower())
print(f"mi nombre es mayuscula {nombre.lower()}")


