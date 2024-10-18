## Scalablilty and High Availibility

### Scalability
- Scalability means that an application / system can handle greater loads by adapting
- There are 2 kinds of scalability
    * Vertical Scalability
        - Means increasing the size of an instance
        - For eg: an application run on a t2.micro you upgrade it to t2.large
        - Vertical scalability is very common for non distributed systems such as databases
        - RDS, Elastic Cache are services that can scale vertically
        - There's usually a limit to how much you can scale vertically (hardware limit)
    * Horizontal Scalability (= elasticity)
        - Means increasing the number of instances / systems for the application
        - Horizontal scaling implies distributed systems
        - This is very common for web application / modern application
        - It's easy to horizontally scale thanks to the cloud offerings sach as EC2
- Scalability is linked but different to High Availibility 

### High Availibility
- Usually goes hand in hand with horizontal scaling
- Means running the application / system atleast in 2 data centers (== 2 Avalibility Zones)
- The goal is to survive a data center loss
- It can be passive (for RDS Multi AZ)
- It can be active (for horizontal scaling)


#### For EC2
- Vertical Scaling: Increase instance size (= scale up/down)
- Horizontal Scaling: Increase number of instances (= scale out/in)
    - Auto Scaling Group (ASG)
    - Load Balancer (ELB)
- HA: Run instances for same application across multi AZ
    - ASG multi AZ
    - ELB milti AZ