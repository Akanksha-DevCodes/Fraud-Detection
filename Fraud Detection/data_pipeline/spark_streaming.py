from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Initialize Spark session
spark = SparkSession.builder \
    .appName("FraudDetection") \
    .getOrCreate()

# Read streaming data from Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions_topic") \
    .load()

# Define schema and process data
transactions = df.selectExpr("CAST(value AS STRING)") \
    .select(expr("json_tuple(value, 'transaction_id', 'amount', 'type', 'timestamp')").alias("transaction_id", "amount", "type", "timestamp"))

# Anomaly detection logic (example: flagging large transactions)
def detect_anomalies(transaction):
    if float(transaction['amount']) > 400:
        return True
    return False

# Output: Write results to console (real-time fraud detection)
query = transactions.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
