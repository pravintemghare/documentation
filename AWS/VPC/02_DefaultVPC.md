## Default VPC in AWS account

1. All new AWS accounts have a default VPC
2. New EC2 instances are launched into the default VPC if no subnet is specified
3. Default VPC has Internet connectivity and all EC2 instances inside it have public IPv4 addresses
4. The default VPC has 3 subnet deployed in 3 different availibility zones


You can have upto 5 VPC's per region (soft limit - can be increased)
Max CIDR per VPC is 5 for each CIDR
 - Min. size is /28 (16 IP)
 - Max. size is /16 (65536 IP)

Because VPC is private, only the Private IPv4 ranges are allowed
 - 10.0.0.0/8 
 - 172.16.0.0/12
 - 192.168.0.0/16

Your VPC CIDR should not overlap with your other networks (eg: intranet)