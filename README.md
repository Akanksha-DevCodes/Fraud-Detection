Project Overview

Real-Time Fraud Detection System
Real-Time Fraud Detection System A scalable fraud detection system that processes streaming financial transactions in real time. It uses Apache Kafka and Spark Streaming for data processing, AWS Redshift for storage, and Power BI for visualization. Features include automated alerts, orchestration with Airflow, and compliance with financial security

Tech Stack
Streaming & Processing: Apache Kafka, Spark Streaming
Storage & Database: AWS Redshift
Programming: Python, SQL
Orchestration: Apache Airflow
Visualization: Power BI
Infrastructure: Terraform, Docker

Features
Kafka-based streaming architecture for real-time transaction monitoring  
Spark Streaming for detecting anomalies in transaction patterns  
AWS Redshift for scalable data storage and analytics  
Power BI dashboards for fraud detection visualization  
Airflow for scheduling and automation of fraud monitoring pipelines  
Automated alerts for suspicious transactions  

Installation & Setup

1 Clone the Repository
$ git clone https://github.com/akanksha-dev/fraud-detection.git
$ cd fraud-detection

2 Install Dependencies
$ pip install -r requirements.txt

3 Start Kafka & Spark Streaming
$ docker-compose up

4 Run the Pipeline
$ python data_pipeline/kafka_producer.py  Start transaction streaming
$ python data_pipeline/spark_streaming.py  Detect fraudulent transactions
$ python data_pipeline/redshift_loader.py  Load data into Redshift

5 View the Power BI Dashboard
Open fraud_detection.pbix in Power BI.
Connect to Redshift and visualize fraud analytics.
