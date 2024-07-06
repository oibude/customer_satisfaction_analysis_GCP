# customer_satisfaction_analysis_GCP

PROBLEM STATEMENT
As a data engineer at a telecommunication company, your goal is to build a pipeline that extracts network data, transforms it using Google Cloud services,and selects relevant features that the analytics team would use for clustering analysis and machine learning The objective is to categorize customers based on their satisfaction with the network using clustering techniques.

Data Description
The dataset in this case study contains telecommunication network usage data, encompassing
various metrics that reflect customer interactions with the network It includes the following metrics
Key Metrics
•Total data usage (both upload and download)
•Average round trip time (RTT) for data transmission
•Customer identifiers like IMSI, IMEI, MSISDN
•Social media data usage
•Netflix, Google, Email, data usage
•Time of the usage

SERVICES
•Python
•Google Cloud Storage
•Google BigQuery
•Cloud Data Fusion
•Cloud Composer (Apache Airflow)

GOOGLE CLOUD STORAGE
A scalable object storage service to store and retrieve data It is designed for robust, secure,
and highly available storage, enabling users to store any data and retrieve it as needed
The key features are
•Scalability
•Durability
•Security
•Flexibility
•Integration
•Cost effective

DATA PIPELINE
• Extract and Store Data on Google Cloud Storage
• Transform Data using with Data Cloud Fusion
• Load Transformed Data Back into Big Query
• Create a Pipeline in Cloud Data Fusion to Load Data into BigQuery
• Orchestrate Workflow using Cloud Composer

Objectives of the Pipeline
•Efficiently collect and store raw data from local storage into Google Cloud Storage
•Clean, preprocess, and transform the raw data using Python to make it suitable for analysis
•Derive new features from the transformed data, such as total data usage and usage
categories, to enhance the clustering analysis
•Load the transformed data into Google BigQuery for analysis and reporting
•Automate the ETL ( Transform, Load) process using Cloud Data Fusion
•Orchestrate the entire data pipeline workflow using Cloud Composer (Apache Airflow) toensure timely and reliable execution of all tasks

