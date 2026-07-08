def check_duplicates(df):
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        return f"FAIL: {duplicates} duplicate rows found"

    return "PASS: No duplicate rows found"