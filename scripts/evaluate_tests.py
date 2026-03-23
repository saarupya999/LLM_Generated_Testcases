import json
import re

INPUT_FILE = "results/generated_tests_context.json"

with open(INPUT_FILE) as f:
    tests = json.load(f)

total_tests = len(tests)
total_assertions = 0
edge_cases = 0

for t in tests:
    code = t["generated_test"]

    # count assertions
    assertions = re.findall(r"assert ", code)
    total_assertions += len(assertions)

    # simple edge case detection
    if "None" in code or "0" in code or "negative" in code:
        edge_cases += 1

print("Total generated tests:", total_tests)
print("Total assertions:", total_assertions)
print("Average assertions per test:", total_assertions / total_tests)
print("Edge case tests:", edge_cases)