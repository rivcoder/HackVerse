import json

with open("results.json", "r") as f:
    data = json.load(f)

print("\nPIPELINE HEALTH REPORT")
print("=" * 30)

for check, result in data["results"].items():
    print(f"{check}: {result}")

print("\nRisk Score:", data["risk_score"])