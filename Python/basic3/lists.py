"""
List is a collection of multiple elements.
Each element is a scaler and each element has an index.
The first element in the list has index 0 second index 1 and so on.

Functions in list:
`len` function allows to take length of the list
`del` function to delete a element in the list

Methods in list:
append, sort, reverse, insert

iterating lists: For loop over a list
"""

list_eg = ["USA", "INDIA", "JAPAN"]

print(list_eg)

#Change index value
list_eg[2] = "UK"
print(list_eg)

#Check length of list
print (len(list_eg))

del(list_eg)[1]
print(list_eg)


## methods
list_eg.insert(1, "INDIA")
print(list_eg)

list_eg.append("ITALY")
print(list_eg)

#swap list
list_eg[0], list_eg[1] = list_eg[1], list_eg[0]
print(list_eg)

#sort list
list_eg.sort()
print(list_eg)

#revers list
list_eg.reverse()
print(list_eg)

# iterating through the list using for loop
ages = [56, 36 , 45 , 88]
total = 0
for age in ages:
    total += age

avg_age = total / len(ages)
print(avg_age)

## Slicing list
# list[start:end] - includes the starting index and exclude the end index

letters = ["A", "B", "C", "D", "E"]
list1 = letters[0:3]
list2 = letters[1:]
list3 = letters[:4]
list4 = letters[1:-1]

del letters[1:3]

## Find in lists

print("B" in letters)
print("Z" not in letters)

## Nested lists
# list which consists of other list are 2d lists
main_list = [[1,2,3],[4,5,6],[7,8,9]]

print(main_list[1][2])
# list which consists of list of other lists are 3d lists
new_list = [["A"["WW","EE","EV"],"B","C"]]
print(new_list[0][1])