import json
import ollama

INPUT_FILE = "results/sampled_methods.json"
OUTPUT_FILE = "results/generated_tests_context.json"

print("Loading sampled methods...")

with open(INPUT_FILE) as f:
    methods = json.load(f)

results = []

for i, m in enumerate(methods[:50]):

    print("Generating test", i+1)

    method_name = m["method_name"]
    
    prompt = f"""
You are a professional Python developer.

Write pytest unit tests for the function '{method_name}'.

The tests should:
- follow pytest format
- include multiple assertions
- include edge cases
- include boundary cases
- simulate realistic developer-written tests
"""

#    prompt = f"""
#Generate pytest unit tests for a Python function named '{method_name}'.

#Requirements:
#- include normal cases
#- include edge cases
#- include assertions
#"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    test_code = response["message"]["content"]

    results.append({
        "method": method_name,
        "generated_test": test_code
    })

print("Generated tests:", len(results))

with open(OUTPUT_FILE, "w") as f:
    json.dump(results, f, indent=2)

print("Saved to:", OUTPUT_FILE)