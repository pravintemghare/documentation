## Network proctection in AWS

- To protect network on AWS we have:
    - NACL
    - SG
    - WAF (protect against malicious requests)
    - Shield & Shield Advance
    - Firewall Manager (to manage them accross accounts)

#### AWS Network Firewall
- Protect your entire VPC
- From layer 3 to layer 7
- Any direction you can inspect
    - VPC to VPC traffic
    - Outbound to internet
    - Inbound from internet
    - To/from Direct Connect & S2S VPN
- Internally the AWS Network Firewall uses the AWS GW LB
- Rules can be centrally managed cross-account by AWS Firewall Manager to apply to many VPC
- Fine Grained Controls
    - Supports 1000 of rules
        - IP & port - eg: 10,000 of IP filtering
        - Protocol - example: block the SMB protocol for outbound communications
        - Stateful domain list rule groups. only allow out bound traffic to *.mycorp.com or third-party software repo
        - General pattern matching using regex
    - Traffic filtering: Allow drop or alert for the traffic that matches the rules
    - Active flow inspection to protect against network threats with intrusion-prevention capabilities (GWLB but all managed by AWS)
    - Send Logs of rules matches to Amazon S3, CW logs, Kinesis Data Firehose