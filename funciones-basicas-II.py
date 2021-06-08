""" 1- Cuenta regresiva : crea una función que acepte un número como entrada. 
Devuelve una nueva lista que cuenta hacia atrás en uno, desde el 
número (como el elemento 0) hasta 0 (como el último elemento).
Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0] """

def num(numero):
    nuevalista=[]
    for i in range(numero,0,-1):
        nuevalista.append(i)
        #print(nuevalista)
    return nuevalista
numero = num(10)
print(numero)
        



"""2- Imprimir y volver : crea una función que recibirá una lista con dos números. 
Imprima el primer valor y devuelva el segundo.
Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2 """

def num(numero):
    for i in range(0,len(numero),1):
        print(numero[0])
        devo=numero[1]
    return devo
numero = num([5,7])
print(numero)


"""3- First Plus Length : crea una función que acepta una lista y devuelve la suma 
del primer valor de la lista más la longitud de la lista """

def num(numero):
    for i in range(0,len(numero),1):
        devo=numero[0]+len(numero)
    return devo
numero = num([1,2,3,4])
print(numero)


"""4- Valores mayores que el segundo : escribe una función que acepte una lista y crea 
una nueva lista que contenga solo los valores de la lista original que sean mayores 
que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. 
Si la lista tiene menos de 2 elementos, haga que la función devuelva False
Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
Ejemplo: values_greater_than_second ([3]) debería devolver False """

def lista(lista):
    nuevaLista=[]
    if len(lista) < 2:
        return False
    else:
        for i in range (len(lista)):
            if lista[i] > lista[1]:
                nuevaLista.append(lista[i])
        return nuevaLista

listaArr=lista([1,2,3,4,5,6])
print(listaArr)



"""5- Esta longitud, ese valor : escribe una función que acepte dos enteros como 
parámetros: tamaño y valor. La función debe crear y devolver una lista cuya 
longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2] """


def lista(a,b):
    lista=[]
    for x in range(0,b,1):
        lista.append(x)
        lista[x]=a
    return lista

listaArr=lista(7,8)
print(listaArr)