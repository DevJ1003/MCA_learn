f = open("new.txt", "a")
f.write("write-the-old")

f = open("new.txt", "r")
print(f.read())

d = open("old1.txt", "x")
d.write("Hello-world")
d = open("old1.txt", "r")
print(d.read())