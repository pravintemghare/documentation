## AWS VPC Components

#### Internet Gateway
- Allows resources (EC2) in a VPC connect to the internet
- It scales horizontally and is highly available and redundant
- Must be created seperately from VPC
- One VPC can only be attached to one IGW, vice versa
- IGW on their own do not allow Internet Access. Must edit the Route tables

#### NAT Instances (Network Address Translation)
- Out dated instead use NAT Gateway
- Allows resources (EC2) in private subnet to connect to the internet 
- Must be launched in a public subnet
- Must disable EC2 setting: Source/Destination Check
- Must have Elastic IP attached to it
- Route tables must be configured to route traffic from private subnets to NAT instances

###### Limitations
- Pre-configured Amazon Linux AMI's available. Reached end of standard support on Dec 2020.
- Not highly available/resilient setup out of the box. You need to create an ASG in multi-AZ + resilient user-data script
- Internet traffic bandwidth depends on EC2 instance type
- You must manage security groups and rules

#### NAT Gateway
- AWS Managed NAT, higher bandwidth, high availibility, no administration
- Pay per hour of usage and bandwidth
- NAT GW is created in a specific AZ, uses Elastic IP
- Can't be used by EC2 instance in the same subnet (only from other subnets)
- Requires an IGW (Private Subnet --> NAT GW --> IGW)
- 5Gbps of bandwidth with automatic scaling upto 100Gbps
- No security groups to manage / required
- NAT GW High availibility:
    - NAT GW is resilient within a single AZ
    - Must create multiple NAT GW in multiple AZ for fault-tollerance
    - There is no cross-AZ failover needed because if an AZ goes down it doesn't need NAT

#### Security Groups (SG) & Network Access Control List (NACL)
- NACL
 - NACL are like firewall which controls traffic from and to subnets
 - One NACL per subnet, new subnet are assigned the Default NACL 
 - You define NACL rules:
    - Rules have a number (1-32766) higher precedence with a lower number
    - First rule match will drive the decission
    - The last rule is asterisk (*) and denies a request in case of no rule match
    - AWS recommends adding rules by increment of 100
    - Newly created NACL will deny everything
- Default NACL allows all traffic in & out
- Do Not modify the default NACL instead create a new one.
 
##### Ephemeral Ports
- For any two endpoints to establish a connection, they must use ports
- Clients connect to a defined port, and expect a response on a ephemeral port
- Different operating systems use different port ranges, eg:
    - IANA & Windows 10 --> 49152 - 65535
    - Linux --> 32768 - 60999

##### Differenct between SG & NACL
1. Operates at the instance level                       || 1. Operates at Subnet leve
2. Supports allow rules only                            || 2. Supports allow rules and deny rules
3. Stateful: return traffic is automatically allowed,   || 3. Stateless: return traffic must be explicitly allowed by
   regardless of any rules.                             ||    rules (think of ephemeral ports)    
4. All rules are evaulated before deciding whether to   || 4. Rules are evaluated in order (lowest to highest) when
   allow traffic                                        ||    deciding whether to allow traffic, first match wins
5. Applies to an EC2 instance when specified by someone || 5. Automatically applies to all EC2 instances in the subnet that it's
                                                        ||    associated with


#### VPC Peering
- Privately connect two VPC's using AWS network
- Make them behave as if they were in the same network
- Must not have overlapping CIDR
- VPC peering connections is NOT transitive (must be established for each VPC that needs to communicate with one another)
- Must update route tables in each VPC's subnets to ensure EC2 instances can communicate with each other
- Can create VPC peering connection between VPC's in different AWS accounts/region
- Can reference a security group in a peered VPC (works cross accounts - same region)


#### VPC Endpoints (AWS Private Links)
- Every AWS service is publically exposed (public URL)
- VPC Endpoints (powered by PrivateLink) allows you to connect to AWS services using a private network instead of using the public internet.
- They are redundant and scale horizontally
- They remove the need og IGW NATGW to access AWS service
- In case of issues:
    - Check DNS Settings Resolution in your VPC
    - Check Route Tables
- Types of VPC Endpoints
    1. Interface Endpoints (powered by PrivateLink)
        - Provisions an ENI (private IP Address) as an entry point (must attach a SG)
        - Supports most AWS services
        - $ per hour + $ per GB data processed
    2. Gateway Endpoints
        - Provisions a gateway and must be used a traget in a route table (does not use security group)
        - Supports both S3 and DynamoDB
        - Free
- Gateway or Interface Endpoint for S3?
 1. Gateway is most likely going to be prefered all the time at the exam.
 2. Cost: free for Gateway, $ for interface endpoint
 3. Interface Endpoint is prefered access is required on-premises (Site-to-Site VPN or Direct Connect), a different VPC or a different region

#### VPC Flow Logs
- Captures information about IP traffic going into the interfaces:
    - VPC Flow Logs
    - Subnet Flow Logs
    - Elastic Network Interface (ENI) Flow Logs
- Helps to monitor & troubleshoot connectivity issues
- Flow logs data can go to S3, CloudWatch Logs, and Kinesis Data Firehose
- Capture network information from AWS managed interfaces too: ELB, RDS, ElasticCache, Redshift, WorkSpace, NATGW, Transit GW.
- Meta data for VPC Flow Logs:
    Version, Account-Id, Interface-Id, SrcAddr, DstAddr, Srcport, Dstport, Protocol, Packets, Bytes, Start, End, Action, Log-Status
