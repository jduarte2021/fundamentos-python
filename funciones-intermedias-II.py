"""1- Actualiza los valores en diccionarios y listas """

#Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].


def lista(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i][j] == 10:
                lista[i][j]=15
    return lista
listax = lista([[5,10,3],[10,8,9]])
print (listax)


#Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
for i in range(len(students)):
    if students[i]['last_name'] == 'Jordan':
        students[i]['last_name'] = 'Bryant'

print(students)
    
####Con Funcion####

def students(students):
    for i in range(len(students)):
        if students[i]['last_name'] == 'Jordan':
            students[i]['last_name'] = 'Bryant'

    return students

stu = students([
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
])

print (stu)




#En el directorio sports_directory, cambia 'Messi' a 'Andres'


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

for key in sports_directory:
    for apellido in range(len(sports_directory[key])):
        #print(sports_directory[key][apellido])
        if sports_directory[key][apellido]=='Messi':
            sports_directory[key][apellido]='Andres'

print (sports_directory)



#Camba el valor 20 en z a 30

z = [ {'x': 10, 'y': 20} ]
for i in z:
    #print(i)
    for key, value in i.items():
        if i[key] == 20:
            i[key] = 30
print(z)
    #print(key)
    

####Con Funcion######

def z(z):
    for i in z:
        #print(i)
        for key, value in i.items():
            if i[key] == 20:
                i[key] = 30
    return z
nuevodic= z([ {'x': 10, 'y': 20} ])
print(f"Nueva Lista es {nuevodic}")


######################################
########PRUEBAS#######################

diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }
for key in diccionario:
  print (key, ":", diccionario[key])


########PRUEBAS#######################
######################################

"""2- Itera a través de una lista de diccionarios """

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
for i in range(len(students)):
    elementos = students[i].items() #Creamos la variable elementos que almacena key y values
    for key,val in elementos: # Iteramos
        print (f"{key} - {val}")
        


"""3- Obtén valores de una lista de diccionarios """

##Nombres##

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

for i in range (len(students)):
    nombre=students[i].get('first_name',"")
    print(f"{nombre}")

    ##Apellidos##

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

for i in range (len(students)):
    apellido=students[i].get('last_name',"")
    print(f"{apellido}")


"""4- Itera a través de un diccionario con valores de listas """

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
#print(dojo.get)

elementos = dojo.items() #Creamos la variable elementos que almacena key y values
for lista in dojo: 
    cont=len(dojo[lista])
    print(f"{cont} - {lista}\n {dojo[lista]}")
    


        
    
    












################PRUEBAS###########################


def students(students):
    ape=[]
    for i in range (len(students)):
        apellido=students[i].get('last_name',"")
        ape.append(apellido)
    return ape

stu = students([
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}])
print(stu)



students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
for i in range(len(students)):
    elementos = students[i].items() #Creamos la variable elementos que almacena key y values
    for key,val in elementos: # Iteramos
        print (f"{key} - {val}")



""" semaforo = {'Rojo' : 'Detenerse', 'Amarillo' : 'Despacio', 'Verde' : 'Avanzar'}
elementos = semaforo.items() #Creamos la variable elementos que almacena key y values
for k,v in elementos: # Iteramos
    print ((k), ('significa'), (v)) """