class animal:
    def sound(self):
        print("Animals make sounds")
class dog(animal):
    def sound(self):
        print("Dogs:Bark")
class cat(animal):
    def sound(self):
        print("cats:Meow")
        
a=animal()
c=cat()
d=dog()

a.sound()
c.sound()
d.sound()


