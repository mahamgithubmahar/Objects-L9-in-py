class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
ob1=parrot("Maham",14)
ob2=parrot("Woe",2)

print("Maham is a",ob1.species)
print("Maham is a {}" .format(ob1.species))
print("Woe is a {}".format(ob2.species))
print("{} is {} years old".format(ob1.name,ob1.age))
print("{} is {} years old".format(ob2.name,ob2.age))