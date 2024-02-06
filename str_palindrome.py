str = input("Enter the string: ")
str = str.casefold()
rev = reversed(str)
if list(str) == list(rev):
    print("The string is palindrome!")
else:
    print("The string is not a palindrome!")