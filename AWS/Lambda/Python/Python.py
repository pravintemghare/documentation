##### Print Function

print('Hello Lambda')

##### Variable

response = 3
print(response)

##### User Input
# syntax iput("input")
s = input('Name of your school')

# print in string .format(a,b)
grade = input("your grade")

print("my school name {} and grade {}".format(s,grade))

##### Data Type - Dictonary
# Curly Brackets
# Key value pair

x={1:'num1',2:'num2'}
print(x[2])
# Nested Dictonary
y={1:'num1',2:{'two':'too','aws':'lambda'}}
print(y[2]['aws'])

##### Dictonary Boto3

response = {
    'Buckets': [
        {
            'Name': 'string',
            'CreationDate': 25
        },
    ],
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    }
}

print(response['Buckets'])


###### Data type - List
# Square brackets
# Data type: string, integers, objects
# list in python are ordered

newlist = ['one','55','hundred','Pravin']
print(newlist[3])

# Slicing 
# slice(start:stop:step)
print(newlist[0:3:2])
# reverse[::-1]
print(newlist[::-1])

###### Data Type - Nested List
nestedlist = [[1,2,3],[4,5,6],[7,8,9]]
print(nestedlist[1][2])


###### Dictonary & List

newresponse = {
    'Buckets': [
        {
            'Name': 'bucket1',
            'CreationDate': 25
        },
        {
            'Name': 'bucket2',
            'CreationDate': 26
        },
    ],
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    }
}

print(newresponse['Buckets'][1])
print(newresponse['Buckets'][1]['Name'])


###### Determine data type

print(type(newresponse))


##### Function
# Function is a block of code which runs when it is called
# syntax:
# def function_name (argument/parameters):
def oddeven (x):
    if (x % 2 == 0):
        print('even')
    else:
        print('odd')

oddeven(44)

# sample lambda function
def lambda_handler (event, context):
    # Your code here
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from lambda")
    }

###### For loop
test = ['hello','world']

for x in test:
    print(x)

###### Length function
# retuns the length of a string
newtest = 'pravin'
print(len(newtest))