## Records

- How to route traffice for a domain
- Each records contain:
    * Domain/Subdomain Name: eg.example.com
    * Record Type: A or AAAA or CNAME
    * Value: 1.2.3.4
    * Routing Policy: how route53 responds to queries
    * TTL: amount of time the record cached at DNS resolvers
- It supports the following DNS record types:
    * A / AAAA / CNAME / NS
    * CAA / DS / MX / NAPTR / PTR / SOA / TXT / SPF / SRV


#### Record Types:

1. A: maps hosts name to IPv4
2. AAAA: maps hostname to IPv6
3. CNAME: maps a hostname to another hostname
    * The target is a domain name which must have an A or AAAA record
    * Can't create CNAME records for the top node of a DNS namespace (Zone Apex)
    * EG: can't create for example.com, but can create for www.example.com
4. NS: Name Server for the Hosted Zone


##### TTL (Time To Live)
- High TTL - eg: 24 hrs
    - Less traffic on Route53
    - Possibly outdated records
- Low TTL - eg: 60 sec
    - More traffic on Route53 ($$)
    - Records are outdated for less time
    - Easy to change records
- Except for Alias records, TTL is mandatory for each DNS record

##### CNAME & Alias
- AWS Resources (ELB, CloudFront) expose an AWS hostname
- CNAME: Points a hostname to any other hostname (appname.mydomain.com) to (somthing.anything.com). This only for non-root domains
- Alias: Points a hostname to an AWS resource (app.domainname.com) to (omthing.anything.com). This works for both root & non-root domains. Free of chaarge