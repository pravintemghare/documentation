## Boto3 for AWS 

- AWS SDK for python is ``boto3``
- Boto3 library makes it easy to integrate with AWS services including Amazon S3, EC2, Dynamo DB and more using Python.

### Boto3 has two distinct levels of API's

#### Client APIs
- Provides low-level interface to the AWS service
- All AWS services operation supported by client

#### Resource APIs
- Provides high-level abstraction compared to client
- Few AWS service operations not supported

############################################################################
############################################################################

### Usecase with Lambda
- botocore.response - Read Method (convert botocore response to read method using)
    ``print(response).read()``

- Convert bytes to string & strings to byte
    Unicode provides a unique way to define every character in every spoken language of world by assigning it a unique number. Among these UTF-8 is most popular.
    ASCII == UNICODE
    - Bytes to string
        s = b.decode('UTF-8')
    - String to byte
        b = s.encode('UTF-8')

- Serialization and De-serialization
    Serialization is a process of converting an object into a special format which is suitable for transmiting over the network or storing in file or database. In case of JSON, when we serializing objects, we essentially convert a Python object into a JSON string
    De-serialization is reverse of serialization. It converts the special format returned by the serialization back into a usable object. It builds up the Python object from its JSON string representation 

- Python provides a built-in module called json for serializing and deserializing objects
    Loads:
        JSON to Dictonary
        Y = json.loads(variable)
    Dumps:
        Dictonary to JSON
        X = json.dumps(variable)

