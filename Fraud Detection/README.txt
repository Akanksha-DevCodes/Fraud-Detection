Real-Time Fraud Detection System

Project Overview
This project builds a real-time fraud detection system that processes streaming financial transactions to identify fraudulent activities. It leverages Apache Kafka and Spark Streaming for real-time data processing, stores transactional data in AWS Redshift, and provides Power BI dashboards for insights.

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

Project Structure

├── data_pipeline
│   ├── kafka_producer.py      Simulates transaction data stream
│   ├── spark_streaming.py     Processes transactions in real time
│   ├── redshift_loader.py     Stores processed data in AWS Redshift
│   └── airflow_dag.py         Orchestrates the workflow
├── dashboards
│   ├── fraud_detection.pbix   Power BI dashboard
├── infrastructure
│   ├── terraform_scripts      Infrastructure as Code Terraform
│   ├── docker_setup           Containerization setup
├── requirements.txt           Dependencies
└── README.md                  Project Documentation

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
- Open fraud_detection.pbix in Power BI.
- Connect to Redshift and visualize fraud analytics.

Contributions & Feedback
Contributions and suggestions are welcome! Feel free to fork the repository, raise issues, and submit pull requests.