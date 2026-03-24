# LLM-Based Automatic Unit Test Generation Using Focal-Method Datasets

## 📌 Overview

Writing high-quality unit tests is a critical yet time-consuming task in software development. Developers often struggle to maintain sufficient test coverage due to time constraints, leading to potential bugs and reduced software reliability.

This project explores the use of **Large Language Models (LLMs)** to automatically generate unit tests for Python functions (focal methods). Using the **pyMethods2Test dataset**, we design and implement a complete pipeline for:

* Extracting focal methods
* Generating unit tests using an LLM
* Evaluating generated tests using behavioral metrics
* Conducting prompt-based experiments

The primary goal is to understand how **prompt design impacts test quality**.

---

## 🎯 Objectives

This project aims to:

* Automate unit test generation using LLMs
* Analyze the impact of prompt engineering on test quality
* Evaluate generated tests using measurable metrics
* Approximate coverage of developer-written tests

---

## ❓ Research Questions

### RQ1: How does prompt context affect generated test quality?

We compare:

* Baseline prompt (minimal context)
* Context-enhanced prompt (detailed instructions)

---

### RQ2: Can LLM-generated tests approximate developer-written test coverage?

We approximate coverage using:

* Assertion density
* Edge-case detection

---

### RQ3: Do generated assertions align with expected behavior?

We evaluate:

* Number of assertions per test
* Diversity of test cases

---

## 📊 Dataset

We use the **pyMethods2Test dataset**, which contains:

* Focal methods (functions under test)
* Metadata about test mappings
* Extracted from real-world Python repositories

Dataset size:

* ~88,000 method-test pairs

---

## ⚙️ System Architecture

The system pipeline consists of the following stages:

```
Dataset
  ↓
Method Extraction
  ↓
Sampling
  ↓
LLM Test Generation
  ↓
Evaluation
```

---

## 🧩 Project Structure

```
LLM_Test_Generator_Project
│
├── pymethods2test/
│
├── scripts/
│   ├── extract_methods.py
│   ├── sample_methods.py
│   ├── generate_tests_llm.py
│   ├── evaluate_tests.py
│   ├── compare_results.py
│
├── results/
│   ├── extracted_methods.json
│   ├── sampled_methods.json
│   ├── generated_tests_baseline.json
│   ├── generated_tests_context.json
│
└── README.md
```

---

## 🚀 Implementation Details

### 1. Method Extraction

Script: `extract_methods.py`

* Reads `.focal.json` files from dataset
* Extracts:

  * method name
  * source file
  * line numbers

Output:

```
results/extracted_methods.json
```

---

### 2. Sampling

Script: `sample_methods.py`

* Samples 1000 methods randomly
* Reduces dataset size for experimentation

Output:

```
results/sampled_methods.json
```

---

### 3. Test Generation

Script: `generate_tests_llm.py`

Uses:

* **Ollama** (local LLM runtime)
* **Llama3 model**

Generates pytest test cases using prompts.

---

### Prompt Variants

#### 🔹 Baseline Prompt

* Minimal instructions
* Only method name

#### 🔹 Context Prompt

* Developer-style instructions
* Includes:

  * edge cases
  * multiple assertions
  * realistic testing patterns

---

### 4. Evaluation

Script: `evaluate_tests.py`

Metrics used:

| Metric             | Description                     |
| ------------------ | ------------------------------- |
| Assertion Count    | Number of assertions in tests   |
| Average Assertions | Assertions per test             |
| Edge Cases         | Presence of boundary/edge tests |

---

### 5. Comparison

Script: `compare_results.py`

* Compares baseline vs context prompts
* Computes behavioral coverage

---

## 📈 Experimental Setup

* Sample size: 50 focal methods
* Two prompt variants tested
* Local LLM inference using Ollama

---

## 📊 Results

| Metric             | Baseline | Context |
| ------------------ | -------- | ------- |
| Generated Tests    | 50       | 50      |
| Total Assertions   | 157      | 286     |
| Average Assertions | 3.14     | 5.72    |
| Edge Cases         | 39       | 45      |

---

## 📌 Key Findings

* Context-based prompts significantly improve test quality
* More assertions → better validation
* More edge cases → stronger robustness

---

## 🧠 Interpretation

* Prompt engineering plays a crucial role in LLM performance
* Minimal prompts lead to generic tests
* Context prompts guide LLM to generate realistic developer-like tests

---

## ⚠️ Limitations

* No real execution-based coverage measurement
* Developer tests not directly executed
* Limited to Python dataset

---

## 🔮 Future Work

* Integrate `pytest-cov` for real coverage
* Compare with developer-written tests directly
* Use larger LLM models (e.g., GPT-4)
* Include method code in prompts

---

## 🧪 How to Run

### Step 1: Extract Methods

```
python3 scripts/extract_methods.py
```

### Step 2: Sample Methods

```
python3 scripts/sample_methods.py
```

### Step 3: Generate Tests

```
python3 scripts/generate_tests_llm.py
```

### Step 4: Evaluate Tests

```
python3 scripts/evaluate_tests.py
```

---

## 🛠️ Technologies Used

* Python
* Ollama
* Llama3
* JSON processing
* Regular expressions

---

## 📚 Related Work

* EvoSuite (search-based testing)
* Randoop (random testing)
* Transformer-based test generation
* LLM-based test generation research

---

## 👥 Authors

* Siwani Sah
* Saarupya Sunkara
* Alexandra Hyatali

---

## 🏫 Institution

Florida Polytechnic University
Instructor: Dr. Karim Elish

---

## 📌 Conclusion

This project demonstrates that LLMs can effectively generate unit tests, and that prompt design significantly impacts test quality. The results highlight the importance of context in guiding LLM behavior for software testing tasks.
