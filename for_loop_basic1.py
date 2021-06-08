############################################
##BASICO##
for i in range (0,151,1):
    print(i)

##MULTIPLOS DE CINCO##

for i in range (5,1001,1):
    if i%5==0:
        print(i)

##CONTAR, DOJO WAY##

for i in range (5,1001,1):
    if i%5==0:
        i="Coding"
    else:
        i%10==0
        i="Coding Dojo"
    print(i)

##¡Uf, Eso es bastante grande!##
sum=0
for i in range (0,10,1):
    if i%2==0:
        x=i
    else: 
        sum += i
print(sum)
    
##Cuenta regresiva por cuatro ##

for i in range (100,1,-1):
    if i< 4:
        break
    print(i-4)

##Contador Flexible - 
# establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
# imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, 
# el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)##

lowNum=3
highNum=12
mult=3
for i in range (lowNum,highNum,1):
    if i%3==0:
        print(i)
