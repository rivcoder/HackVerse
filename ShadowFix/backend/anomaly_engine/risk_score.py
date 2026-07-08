def calculate_risk(results):
    score = 0

    if "FAIL" in results["null_check"]:
        score += 40

    if "FAIL" in results["duplicate_check"]:
        score += 30

    if "FAIL" in results["schema_check"]:
        score += 50

    return score