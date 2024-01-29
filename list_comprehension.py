fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# with looping
newlist1 = []
for x in fruits:
    if "a" in x:
        newlist1.append(x)
print("newlist1:", newlist1)

# with list comprehension
newlist2 = [x for x in fruits if "a" in x]
print("newlist2:", newlist2)