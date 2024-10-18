#### CIDR - Classless Inter Domain Routing 

Method for allocating IP Address
Used in Security Groups rules and AWS networking in general


/32 - one IP
/0 - all IP

192.168.0.0 - 192.168.0.255 /24

Bas IP - 192.168.0.1
Subnet Mask 255.255.255.0 --- /0 , /16, /24 , /32

Octets of IP Address

___.___.___.___

/32 - No octets changes
/24 - Last octets changes
/19 - Last 2 octets changes
/8  - Last 3 octets changes
/0  - All octets changes

##### Public and Private IP Address (IPv4)

The Internet Assigned Number Authority (IANA) established centain blocks of IPv4 addresses for the use of private (LAN) and public (Internet) addresses

Private IP can onle allow certain values:
10.0.0.0/8 -- for bigger networks
172.16.0.0/12 -- AWS default VPC in that range
172.16.0.0/16 -- for 
192.168.0.0/24 -- for smaller networks

127.0.0.1 - loop back ip address