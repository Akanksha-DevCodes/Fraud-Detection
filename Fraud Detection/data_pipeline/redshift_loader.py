import psycopg2
from datetime import datetime

# Redshift connection parameters
host = "your-redshift-cluster-name"
dbname = "yourdbname"
user = "yourusername"
password = "yourpassword"
port = "5439"

# Connect to Redshift
conn = psycopg2.connect(
    dbname=dbname, user=user, password=password, host=host, port=port
)
cursor = conn.cursor()

# Function to load data to Redshift
def load_to_redshift(transaction_data):
    insert_query = """
    INSERT INTO transactions (transaction_id, amount, type, timestamp)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (transaction_data['transaction_id'], transaction_data['amount'], transaction_data['type'], transaction_data['timestamp']))
    conn.commit()

# Example function call (you'd adapt to your actual use case)
transaction_data = {
    'transaction_id': 1234,
    'amount': 500.50,
    'type': 'debit',
    'timestamp': datetime.now()
}

load_to_redshift(transaction_data)