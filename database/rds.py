import psycopg2

# Set the connection parameters
host = '<RDS endpoint>'
port = '<RDS port>'
database = '<database name>'
username = '<database username>'
password = '<database password>'

# Connect to the database
conn = psycopg2.connect(
    host=host,
    port=port,
    dbname=database,
    user=username,
    password=password
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a sample SQL query
cur.execute('SELECT version()')

# Fetch the query result
db_version = cur.fetchone()[0]

# Print the result
print(f'Database version: {db_version}')

# Close the cursor and connection
cur.close()
conn.close()
