class Animal:
    def speak(self):
        print("Animal Speeaking")
        
class Dog(Animal):
    def bark(self):
        print("Dog Barking")
        
class ChildDog(Dog):
    def eat(self):
        print("childDog Eating")
        
d = ChildDog()
d.speak()
d.bark()
d.eat()