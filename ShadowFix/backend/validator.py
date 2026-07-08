from google.cloud import bigquery
from save_results import save_results
from validators.null_check import check_nulls
from validators.duplicate_check import check_duplicates
from validators.schema_check import check_schema

from anomaly_engine.risk_score import calculate_risk

client = bigquery.Client()

query = """
SELECT *
FROM `pipelineguardian.pipeline_data.Sales`
"""

df = client.query(query).to_dataframe()

results = {
    "null_check": check_nulls(df),
    "duplicate_check": check_duplicates(df),
    "schema_check": check_schema(df)
}


risk_score = calculate_risk(results)

print(results)
print("Risk Score:", risk_score)

save_results(results, risk_score)