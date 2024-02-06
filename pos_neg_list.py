n = int(input("Enter the number of elements in list: "))
numbers = []
pos_numbers = []
neg_numbers = []
for i in range(n):
    num = int(input(f"Enter the element:"))
    numbers.append(num)
    
for num in numbers:
    if num > 0:
        pos_numbers.append(num)
    elif num < 0:
        neg_numbers.append(num)
        
print("Positive numbers: ", pos_numbers)
print("Negative numbers: ", neg_numbers)