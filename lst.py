list_1 = []
n = int(input("Enter the number of elements: "))
for i in range(0, n):
    el = int(input())
    list_1.append(el)
    
# los = list(map(lambda x: {x}, list_1))        => to print list of numbers
los = list(map(lambda x: x ** 3, list_1))      #=> to print list with cubes
print("List of set:", los)