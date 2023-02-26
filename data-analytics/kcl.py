from __future__ import print_function
from datetime import datetime
import time
import boto3
import logging
from boto3.dynamodb.conditions import Key, Attr

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Define the Kinesis stream name and the DynamoDB table name
kinesis_stream_name = 'my-kinesis-stream'
dynamodb_table_name = 'my-dynamodb-table'

# Create a Kinesis client
kinesis_client = boto3.client('kinesis')

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodb_table_name)

# Define the Kinesis stream iterator type
iterator_type = 'TRIM_HORIZON'

# Define the number of records to fetch from the Kinesis stream in each iteration
batch_size = 100

# Define the sleep time between each Kinesis stream fetch
sleep_time = 0.5

# Define the KCL process records function
def process_records(records, shard_id):
    for record in records:
        # Process the record data
        logger.info(f"Processing record: {record}")
        # Save the record data to DynamoDB
        table.put_item(Item=record)
        # Sleep for a while to avoid throttling
        time.sleep(sleep_time)

# Define the KCL shutdown function
def shutdown(reason, **kwargs):
    logger.info(f"Shutdown: {reason}")
    return

# Define the KCL main function
def run_kcl(app_name, stream_name):
    try:
        logger.info("Starting KCL...")
        kcl_config = {
            'stream_name': stream_name,
            'region_name': 'us-east-1',
            'record_processor': process_records,
            'shard_id': 'shardId-000000000000',
            'dynamodb': {
                'table_name': dynamodb_table_name,
                'region_name': 'us-east-1'
            },
            'kinesis': {
                'region_name': 'us-east-1'
            }
        }
        worker = kcl.KCLProcess(
            kcl_config,
            app_name,
            record_processor=process_records,
            shutdown_handler=shutdown
        )
        worker.run()
    except Exception as e:
        logger.error(f"Exception in KCL: {e}")

# Run the KCL main function
if __name__ == '__main__':
    run_kcl('my-kcl-app', kinesis_stream_name)
