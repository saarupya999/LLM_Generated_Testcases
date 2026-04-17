
import json
import re

INPUT_FILE = "results/generated_tests_advanced.json"

with open(INPUT_FILE) as f:
    tests = json.load(f)

total_tests = len(tests)
total_assertions = 0
edge_cases = 0

for t in tests:
    code = t["generated_test"]

    # count assertions (same logic everywhere)
    assertions = re.findall(r"assert ", code)
    total_assertions += len(assertions)

    # simple edge case detection
    if any(k in code.lower() for k in ["none", "0", "negative", "[]", "-1", "large"]):
        edge_cases += 1

# calculate average
avg_assertions = total_assertions / total_tests

# print results
print("Total generated tests:", total_tests)
print("Total assertions:", total_assertions)
print("Average assertions per test:", round(avg_assertions, 2))
print("Edge case tests:", edge_cases)

# save for dashboard (FIXED VARIABLE NAME)
results = {
    "total_tests": total_tests,
    "total_assertions": total_assertions,
    "avg_assertions": avg_assertions,
    "edge_cases": edge_cases
}

with open("results/evaluation_summary.json", "w") as f:
    json.dump(results, f, indent=2)

