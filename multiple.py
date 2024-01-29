class Cal1:
    def add(self, a, b):
        return a+b
        
class Cal2:
    def sub(self, a, b):
        return a-b
    
class Cal3(Cal1, Cal2):
    def mul(self, a, b):
        return a*b
    
d = Cal3()
print(d.add(3, 2))
print(d.sub(3, 2))
print(d.mul(3, 2))