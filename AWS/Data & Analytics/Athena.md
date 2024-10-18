## AWS Athena

- Serverless query service to analyze data stored in Amazon S3
- Uses standard SQL Language to query the files(built on Presto)
- Support JSON, CSV, ORC, Avro, and Parquet
- Pricing 5$ per TB data scanned
- Commonly used with Amazon Quicksight for reporting/dashboards

* Uscase: Business intelligence / analytics / reporting, analyze, and query VPC Flow Logs, ELB Logs, CloudTrail trails, etc..

- Performance Improvement
    * Use columnar data for cost-savings(less scan)
        * Apache Parquet or ORC is recommended
        * Huge performance improvement
        * Use Glue to convert your data to Paraquet or ORC
    * Compress data for smaller retrivels (bzip2, gzip, lz4, snappy, zlip, zstd..)
    * Partition datasets in S3 for easy quering on virtual columns 
        - EG: s3://athena-example/flights/paraquet/year=2000/motth=1/day=1/
    * Use larger files (> 128 MB) to minimize overhead

- Federated Query
    * Allows you to run SQL queries across data stored in relational, non-relational object, and custom data source (AWS or On-prem)
    * Uses Data Source Connectors that run on AWS Lambda to run Federated Queries (CloudWatch Logs, DynamoDB, RDS...)
    * Store the results back in Amazon S3