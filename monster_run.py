from monster_hw import *
my_monster = monster('Grumpy', ['sure', 'not'], 300)   # this is where an instance of class animal was created
print(my_monster.name.height)
print(my_monster.skills)
print(my_monster.height)
print((my_monster).eat())



my_monster2 = monster('Frank', ['some', 'no'], 3)
print(my_monster.name.height)
print(my_monster.skills)
print(my_monster.height)
print((my_monster).eat())


my_monster3 = monster('Godzilla', ['die', 'yes'], 300)
print(my_monster.name.height)
print(my_monster.skills)
print(f' Height in meters {my_monster.height}')
print((my_monster).eat())