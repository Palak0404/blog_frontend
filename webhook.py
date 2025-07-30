import streamlit as st
import requests
import json

st.set_page_config(page_title="Blog Generator", layout="wide")
st.title("Submit Blog Topic")

topic = st.text_input("Enter your blog topic:")
model_choice = st.selectbox("Choose Model:", ["gemini", "gpt-4o-azure"])

if st.button("Generate Blog"):
    if topic:
        webhook_url = "https://n8n-production-1992.up.railway.app/webhook/blog-generator"



        headers = {"Content-Type": "application/json"}
        payload = {"topic": topic.strip(), "model": model_choice}

        try:
            response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

            if response.status_code == 200:
                st.success("Blog generated and saved as blog.md via n8n!")
            else:
                st.error(f"Failed with status code {response.status_code}")
                st.json(response.json())

        except Exception as e:
            st.error(f"Request failed: {str(e)}")
    else:
        st.warning("Please enter a topic before generating the blog.")
