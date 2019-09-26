from animal_class import*
class Reptile(animal): ## inheritance
    # it will run all the same method as animal
    # because all it knows
    def __init__(self, name,type, number_hearts, camouflage, eyes = 2):
        super().__init__(name, type, eyes) # Run the _init_ in parent class
        self.number_h = number_hearts
        self.camo = camouflage
    # the above method overrides the previous init method. Howeve
    # the super call the previous init method so out object does have all of the previous characteristics
    # an then!! we added more characteristics.

    def eat(self, food = 'bugs'): # method polimorphism whee we override the method eat()
        return ('waittttfooorrrrrrrr itttt andddddd Pounce!! NOM' + food)

    def seek_heat(self):    # adding new methods to this class
        return 'Humm bit chilly, where that sun at? why did I sit at the back of the class?'
    pass