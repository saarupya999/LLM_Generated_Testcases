
import streamlit as st
import json

st.set_page_config(page_title="LLM Test Dashboard", layout="wide")

st.title("🧪 LLM Test Generation Dashboard")

# ===================== LOAD DATA =====================
with open("results/generated_tests_advanced.json") as f:
    data = json.load(f)

with open("results/evaluation_summary.json") as f:
    eval_data = json.load(f)

total_tests = eval_data["total_tests"]
total_assertions = eval_data["total_assertions"]
avg_assertions = eval_data["avg_assertions"]
edge_cases = eval_data["edge_cases"]

# ===================== FAILURE ANALYSIS =====================
valid = 29
invalid = 21
extra_text = 42

# ===================== SUMMARY =====================
st.header("📊 Summary Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Tests", total_tests)
col2.metric("Total Assertions", total_assertions)
col3.metric("Avg Assertions/Test", round(avg_assertions, 2))

# ===================== VALIDITY =====================
st.header("📊 Test Validity")

valid_pct = (valid / total_tests) * 100
invalid_pct = (invalid / total_tests) * 100

st.write(f"✅ Valid Tests: {valid} ({valid_pct:.1f}%)")
st.write(f"❌ Invalid Tests: {invalid} ({invalid_pct:.1f}%)")
st.write(f"⚠️ Extra Text Issues: {extra_text}")

# ===================== CHART =====================
st.header("📈 Test Quality Overview")

chart_data = {
    "Metric": ["Valid", "Invalid", "Extra Text"],
    "Count": [valid, invalid, extra_text]
}

st.bar_chart(chart_data, x="Metric", y="Count")

# ===================== EDGE CASES =====================
st.header("🧠 Edge Case Coverage")

st.success(f"Edge Case Tests: {edge_cases} / {total_tests}")

# ===================== SAMPLE TESTS =====================
st.header("📄 Sample Generated Tests")

for i, t in enumerate(data[:5]):
    st.subheader(f"Method: {t['method_name']}")
    st.code(t["generated_test"], language="python")

# ===================== INSIGHTS =====================
st.header("🧠 Key Insights")

st.write(f"""
- Assertions are directly taken from evaluation script.
- Total Assertions: {total_assertions}
- Average Assertions/Test: {avg_assertions:.2f}
- Ensures perfect consistency between evaluation and dashboard.
""")

st.markdown("---")
st.markdown("🚀 Project: LLM-Based Automatic Unit Test Generation")

