num = int(input("Enter the number: "))
if num % 2 == 0:
    print("Number is even!")
else:
    print("Number is odd!")

if num == 1:
    print("Number is not a prime number!")
elif num > 1:
    for i in range(2, num):
        if(num % i == 0):
            print("Number is not a prime number!")
            break
        else:
            print("Number is a prime number!")
            break
else:
    print("Number is not a prime number!")    