## Route53 Routing Policies

- Define how Route53 responds to DNS queries
- Don't get confused by the work 'Routing'
    - It's not the same as Load Balancer which routes traffic 
    - DNS does not route any traffic, it only responds to the DNS queries

##### Health Checks
- HTTP Health checks are for public resources only
- Health Check => Automated DNS Failover
    * Health checks that monitor an endpoint (application, server)
    * Health checks that monitor other health checks (calculated health checks)
    * Health checks that monitor CloudWatch Alarms (full control)
- Health Checks are integrated with CW metrics
- Types of Health Checks:
    1. Monitor an Endpoint
        * About 15 global health checkers will check the endpoint health
            - Health/Unhealthy Thereshold - 3 (default)
            - Interval - 30 secs (can set to 10 secs - higher cost)
            - Supports Protocol HTTP, HTTPS & TCP
            - If > 18% of heath checks reports the endpoint is healthy, Route53 considers it healthy otherwise unhealthy
            - Ability to choose which locations you want Route53 to use
        * Health checks pass only when the endpoint responds with 2xx or 3xx status code.
        * Healtch checks can be setup to pass/fail based on the text in the first 5120 bytes of the response
        * Configure your router/firewall to allow incoming requests from Route53 health checkers
    2. Calculated Health checks
        * Combine the results of multiple Health Checks into a single Health Check
        * You can use OR, AND and NOT
        * Can monitor up to 256 Child Health Checks
        * Specify how many of the health checks need to pass to make the parent pass
        * Usage: perform maintenacne to your website without causing all health checks to fail
- Private Hosted Zone
    * Route53 health checker are outside of the VPC 
    * They can't access private endpoints (private VPC or on-prem resources)
    * You can create a CloudWatch Metric and associate a CloudWatch Alarm, then create a Health Check that checks the alarm itself

#### Simple Routing Policy
- Typically route traffic to a single resource
- Can specify multiple values in the same record
- If multiple values are returned a random one is chosen by the client
- When Alias enabled, specify only one AWS resource
- Can't be associated with Heath Checks

#### Weighted Routing Policy
- Control the % of the request that go to each specific resource
- Assign each record a relative weight
    - traffic % = Weight for a specific record / Sum  of all the weights for all records
    - Weight doen't need to sum up to 100
- DNS record must have the same name & type
- Can be associated with health checks
- Use case: load balancing between regions, testing new application version
- Assign weight of 0 to a record to stop sending traffic to a resource
- If all records have weight of 0 then, all records will be returned equally 

#### Latency Routing Policy
- Redirect to the resource that has the least latency close to the user.
- Super helpful when latency for users is priority
- Latency is based on traffic between users ans AWS Regions
- Can be associated with Health checks (has failover capibility)

#### Failover Routing Policy (active-passive)
- Can be used to monitor AWS resources for failover
- If one resource fails the Route53 requests are moved to the the other resource

#### Geoloaction Routing Policy
- Different from latency-based
- This routing is based on user location
- Specify location by Continent, Country or by US state (if there's overlaping, most precise location is seleted)
- Should create a "Default" record (in case the location not match)
- Use case: website localization, restrict content distrubution, load balancing
- Can be associated with Health Checks

#### Geoproximity Routing Policy
- Route traffic to your resources based on the geographic location of users and the AWS resources
- Ability to shift more traffic to resources based on the defined bias
- To change the size of the geographic region, specify bias value:
    * To expand (1 to 99) - more traffic to the resource
    * To shrik (-1 to -99 ) - less traffic to the resource
- Resource can be:
    * AWS resources (specify AWS region)
    * Non-AWS resources (specify Latitude and Longitude)
- Must use Route53 Traffic flow (advanced) to use this feature

#### IP-based Routing Policy
- Routing is based on client's IP Address
- Provide a list of CIDR's for your clients and the corresponding endpoints/locations (user-IP-to-endpoint mappings)
- Use case: Optimize performance, reduce network costs
- Example: route end users from a particular ISP to a specific endpoint

#### Multi-Value Routing Policy
- Use when routing traffic to multiple resources
- Route53 return multiple values/resources
- Can be associated with Health Checks (return only values of healthy resources)
- Up to 8 healthy records are returned for each Multi-Value query
- Multi-Value is not a substitute for having a ELB