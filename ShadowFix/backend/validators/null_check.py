def check_nulls(df):
    null_count = df.isnull().sum().sum()

    if null_count > 0:
        return f"FAIL: {null_count} null values found"

    return "PASS: No null values found"