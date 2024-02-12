## Creating own function. Which helps to repeat a section of code
## function start with key word `def`
## if key word 'return' is used in the function it stops the execution of the rest of the function body

def function1():
    a = 3
    b = 5
    if (a > b):
        print("Hello")
    else:
        print("World")

function1()  # to run function

#Arguments
def input_num(num):
    return int(input("Enter a number:")) * num

newput = input_num(num = 3)
print(newput)

# return statement
def is_even(num):
    if(num % 2 == 0):
        return True
print(is_even(7))

# list argument
def multiply_values(list):
    multiplied_values = []
    for item in list:
        multiplied_values.append(item * 2)
    return multiplied_values

print(multiply_values([1,2,3,-4]))

# Scopes
def input_num(num):
    result = int(input("Enter a number:")) * 100
    return result
print(input_num(3))

#Arguments
age = 22
def multiply(num):
    num *= 2
    print("In multiply:", str(num))

multiply(age)
print(age)