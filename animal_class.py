class animal():

    # characteristics
    def __init__(self, name, type , eyes = 2): # runs only once whne you intialise an object
        self.name = name
        self.number_eyes = eyes
        self.alive = True
        self.number_animal_eaten = 0
        self.age = 0
        self.type = type

    # behaviours - functions that belong to a class.
    # Methods - functions that can only be used on this class's instance
    def eat(self, food = 'Fajitas'):
        return 'NOM NOM NOM' + ' ' + food

    def sleep(self):
        return 'ZZZZZZZ ZZOOO ZLEEPY'

    def hunt(self):
        return 'ATTAAACCCKKKKK!!!! THIS IS SPARTA'

    def potty(self):
        return '0_0...... HUNNNNHH.... O_O HUHHHHH.....HHUHH!! O_O SPOSH! -.- :D'

    def roar(self):
        return 'GGUUUUUUUrrrrrrrrrrrrrrrrrrrrr'

# Let's create an object of class Animal :)
    # Initialising an object

# my_animal = animal()   # this is where an instance of class animal was created
# print(my_animal)
# print(type(my_animal))
