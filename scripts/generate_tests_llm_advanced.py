
import json
import ollama

# INPUT / OUTPUT FILES
INPUT_FILE = "results/sampled_methods.json"
OUTPUT_FILE = "results/generated_tests_advanced.json"

print("Loading sampled methods...")

with open(INPUT_FILE) as f:
    methods = json.load(f)

results = []

# EDGE CASE GENERATOR (based on method name)
def get_edge_cases(method_name):
    method_name = method_name.lower()

    if "add" in method_name or "sum" in method_name:
        return ["0,0", "-1,-2", "1000000,1000000"]
    elif "divide" in method_name:
        return ["1,0", "0,5", "-10,2"]
    elif "list" in method_name:
        return ["[]", "[1]", "[None]"]
    elif "string" in method_name or "str" in method_name:
        return ["''", "'a'", "'longstring'*100"]
    else:
        return ["None", "0"]

# LOOP THROUGH METHODS
TOTAL = 100   # you can increase later (100 recommended)

for i, m in enumerate(methods[:TOTAL]):

    method_name = m.get("method_name", "unknown_function")
    method_code = m.get("method_code", "")

    edge_cases = get_edge_cases(method_name)

    # BUILD ADVANCED PROMPT
    prompt = f"""
You are a professional Python developer.

{"Here is the function:\n" + method_code if method_code else f"Function name: {method_name}"}

Generate pytest unit tests.

Requirements:
- Include normal test cases
- Include edge cases:
  - zero values
  - negative values
  - empty inputs
  - invalid inputs
  - boundary conditions
  - large inputs
- Also include these specific edge cases: {edge_cases}
- Use multiple assertions
- Use pytest.mark.parametrize where possible
- Create multiple test functions (not just one)

STRICT RULES:
- Output ONLY valid Python pytest code
- Do NOT include explanations outside code
- Add explanation ONLY as comments (#) inside tests
- Each test function must include at least 2 assertions
"""

    print(f"Generating test {i+1}/{TOTAL}...")

    try:
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        test_code = response["message"]["content"]

        results.append({
            "method_name": method_name,
            "generated_test": test_code
        })

    except Exception as e:
        print(f"Error generating test {i+1}:", e)

# SAVE OUTPUT
with open(OUTPUT_FILE, "w") as f:
    json.dump(results, f, indent=2)

print("\n✅ Generation Complete")
print("Generated tests:", len(results))
print("Saved to:", OUTPUT_FILE)
