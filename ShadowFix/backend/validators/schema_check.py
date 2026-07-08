def check_schema(df):
    expected_columns = ["id", "customer_name", "revenue"]

    if list(df.columns) != expected_columns:
        return "FAIL: Schema mismatch"

    return "PASS: Schema valid"