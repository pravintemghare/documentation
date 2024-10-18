## AWS Glue

- Managed extract, transform & load (ETL) service
- Useful to prepare and transform data from analytics
- Fully serverless service
- Convert data to Paraquet format
- Glue Job Bookmarks: prevent re-processing old data
- Glue Elastic Views:
    * Combine and replicate data across multiple data stores using SQL
    * No custom code Glue monitors for changes in the source data, serverless
    * Leverage a 'virtual table' (materialized view)
- Glue DataBrew: clean and normalize data using pre-built transformation
- Glue Studio: new GUI to create, run & monitor ETL jobs in Glue
- Glue Streaming ETL (build on Apache Spark Structured Streaming): compatiable with Kinesis Data streaming, Kafka, MSK(managed kafka)