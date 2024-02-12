"""
We can use 'and' OR "or" OR 'not' operator to validate to conditions

for `and`
True and True = True
True and False = False
False and Ture = False
False and False = False

for `or`
True or True = True
True or False = True
False or True = True
False or False = False

for `not`
not True = False
not False = True
"""

x = 10
y = 15

if (x >= 18 and y >= 18):
    print("You both are adult")
elif (x >= 18 or y >= 18):
    print("One of you are adult")
else:
    print("You both are minor")


hungry = True
if (not hungry):
    print("You are not hungry")
else:
    print("You are hungry")