- VPC Flow Logs Architecture
    --> VPC Flow Logs -- CloudWatch Logs -- CloudWatch Contributor Insights
    --> VPC Flow Logs -- CloudWatch Logs -- CW Alarm -- SNS Topic
    --> VPC Flow Logs -- S3 Bucket -- Amazon Athena -- Amazon QuickSight

#### AWS Site-to-Site VPN
- Two most important things in S2S VPN
    1. Virtual Private Gateway (VGW)
        - VPN concentrator on the AWS side of the VPN connection
        - VGW is created and attached to the VPC from which we want to create the S2S VPN connection
        - Possibility to customize the ASN (Autonomous System Number)
    2. Customer Gateway (CGW)
        - Software application or physical device on customer side of the VPN connection
- CGW device (on-prem)
    - What IP address to use?
        - Public Internet-routable IP from your CGW device
        - If it's behind a NAT device that enabled for NAT traversal (NAT-T) use the public-IP of the NAT device
* Enable Route Propagation for the VGW in the route table that is associated with your subnets
- If you need to ping EC2 instance from on-prem, make sure you add ICMP protocol on the inbound of your SG

##### AWS VPN CloudHub
- Provide secure communication between multiple sites, of you have multiple VPN connections
- Low-cost hub-and-spoke model for primary or secondary network connectivity between different locations (VPN only)
- Its a VPN connection so it goes over the public Internet.
- To set up, connect multiple VPN connection on the same VGW, setup dynamic routing and congfigure route table

#### Direct Connect (DX)
- Provides a dedicated private connection from a remote network to the VPC
- Dedicated connection must be setup between the DC and AWS DX locations
- Need to setup a VGW on the VPC
- Access public resources S3 and private EC2 on same connection
- Use case:
    - Increase bandwidth throughtput - working with large data sets - lower cost
    - More consistent network experience - applications using real-time data feeds
    - Hybrid Environments (on-prem + cloud)
- Connectivity setup: Customer router/firewall --> Customer or partner router --> AWS DX Endpoint --> VGW using Private Virtual Interface 
- Want to setup a DX to one or more VPC in many different regions(same account), must use a direct connect gateway. 
- Types of Direct Connect:
    1. Dedicated Connections: 1, 10, 100 Gbps capacity
        - Physical Ethernet Port dedicated to a customer
        - Reqeust made to AWS then completed by AWS DX Partner
    2. Hosted Connections: 50, 500 Mbps to 10 Gbps
        - Connections requests are made via AWS DX Partner
        - Capacity can be added or removed on demand
        - 1,2,5,10 Gbps available at select AWS DX Partners
    Lead time are often longer than 1 month to establish a new connection
- DX - Encryption
    - Data in tansit is not encrypted but is private
    - AWS DX + VPN provides an IPsec-encrypted private connection
    - Good for an extra level of security but slightly more complex to put in place 
- DX - Resiliency
    - High Resiliency for critical workloads: 2DC -- 2 AWS DX locations with 1 DX -- VPC
    - Maximum Resilency for crirical workload: 2DC -- 2 AWS DX locations with 2 DX -- VPC
- In case DX fails, you can set up a backup DX connection (expensive) or a S2S VPN connection

#### VPC Transit Gateway
- For having transitive peering between thousands of VPC and on-prem, hub-spoke(star) connection
- Regional resouce, can work cross-region
- Share cross-account using Resource Access Manager (RAM)
- You can peer TG accross regions
- Route Tables: limit which VPC can talk with other VPC
- Works with DX GW & VPN Connection
- Supports IP Multicast (not supported by any other AWS service)
- S2S VPN ECMP (Equal Cost Multi-path Routing)
    - Routing stategy to allow to forward a packet over multiple best path
    - Use case: create multiple S2S VPN connections to increase the bandwidth of connections to AWS
- TG shares Direct Connection between multiple accounts

#### VPC Traffic Mirroring
- Allows you to capture and inspect network traffic in you VPC
- Route the traffic to security appliances that you manage
- Capture traffic
    - From (source) - ENI
    - To (destination) - ENI or NLB
- Capture all packets or capture the packets of your interest (optionally,truncate packets)
- Source and Target can be in the same VPC or different VPCs (VPC Peering)
- Use cases: content inspection, threat monitoring, troubleshooting

#### IPv6 for VPC
- IPv4 addresses to provide 4.3 Billion addresses (they are going to be exhausted soon)
- IPv6 successor of IPv4
- IPv6 is designed to provide 3.4 x 10(38) unique IP addresses
- Every IPv6 IP address in AWS is public and internet-routable (no private)
- Format x.x.x.x.x.x.x.x (x is hexadecimal, range can be from 0000 to ffff)
- IPv4 cannot be disabled in VPC and subnets
- Can enable IPv6 (they are public IP) to operate in dual-stack mode
- An EC2 will get at least a private internal IPv4 and a Public IPv6 
- They communicate using either IPv4 or IPv6 to the internet through an IG

#### Egress-Only IG
- Used for IPv6 only (similar to NAT GW but for IPv6)
- Allows instances in your VPC outbound connections over IPv6 while preventing the internet to initiate an IPv6 connection to your instance
- Must update the route tables