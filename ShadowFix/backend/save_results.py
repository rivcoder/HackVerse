import json

def save_results(results, risk_score):
    data = {
        "results": results,
        "risk_score": risk_score
    }

    with open("results.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Results saved")