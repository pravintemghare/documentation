## Subnets

- AWS reserves 5 IP addresses (first 4 & last 1) in each subnet
- These 5 IP addresses are not available for use and can't be assigned to an EC2 instance.
- Example: If CIDR block 10.0.0.0/24, then reserved IP addresses are:
    - 10.0.0.0 - Network address
    - 10.0.0.1 - reserved by AWS for the VPC router
    - 10.0.0.2 - reserved by AWS for mapping to Amazon-provided DNS
    - 10.0.0.255 - Network Broadcast Address. AWS doen't support boardcast in a VPC therefore this address is reserved.

EG: if you need 29 ipaddress in a subnet:
 - if you select /27 which gets 32 IP's but if we remove the reserved 5 then we are left with 29
 - if you select /26 which get 64 IP's then you will have 29 Ip Addresses.