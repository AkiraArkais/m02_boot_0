#Object/Class
class Dog():
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.weight = w
        
    def bark(self):
        if self.weight >=30:
            print("GUAU, GUAU")
        else:
            print("guau, guau")
        
    def __str__(self):
        return "Soy el perro {}".format(self.name)

#Happy Dog Subclass
class HappyDog(Dog):
    def __init__(self, n, a, w, o):
        Dog.__init__(self, n, a, w)
        self.owner = o
        self.happy = True
        
    def __str__(self):
        return "{}, el perro feliz, es de {}".format(self.name, self.owner)
    
    def walk(self):
        print ("{} tira de la correa y se lleva piedras a casa de {}".format(self.name, self.owner))
        
#Wolf Dog Subclass
class WolfDog(Dog):
    def __init__(self, n, a, w, o):
        Dog.__init__(self, n, a, w)
        self.owner = o
        self.wolf = True
        self.__hunting = False
        
    def __str__(self):
        return "{}, el perro lobo, es de {}".format(self.name, self.owner)
    
    def howl(self):
        if self.__hunting:
            print("Shhhhh, calla que se escapa")
        else:
            print("AUUUUUUUUUUUUUUUUUUUU")
            
    def hunting(self, value=None):
        if value == None:
            return self.__hunting
        else:
            self.__hunting = value