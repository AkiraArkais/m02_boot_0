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