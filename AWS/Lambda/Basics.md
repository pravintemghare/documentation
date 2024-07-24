# Basics of Lambda Functions


## Evolution from Physical servers to Lambda

- Physical Servers
- Virtual Servers
- Cloud Computing

#### Lambda is a function as a service. Service provided by cloud providers

Lambda is a compute service that let you run code without provisioning or managing servers. Lambda runs your code on high availibility compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scalling, and logging.

### Key feature
1. Compute Service
2. Highly Available
3. All of the administration of the compute resources, including server and operating system, autoscaling and logging.
4. Privisioning done by AWS and Pay as you go use.
5. Bring your code and run on Lambda
6. Lambda is a serverless, event driven compute service.

### Usecase for Lambda
- Event Driven
- Unpredictable demand

### When not to use a AWS Lambda
- When you need to manage the infrastructure
- Need to run the Servers Continously instead of event driven.

### Lambda Execution Role
- A Lambda execution role is an AWS IAM role that grants the fuction permission to access AWS services and resources
- Default Lambda Function Role Permission
- AWS LambdaBasicExecutionRole: grants permission to upload logs to CloudWatch.
- Need to provide an execution role when a function is created. Invoke your function, Lambda automatically provides your function with temporary credentials by assuming this role.

### Lambda Invocation Model
- Synchronous (push)
    API Gateway with Lambda: S3 (static content) --> user --> API Gateway --> Lambda (trigger) --> DynamoDB --> API Gateway --> User (Expects response)
- Asynchronous (event)
    S3 with Lambda: Upload Image to S3 --> Lambda (trigger with eventbridge) --> New resized Image (Does not expects response) 
- Stream (poll-based)
    Kinesis or SQS with Lambda: Kinesis data --> Lambda (polling) --> DynamoDB --> Social Media trend (Scheduled polling or real time)

### Lambda timeout
- Lambda runs code for a set amount of time before timing out.
- When specified timeout reached, Amazon Lambda terminates execution of the Lambda function
- The default value for this setting is 3 seconds
- Maximum value of 900 seconds (15 minutes)
- Performance and cost are two key parameters for setting the Timeout limit
- Edge cases can impact cost
- Pricing depends on the memory/cpu & timeout set for Lambda function