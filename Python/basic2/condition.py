# If statement is used to run code conditionally.

#if condition is true code is executes & if false code is not executed

# if , elif and else to add multiple conditions

age = input("Enter your age: ")

age = int(age)

if age >= 18:
    print("You are adult")
else:
    print("You are minor")



## Another condition we can use `while` instead
# This while loop will run until the conditions is true

num = 8
guess = int(input("Enter a number: "))

while guess != num:
    guess = int(input("Enter a number: "))
else:
    print("The number is correct")