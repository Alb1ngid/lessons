class Person:
    def __init__(self, name):
        self.__name = name

    def setName(self,name):
        self.__name=name


    def getName(self):
        return self.__name

    def __dead(self):
        print('dead')


p = Person('Ivan')
p.name='Beka'
print(p.name,p._Person__name)


p.setName('Vanya')
print(p.getName())
print(p._Person__name)
