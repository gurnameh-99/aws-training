import boto3

# Create a new Athena client
athena = boto3.client('athena')

# Create a new Athena table
response = athena.start_query_execution(
    QueryString='CREATE EXTERNAL TABLE my_table (column1 string, column2 int) LOCATION "s3://my-bucket/my-folder/"',
    ResultConfiguration={
        'OutputLocation': 's3://my-bucket/athena-output/',
        'EncryptionConfiguration': {
            'EncryptionOption': 'SSE_S3'
        }
    }
)

# Wait for the query to complete
query_execution_id = response['QueryExecutionId']
while True:
    status = athena.get_query_execution(QueryExecutionId=query_execution_id)['QueryExecution']['Status']['State']
    if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
        break

# Query the Athena table
response = athena.start_query_execution(
    QueryString='SELECT * FROM my_table',
    ResultConfiguration={
        'OutputLocation': 's3://my-bucket/athena-output/',
        'EncryptionConfiguration': {
            'EncryptionOption': 'SSE_S3'
        }
    }
)

# Wait for the query to complete
query_execution_id = response['QueryExecutionId']
while True:
    status = athena.get_query_execution(QueryExecutionId=query_execution_id)['QueryExecution']['Status']['State']
    if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
        break

# Get the query results
results = athena.get_query_results(QueryExecutionId=query_execution_id)
for row in results['ResultSet']['Rows']:
    print(row)
