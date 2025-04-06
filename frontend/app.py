# frontend/app.py

import streamlit as st
import requests

# MUST BE FIRST Streamlit command
st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")

st.title("🔍 SHL Assessment Recommendation Tool")
st.write("Paste your job description or hiring query below:")

query = st.text_area("Job Description or Query", height=200)

if st.button("Get Recommendations"):
    with st.spinner("Finding best assessments..."):
        try:
            res = requests.post("http://localhost:8080/recommend", json={"query": query})
            if res.status_code == 200:
                results = res.json()
                if results:
                    st.success("Here are the top recommendations:")
                    for r in results:
                        st.markdown(f"### [{r['Assessment Name']}]({r['URL']})")
                        st.write(f"**Type:** {r['Test Type']} | **Duration:** {r['Duration']} min")
                        st.write(f"Remote: {r['Remote Support']} | Adaptive: {r['Adaptive Support']}")
                        st.markdown("---")
                else:
                    st.warning("No recommendations found for your query.")
            else:
                st.error("Error getting recommendations. Please check the backend service.")
        except Exception as e:
            st.error(f"Error: {e}")
