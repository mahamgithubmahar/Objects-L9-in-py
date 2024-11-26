class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return "{} sings {}".format(self.name,song)
    def dance(self):
        return "{} is now dancing".format(self.name)
ob1=parrot("Woe",12)
print(ob1.sing("happy"))
print(ob1.dance())