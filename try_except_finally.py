a = ["Python", "Exceptions", "Hello"]

try:
    for i in range(0, 4):
        print("The index and element are ", i, a[i])
        
except:
    print("Index out of range")
    
finally:
    print("I will print every time")