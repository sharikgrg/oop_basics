class monster():
    def __init__(self, name, skills, int(height), eyes = 2): # runs only once whne you intialise an object
        self.name = name
        self.number_eyes = eyes
        self.fur_type = True
        self.skills = [skills]
        self.cuteness = 0
        self.height = height
    def scare(self):
        return 'GURRRRRRRRRRRR'
    def eat(self):
        return 'GUmp GUMP GUMP GUMP'
    def transforn(self):
        return 'beeeep beeeeep beeeeeeeeeeeeeeeeeeeeeeep'
    def run(self):
        return "Never, Monster's walk"
    def fart(self):
        return 'puitttttttttttt'
    def laugh(self):
        return 'HIGAGAGAGAG AGAGAGGAGAGA'