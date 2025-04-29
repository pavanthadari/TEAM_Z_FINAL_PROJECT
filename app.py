import streamlit as st
from agents.requirements_agent import generate_requirements
from agents.architecture_agent import generate_architecture
from agents.code_agent import generate_code
from agents.uml_agent import generate_uml
from agents.testcase_agent import generate_testcases


st.title("AutoSDLC Architect Pro")
st.caption("COT 6930-001: GenAI Software Development Lifecycles")


idea = st.text_input("💡 Enter your software idea:")

if idea:
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Requirements", "Architecture", "Code", "UML Diagrams", "Test Cases", "📄 Report"])

    with tab1:
        st.subheader("📋 Functional Requirements")
        st.text(generate_requirements(idea))

    with tab2:
        st.subheader("🏗️ System Architecture")
        st.text(generate_architecture(idea))

    with tab3:
        st.subheader("🧱 Code Components")
        st.code(generate_code(idea), language="python")

    with tab4:
        st.subheader("📊 UML Diagrams (Textual)")
        st.text(generate_uml(idea))

    with tab5:
        st.subheader("✅ Auto-Generated Test Cases")
        st.code(generate_testcases(idea), language="python")


    with tab6:
        st.subheader("📄 Project Report (Generated)")
        with st.spinner("Generating report..."):
            import ollama
            report_prompt = f"Write a professional software project report for this idea: {idea}. Include overview, objectives, architecture, and modules."
            try:
                response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': report_prompt}])
                st.text_area("Generated Report", response['message']['content'], height=500)
            except Exception as e:
                st.error(f"Failed to generate report: {e}")
st.markdown('---')
st.caption('Developed by Manish Lnu | manishlnu2024@fau.edu, Sree Teja Reddy Chappidi | schappidi2024@fau.edu, Pavan Thadari | pthadari2024@fau.edu')

