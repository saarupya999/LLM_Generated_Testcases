
import streamlit as st
import json
import os

st.set_page_config(page_title="LLM Test Dashboard", layout="wide")

# ===================== HEADER =====================
st.markdown("""
    <h1 style='text-align: center;'>🧪 LLM Test Generation Dashboard</h1>
    <p style='text-align: center; color: gray;'>Interactive Analysis of LLM-Generated Unit Tests</p>
""", unsafe_allow_html=True)

# ===================== LOAD DATA =====================
def load_json(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

data = load_json("results/generated_tests_advanced.json")
eval_data = load_json("results/evaluation_summary.json")

total_tests = eval_data.get("total_tests", len(data))
total_assertions = eval_data.get("total_assertions", 0)
avg_assertions = eval_data.get("avg_assertions", 0)
edge_cases = eval_data.get("edge_cases", 0)

# ===================== REFRESH BUTTON =====================
if st.button("🔄 Refresh Dashboard"):
    st.rerun()

# ===================== METRICS =====================
st.markdown("## 📊 Summary Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("🧪 Total Tests", total_tests)
col2.metric("✅ Total Assertions", total_assertions)
col3.metric("📈 Avg Assertions/Test", round(avg_assertions, 2))

# ===================== FAILURE ANALYSIS =====================

failure_data = load_json("results/failure_summary.json")

valid = failure_data.get("valid", 0)
syntax_errors = failure_data.get("syntax_errors", 0)
no_assertions = failure_data.get("no_assertions", 0)
extra_text = failure_data.get("extra_text", 0)


# ===================== VALIDITY =====================
st.markdown("## 📊 Test Quality Breakdown")

col1, col2, col3, col4 = st.columns(4)

col1.metric("✅ Valid Code", valid)
col2.metric("❌ Syntax Errors", syntax_errors)
col3.metric("⚠️ No Assertions", no_assertions)
col4.metric("📄 Extra Text", extra_text)

# ===================== CHART =====================
chart_data = {
    "Metric": ["Valid", "Syntax Errors", "No Assertions", "Extra Text"],
    "Count": [valid, syntax_errors, no_assertions, extra_text]
}

st.bar_chart(chart_data, x="Metric", y="Count")

# ===================== EDGE CASE =====================
st.markdown("## 🧠 Edge Case Coverage")

progress = edge_cases / total_tests if total_tests > 0 else 0
st.progress(progress)
st.write(f"{edge_cases} / {total_tests} tests include edge cases")

# ===================== FILTER =====================
st.markdown("## 🔍 Explore Generated Tests")

method_names = [t.get("method_name", "Unknown") for t in data]
selected = st.selectbox("Select Method", method_names)

for t in data:
    if t.get("method_name") == selected:
        st.code(t.get("generated_test", ""), language="python")

# ===================== SAMPLE TESTS =====================
st.markdown("## 📄 Sample Tests")

for t in data[:3]:
    with st.expander(f"📌 {t.get('method_name', 'Unknown')}"):
        st.code(t.get("generated_test", ""), language="python")

# ===================== INSIGHTS =====================
st.markdown("## 🧠 Key Insights")

st.success(f"""
- Total Assertions: {total_assertions}
- Average Assertions/Test: {avg_assertions:.2f}
- Edge Case Coverage: {edge_cases}/{total_tests}
- LLM generates high coverage but limited execution reliability.
- Requires validation before real-world usage.
""")

# ===================== FOOTER =====================
st.markdown("---")
st.markdown("<p style='text-align:center;'>🚀 LLM-Based Automatic Unit Test Generation</p>", unsafe_allow_html=True)

