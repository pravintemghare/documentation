# Python uses for to create loops in code.
# use key word `break` to break out of the loop
# use key word `continue` to skip that value and continue the loop

for i in range(5):
    print ("i is: ", i)


for i in range(5):
    if i == 2:
        break
    print ("i is ", i)

for i in range(5):
    if i ==3:
        continue
    print ("i is ", i)