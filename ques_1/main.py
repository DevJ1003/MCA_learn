import add
import sub
import mul
import div

a = int(input("Enter the 1st digit: "))
b = int(input("Enter the 2nd digit: "))

# print and calling statements for the functions
print("Add for these values:", add.f_add(a,b))
print("Sub for these values:", sub.f_sub(a,b))
print("Mul for these values:", mul.f_mul(a,b))
print("Div for these values:", div.f_div(a,b))