import streamlit as st
import requests
import json
import time
from pdf_exporter import create_pdf

# Constants
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Smart Business Decision Assistant", layout="wide")

st.title("Smart Business Decision Assistant (SBDA)")
st.write("A Competitor & Market Intelligence tool using RAG and Multi-Agent Architecture.")

st.sidebar.header("Configuration")
query = st.sidebar.text_input("Analysis Query", value="Apple vs Samsung smartphones")
company_name = st.sidebar.text_input("Target Company", value="Apple")
competitors = st.sidebar.text_input("Key Competitors", value="Samsung, Google, Xiaomi")

if st.sidebar.button("Generate Intelligence Report"):
    with st.spinner("Initializing Agent Graph and Planning Research..."):
        try:
            # 1. Trigger the analysis
            payload = {
                "query": query,
                "company_name": company_name,
                "competitors": competitors
            }
            res = requests.post(f"{API_URL}/analyze", json=payload)
            res.raise_for_status()
            analyze_data = res.json()
            
            st.success("Analysis Complete!")
            st.write("### Research Plan")
            st.write(analyze_data.get("plan", "No plan returned."))
            
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
            st.stop()
            
    with st.spinner("Retrieving Final Report..."):
        try:
            # 2. Fetch the report
            time.sleep(1) # wait briefly for state to settle
            rep_res = requests.get(f"{API_URL}/report")
            rep_res.raise_for_status()
            report_data = rep_res.json()
            
            st.markdown("---")
            
            # Display components in tabs
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["Final Report", "SWOT", "Competitor Comparison", "Risk Analysis", "Strategic Recommendations"])
            
            with tab1:
                st.markdown(report_data.get("final_report", "No report content."))
                
                # Export to PDF functionality
                if report_data.get("final_report"):
                    pdf_bytes = create_pdf(report_data["final_report"])
                    st.download_button(
                        label="📄 Download Report as PDF",
                        data=pdf_bytes,
                        file_name="Intelligence_Report.pdf",
                        mime="application/pdf"
                    )
            
            with tab2:
                st.markdown(report_data.get("swot_analysis", "No SWOT analysis found."))
                
            with tab3:
                st.markdown(report_data.get("competitor_comparison", "No competitor comparison found."))
                
            with tab4:
                st.markdown(report_data.get("risk_analysis", "No risk analysis found."))
                
            with tab5:
                st.markdown(report_data.get("recommendations", "No recommendations found."))
                
        except Exception as e:
            st.error(f"Failed to fetch report: {e}")
