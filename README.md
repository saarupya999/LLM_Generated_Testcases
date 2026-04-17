# 🧪 LLM-Based Automatic Unit Test Generation Using Focal-Method Datasets

---

## 📌 Overview

This project explores how Large Language Models (LLMs) can automatically generate **unit tests for Python functions** using a focal-method dataset.

We:

* Extract methods from a dataset
* Generate tests using different prompts
* Evaluate quality using metrics
* Analyze limitations of LLM outputs
* Visualize results using a dashboard

---

## 🎯 Objectives

* Automate unit test generation using LLMs
* Compare prompting strategies (Baseline, Context, Advanced)
* Evaluate generated tests (assertions, edge cases, validity)
* Identify limitations of LLM-generated tests

---

## 🧱 Project Workflow (IMPORTANT)

```text
Dataset
  ↓
Extract Methods
  ↓
Sample Methods
  ↓
Generate Tests (Baseline / Context / Advanced)
  ↓
Evaluate Tests
  ↓
Failure Analysis
  ↓
Dashboard Visualization
```

---

## 🔁 Execution Flow (STEP-BY-STEP)

```text
1. extract_methods.py
        ↓
2. sample_methods.py
        ↓
3. generate_tests_llm.py
        ↓
4. generate_tests_llm_advanced.py
        ↓
5. evaluate_tests.py
        ↓
6. failure_analysis.py
        ↓
7. dashboard_streamlit.py
```

---

## 🗂️ Project Structure

```text
LLM_Test_Generator_Project/
│
├── pymethods2test/data/       # Dataset
│
├── scripts/
│   ├── extract_methods.py
│   ├── sample_methods.py
│   ├── generate_tests_llm.py
│   ├── generate_tests_llm_advanced.py
│   ├── evaluate_tests.py
│   ├── failure_analysis.py
│   ├── dashboard_streamlit.py
│
├── results/
│   ├── sampled_methods.json
│   ├── generated_tests.json
│   ├── generated_tests_advanced.json
│   ├── evaluation_summary.json
│
└── README.md
```

---

## ⚙️ Setup

### 1. Install dependencies

```bash
pip install ollama streamlit
```

---

### 2. Run LLM (Llama3)

```bash
ollama run llama3
```

---

## 🚀 How to Run the Project

### 🔹 Step 1: Extract methods

```bash
python3 scripts/extract_methods.py
```

---

### 🔹 Step 2: Sample methods

```bash
python3 scripts/sample_methods.py
```

---

### 🔹 Step 3: Generate tests (baseline)

```bash
python3 scripts/generate_tests_llm.py
```

---

### 🔹 Step 4: Generate tests (advanced)

```bash
python3 scripts/generate_tests_llm_advanced.py
```

---

### 🔹 Step 5: Evaluate tests

```bash
python3 scripts/evaluate_tests.py
```

Output:

```text
Total tests: 50
Total assertions: 457
Average assertions: 9.14
Edge cases: 50
```

---

### 🔹 Step 6: Failure analysis

```bash
python3 scripts/failure_analysis.py
```

---

### 🔹 Step 7: Run dashboard

```bash
streamlit run scripts/dashboard_streamlit.py
```

Open in browser:

```text
http://localhost:8501
```

---

## 🧠 Prompt Strategies

### 🔹 Baseline

* Uses only method name
* Generates simple tests

### 🔹 Context

* Adds structured instructions
* More realistic tests

### 🔹 Advanced

* Includes edge cases
* Multiple assertions
* Parameterized tests
* Explanations in comments

---

## 📊 Evaluation Metrics

* Total assertions
* Average assertions per test
* Edge case coverage
* Valid vs invalid tests

---

## 📉 Results

| Metric              | Value |
| ------------------- | ----- |
| Total Tests         | 50    |
| Total Assertions    | 457   |
| Avg Assertions/Test | 9.14  |
| Edge Case Coverage  | 100%  |
| Valid Tests         | 29    |
| Invalid Tests       | 21    |

---

## 🧠 Research Questions

---

### 🔹 RQ1: Effect of Prompting

Advanced prompts improve test quality by increasing assertions and edge-case coverage. However, improvements over context prompts are moderate, showing that structured prompts already perform well.

---

### 🔹 RQ2: Test Quality

Generated tests show strong coverage:

* High number of assertions (457)
* Full edge-case coverage (100%)

This demonstrates that LLMs can generate diverse and comprehensive tests.

---

### 🔹 RQ3: Limitations

* Only ~58% tests are valid
* Many contain syntax errors
* Extra text affects execution
* Logical correctness is not guaranteed

LLMs require **post-processing and validation**.

---

## 🧾 Key Insights

* LLMs generate strong test coverage
* Prompt design affects output quality
* Outputs are not always executable
* Human validation is required

---

## 🏁 Conclusion

LLMs are powerful tools for test generation but are not fully reliable.
They can assist developers but cannot replace them without validation.

---

## 🚀 Future Work

* Improve parsing and cleaning
* Add pytest execution
* Measure code coverage
* Compare with developer tests

---

## 🛠️ Technologies

* Python
* Ollama
* Llama3
* Streamlit

---

## 📌 Final Status

```text
Project Completed: ✅ 100%
```

---

## 🙌 Acknowledgements

* pyMethods2Test dataset
* Ollama LLM framework
* Course guidance

---
