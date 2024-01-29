# class Dog:
#     attr1 = "mammal"
#     attr2 = "bark"
    
#     def fun(self):
#         print("I'm a", self.attr1)
#         print("I can", self.attr2)
        
# rodger = Dog()
# rodger.fun()



class Dog:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2
        
    def fun(self):
        print("I'm a", self.attr1)
        print("I can", self.attr2)

rodger = Dog("mammal", "bark")
rodger.fun()