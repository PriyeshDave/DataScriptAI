import streamlit as st
from services.test_case_generator import TestCaseGenerator
from services.synthetic_data_generator import SyntheticDataGenerator
from services.karate_script_generator import KarateScriptGenerator

test_case_generator = TestCaseGenerator()
synthetic_data_generator = SyntheticDataGenerator()
karate_script_generator = KarateScriptGenerator()

st.title("AI-Powered API Test Automation")

business_justification = st.text_area("Enter Business Justification for API Testing")
test_cases = None
if st.button("Generate Test Cases"):
    test_cases = test_case_generator.generate_test_cases(business_justification)
    st.session_state["test_cases"] = test_cases

if "test_cases" in st.session_state:
    st.subheader("Generated Test Cases")
    st.write(test_cases)
    response_json = {"test_cases": test_cases}
    # st.json(response_json) 
    #st.write(type(st.session_state["test_cases"]))
    #st.json(st.session_state["test_cases"])

    if st.button("Generate Synthetic Data"):
        attributes = synthetic_data_generator.get_attributes(st.session_state["test_cases"])
        synthetic_data = synthetic_data_generator.generate_synthetic_data(attributes)
        st.session_state["synthetic_data"] = synthetic_data
        st.json(synthetic_data)

if "test_cases" in st.session_state:
    if st.button("Generate Automation Scripts"):
        karate_script = karate_script_generator.generate_karate_script(st.session_state["test_cases"])
        st.session_state["karate_script"] = karate_script
        st.code(karate_script, language="java")
