class Underscore:
    def map(self, iterable, callback):
        for i in range (len(iterable)):
            iterable[i]=callback(iterable[i])
        return iterable

    def find(self, iterable, callback):
        for i in range (len(iterable)):
            if callback(iterable[i])== True:
                return iterable[i]

    def filter(self, iterable, callback):
        dato=[]
        for i in range (len(iterable)):
            if callback(iterable[i])==True:
                dato.append(iterable[i])
        return dato
                

    def reject(self, iterable, callback):
        dato=[]
        for i in range (len(iterable)):
            if callback(iterable[i])==True:
                dato.append(iterable[i])
        return dato



# has creado una libreria con 4 métodos
# se crea la instancia de la clse
_ = Underscore() # sí, estamos configurando una instancia a una variable que es un guión bajo
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# debe retornar [2, 4, 6] después que termines de implementar el código de arriba

print(_.map([1,2,3], lambda x: x*2)) # debe retornar [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # debe retornar el primer valor que es mayor que 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2!=0)) # debe retornar [1,3,5]