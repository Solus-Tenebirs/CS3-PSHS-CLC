class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def take_damage(self, amount):
        self.hp -= amount

Arthur = Hero("Arthur", 100)
Morgana = Hero("Morgana", 60)

Arthur.take_damage(10)

print(f"{Arthur.name} has {Arthur.hp} left. {Arthur.name}'s max hp is 100")
print (f"{Morgana.name} has {Morgana.hp} left. {Morgana.name}'s max hp is 60")
        

