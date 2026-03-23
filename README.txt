# LLM-Based Automatic Unit Test Generation Using Focal-Method Datasets

## 📌 Overview

Unit testing is a fundamental practice in modern software engineering, ensuring correctness, reliability, and maintainability of code. However, writing high-quality unit tests manually is time-consuming and often neglected in practice.

This project explores the use of **Large Language Models (LLMs)** to automatically generate unit tests for Python functions using focal-method datasets. We build a complete end-to-end pipeline that extracts focal methods, generates pytest-based tests using an LLM, and evaluates the generated tests using quantitative metrics.

Our approach focuses on understanding how **prompt design impacts test quality**, and whether LLM-generated tests can approximate the behavior of developer-written tests.

---

## 🎯 Objectives

The main goals of this project are:

- Automate unit test generation using LLMs
- Investigate the impact of prompt design on generated tests
- Evaluate test quality using measurable metrics
- Approximate coverage and behavioral correctness of generated tests

---

## ❓ Research Questions

This project is guided by the following research questions:

### 🔹 RQ1
**How does varying the amount of prompt context affect the quality of generated unit tests?**

### 🔹 RQ2
**Can LLM-generated tests approximate the coverage of developer-written tests?**

### 🔹 RQ3
**To what extent do generated assertions align with expected behavior?**

---

## 📊 Dataset

We use the **pyMethods2Test dataset**, which contains:

- Over **88,000 focal methods**
- Mappings between methods and developer-written tests
- Real-world Python projects

This dataset allows us to simulate realistic unit test generation scenarios.

---

## 🏗️ System Architecture

The system follows a modular pipeline:
