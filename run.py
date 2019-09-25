from animal_class import *
my_animal = animal('Ricky', 'fish')   # this is where an instance of class animal was created
print(my_animal.name)
print(my_animal.type)
print((my_animal).eat('lasagne'))



my_animal2 = animal('Frank', 'primate', 3)
#my_animal = animal()   # this is where an instance of class animal was created
print(my_animal2.name)
print(my_animal2.sleep())
print((my_animal).eat('lasagne'))


my_animal3 = animal('Ribery', 'not sure')
print(my_animal3.animal)
print((my_animal).roar())
