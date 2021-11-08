from google.cloud import bigquery
import os

credentials_path = 'C:/Users/Janna/OneDrive - DePaul University/Janna/Fall 2021/MSDS 498/GitHub/Continuous-Delivery-of-Flask-Data-Engineering-API-1/pythonbq.privateKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id='omega-research-328704.HDPE.HDPE_PREDICTION'

query = """
    SELECT CAST(Month AS DATE) AS Month, ROUND(Predicted_value, 3) AS Predicted_value 
    FROM `omega-research-328704.HDPE.HDPE_PREDICTION` 
"""
query_job = client.query(query)

for row in query_job:
    print("Month = {}, Predicted HDPE Value = {}".format(row["Month"],row["Predicted_value"]))