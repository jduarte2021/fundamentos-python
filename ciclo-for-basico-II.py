"""1- Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5] """

def lista(lista):    
    for i in range(len(lista)):
        if lista[i] > 0:
            lista[i]="big"
    return lista

listaArr=lista([-1,2,3,-4,5])
print(listaArr)


"""2- Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. 
(Tenga en cuenta que cero no se considera un número positivo).
Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve """

def lista(lista):
    cont=0    
    for i in range(len(lista)):
        if lista[i] > 0:
            cont+=1
    lista[-1]=cont
    return lista

listaArr=lista([1,2,4,5,-5,-7])
print(listaArr)



"""3- Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
Ejemplo: sum_total ([6,3, -2]) debería devolver 7 """

def lista(lista):
    su=0
    suma=0    
    for i in range(len(lista)):
        su=lista[i]
        suma+=su
    return suma

listaArr=lista([1,2,4,2,1,-2])
print(listaArr)




"""4- Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5 """

def lista(lista):
    su=0
    suma=0    
    for i in range(len(lista)):
        su=lista[i]
        suma+=su
        prom=suma/len(lista)
    return prom

listaArr=lista([1,2,4,2,1,7,9,3])
print(listaArr)



"""5- Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
Ejemplo: longitud ([]) debería devolver 0 """

def lista(lista):
    cont=0    
    for i in range(len(lista)):
        cont+=1
    return cont

listaArr=lista([0,1,2,3,4,5,6,7,8])
print(listaArr)



"""6- Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
Ejemplo: mínimo ([]) debería devolver False """

def lista(lista): 
    for i in range (len(lista)): 
        if len(lista)<0:
            return False
        else:
            maximo=max(lista)
            return maximo


listaArr=lista([1,2,20,4,5,6])
print(listaArr)



"""7- Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
Ejemplo: máximo ([]) debería devolver False """

def lista(lista): 
    for i in range (len(lista)): 
        if len(lista)<0:
            return False
        else:
            minimo=min(lista)
            return minimo


listaArr=lista([1,2,20,-4,5,6])
print(listaArr)


"""8- Análisis final : crea una función que tome una lista y devuelva un diccionario 
que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4} """

def lista(lista):
    su=0
    suma=0    
    for i in range(len(lista)):
        su=lista[i]
        suma+=su
        prom=suma/len(lista)
        minimo=min(lista)
        maximo=max(lista)
        longitud=len(lista)
    diccionario = {'Suma total' : suma, 'Promedio' : prom, 'Minimo' : minimo, 'Maximo' : maximo, 'Longitud de Lista' : longitud}
    return diccionario

listaArr=lista([1,2,4,2,1,7,9,3])
print(listaArr)

"""9- Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda 
lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37] """


def lista(lista):    
    return lista[::-1]

listaArr=lista([-1,2,3,-4,5])
print(listaArr)

