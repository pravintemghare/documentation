## Lambda Advance topics

### AWS Lambda Concurrency, Reserved Concurrency and Provisioned Concurrency

#### AWS Lambda Function Execution and Cold Start:

Manny Accounts:
    - Hardware
    - Host OS

One Accounts:
    - Hypervisor
    - Guest OS

One Function:
    - Sandbox
    - Lambda Runtime
    - Code

AWS Optimization
    Full cold start
        - Download your code
        - Start new micro vm

Your Optimization
    Partial cold start
        - Bootstrap the runtime
    Warm start
        - start the code

- Lambda Concurrency
    - Concurrency is the number of inflight requests the Lambda function is handling at the same time.
    - For each concurrent request, Lambda provisions a seperate instance of the execution environment.
    - As the function receives more requests, Lambda automatically handles scaling the number of exections environments until account's concurrency limit.
    - By default, Lambda provides account with a total concurrency limit of 1000 across all functions in a region.

- Lambda Concurreny Calculation
    - Concurrency = (average requests per second) * (average request duration in seconds)
    - If the average request duration is 500ms, the concurrency is:
    - Concurrency = (100 requests/second) * (0.5 seconds/request) = 50
    - Concurrency Implications: 
    - A concurrency of 50 means that Lambda must provision 50 executions environment instances to efficiently handle this workload without any throttling.

- Lambda Provisioned Concurrency
    - Set number of pre-provisioned execution environment instances for your function
    - Use provisioned concurrency to pre-initilize a number of environment instances for a function. This is useful for reducing cold start latencies

- Lambda Reserved Concurrency
    - Maximum number of execution environment instance for a particular function
    - Use reserved concurrency to reserve a portion of your account's concurrency for a function. This is useful if you don't want other functions taking up all the available unreserved concurrency.

### AWS Lambda Memory - Limits
    - Lambda allocates CPU power in proportion to the amount of memory configured.
    - Default Memory - 128 MB
    - Maximum Memory - 10,240 MB, in 1-MB increments
    - At 1769 MB, a function has the equivalent of one vCPU.
    - More memory = more CPU
    - Lambda pricing - Number of invocations * Memory allocated * Execution Time
    - One-thounsandth of a cent cost difference, the function has a 10-fold improvement in performance
    - Chosing the memory allocated to lambda function is an optimization process that balances speed(duration) and cost.
    - AWS Lambda Power Tuning tools allows to automate the process.

    * Best Practice:
        - Derive the balance between Function Timeout and Memory allocation (think about the edge cases)
        - Over-Provision in Memory, if required but Not Function Timeout.

#### AWS Lambda Deployment options
    - Default deployment:
        * All lambda functions run securely inside a default system-managed virtual private cloud(VPC)
        * Not in customer VPC
        * Has access to all the services that can be accessed on Internet - S3, DynamoDB, etc..
    
    - VPC deployment
        * Lambda need the IAM permission required to create and delete network interface in your VPC - AWSLambdaVPCAccessExecutionRole
        * Control the subnet and security group configuration of these network interface
        * Use NAT device to give function internet access or use VPC endpoints to connect to services outside of the VPC

#### AWS Lambda with CloudWatch
- Lambda Service automatically monitors functions and sends Metrics and Logs to CloudWatch
- On processing an event, Lambda sends metrics about the invocation to CloudWatch and generate logs
- Graphs and dashboards can be built with these metrics on the CloudWatch console
- Set alarm to respond to changes, in utilization, performance or error rates
- Lambda sends metrics data to CloudWatch in 1 minutes internvals (min) 
- Lambda CloudWatch metrics:
    * Invocations: The number of times that your function code invoked. including successful invocations and incotvation that result in a function error
    * Duration: The amount of time that your function code spends processing an event
    * Errors: This logs the number of errors thrown by a function
    * Throttle: Set alarm on this metric for any non-zero value since this occurs if the number of invocations exceeds concurrency in your avvount
    * Concurrent Execution: Monitor this value to ensure that your function are not runnig close to the total concurrency limit of you AWS account
    * UnreservedConcurrentExpression: Similar to previous metric but excludes functions using reserved concurrency
    * DeadLetterErrors: An error is triggered if Lambda cannot write to the designed dead-letter queue, set alarm on any non-zero values for this metric
    * IteratorAge: For Lambda functions that poll streaming sources, such as Kenisis or DynamoDB streams, the value indicates when envents are being produced faster than they are being consumed by Lambda.