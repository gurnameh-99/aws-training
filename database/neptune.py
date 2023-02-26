import boto3

# Initialize the Neptune client
neptune = boto3.client('neptune')

# Create a Neptune cluster
response = neptune.create_db_cluster(
    DBClusterIdentifier='my-neptune-cluster',
    Engine='neptune',
    MasterUsername='admin',
    MasterUserPassword='password'
)

# Print the cluster details
print(response)

# Create a Neptune instance
response = neptune.create_db_instance(
    DBInstanceIdentifier='my-neptune-instance',
    DBInstanceClass='db.r5.large',
    Engine='neptune',
    DBClusterIdentifier='my-neptune-cluster'
)

# Print the instance details
print(response)

# Connect to the Neptune instance using Gremlin
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.traversal import T

# Set the Neptune endpoint and port
endpoint = '<my-neptune-instance>.<region>.neptune.amazonaws.com'
port = 8182

# Connect to the Neptune instance
remote_conn = DriverRemoteConnection(f'wss://{endpoint}:{port}/gremlin', 'g')

# Create a new vertex in the Neptune graph
g = remote_conn.traversal()
vertex = g.addV('person').property('name', 'Alice').property('age', 30).next()

# Print the vertex details
print(vertex)

# Query the Neptune graph using Gremlin
result_set = g.V().hasLabel('person').has('age', T.gt(25)).values('name', 'age').toList()

# Print the query result
print(result_set)

# Delete the Neptune instance and cluster
response = neptune.delete_db_instance(DBInstanceIdentifier='my-neptune-instance')
print(response)

response = neptune.delete_db_cluster(DBClusterIdentifier='my-neptune-cluster')
print(response)
