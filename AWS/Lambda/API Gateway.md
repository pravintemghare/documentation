## API Gateway

Amazon API Gateway is an AWS service for creating, publishing, maintaining, monitoring and securing REST, HTTP, and WebSocket API at any scale.

### Key features of API Gateway

#### Types of API Gateway
- HTTP API
    Build low-latency and cost-effective REST APIs with built-in features such as OIDC and OAuth2 and native CORS support
- Websocket API
    Build a WebSocket API using persistent connections for real-time use cases such as chat applications or dashboards
- REST API
    Develop a REST API when you gain complete control over the request and response along with API management capabilities
- REST API(Private)
    Create a REST API that is only accessible from within a VPC.

#### REST API v/s HTTP API

- REST API supports more features than HTTP API while HTTP API are designed with minimal features and offered at a lower price.
- Choose REST API if you need features like API keys, pre-client throttling, request validation, AWS WAF integration, or private API endpoints.
- Choose HTTP API if you don't need feature included in REST API

#### API Gateway Endpoint Types
- An API endpoint type refers to the hostname of the API
- The API endpoint type can be edge-optimized, regional or private, depending on where the majority of your API traffic originates from

    Edge-optimized: For applications hosted on internet and requests coming from around the globe. CloudFront at the front or API Gateway
    Regional: For application requests coming from a particular region.
    Private: Within the VPC

#### REST API
- Resources: REST Architecture treats every content as a resource. These resources can be Text files, HTML Pages, Images, Videos or Business Data.

- Methods: 
    - GET - Retrive information about the REST API resource
    - POST - Create REST API resource
    - PUT - Update REST API resource
    - DELETE - Delete REST API resource or related component

#### Integration Type
- Lambda Function: Lets you integrate API Gateway with Lambda function
- HTTP: Allows integration with existing HTTP endpoint. This type of integration lets an API expose HTTP endpoints in the backend
- Mock: This type of intergation lets API Gateway retun a response without sending the request further to the backend
- AWS Services: This integration lets an API expose AWS service actions
- VPC Link: A VPC link is a resource in Amazon API Gateway that allows for connecting API routes to private resources inside a VPC

#### Deployment 
- After creating the API, you must deploy it to make it called by the users
- To deploy API, you create an API deployment and associate it with stages
- Everytime you update an API you must redeploy the API to an existing stage or to a new stage
- Updating an API includes modifying routes, methods, integrations, authorizers and anything else other than stage settings

#### Stage
- A logical reference to a lifecycle state of you API (for eg: 'dev', 'prod', 'beta', 'v2')

https://{restapi-id}.execute-api.{region}.amazonaws.com/{stageName}

#### Usage Plan
- Difference between Basic and Premium customers
- Set the target request rate - Throttling, Burst, Quota limit for each API Key

#### API Key
- An alphanumeric string that API Gateway uses to identify an app developer who uses your REST or Websocket API
- You can use API keys together with Lambda authorizers or usage plans to control access to your APIs

#### AWS API Authentication and Authorization
- API security - IAM: Authentication -- IAM, Authorization -- IAM policy. Use case: Internal AWS services, cross account roles
- API security - Cognito: Authentication -- Cognito user pool, Authorization -- API Gateway Methods. Use case: External users from web/mobile apps
- API security - Lambda Authorizer: Authentication -- External, Authorization -- Lambda Function. Use case: Thrid party identity provider such as OAuth 2.0

#### API Integration and Private APIs
- Private APIs: the API endpoint is reachable only through the VPC. Private APIs are accessible only from clients within the VPC or from clients that have network connectivity to the VPC
- Private Integration: An API Gateway integration type for a client to access resources inside a customer's VPC through a private REST API endpoint without exposing the resources to the public internet