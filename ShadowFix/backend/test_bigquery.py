from google.cloud import bigquery

client = bigquery.Client()

query = """
SELECT *
FROM `pipelineguardian.pipeline_data.Sales`
"""

rows = client.query(query)

for row in rows:
    print(row)