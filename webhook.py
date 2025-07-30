import streamlit as st
import requests
import json

st.set_page_config(page_title="Blog Generator", layout="wide")
st.title(" AI Blog Generator")

# Input fields
topic = st.text_input("Enter your blog topic:")
model_choice = st.selectbox("Choose Model:", ["gemini", "gpt-4o-azure"])

if st.button("Generate Blog"):
    if topic:
        
        webhook_url = "https://n8n-production-1992.up.railway.app/webhook/blog-generator"

        headers = {"Content-Type": "application/json"}
        payload = {"topic": topic.strip(), "model": model_choice}

        # Display request being sent
        st.info("⏳ Sending request to n8n webhook...")

        try:
            response = requests.post(webhook_url, json=payload, headers=headers)

            st.write(f" Status Code: {response.status_code}")

            if response.status_code == 200:
                st.success(" Blog generated and saved as blog.md!")
                try:
                    st.subheader("Webhook Response:")
                    st.json(response.json())  # Try to show actual response
                except Exception:
                    st.text("ℹResponse could not be parsed as JSON.")
                    st.text(response.text)
            else:
                st.error(f" Failed! Status code: {response.status_code}")
                try:
                    st.json(response.json())
                except Exception:
                    st.text("⚠ Raw response:")
                    st.text(response.text)

        except Exception as e:
            st.error(f" Request to webhook failed: {str(e)}")
    else:
        st.warning("⚠ Please enter a topic before generating the blog.")
