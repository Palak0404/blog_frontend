import streamlit as st
import requests
import json

st.set_page_config(page_title="AI Blog Generator", layout="wide")
st.title("AI Blog Generator")

topic = st.text_input("Enter your blog topic:")
model_choice = st.selectbox("Choose Model:", ["gemini", "gpt-4o-azure"])

if st.button(" Generate Blog"):
    if topic:
        webhook_url = "https://n8n-production-1992.up.railway.app/webhook/blog-generator"
        headers = {"Content-Type": "application/json"}
        payload = {"topic": topic.strip(), "model": model_choice}

        try:
            response = requests.post(webhook_url, json=payload, headers=headers)

            if response.status_code == 200:
                data = response.json()
                github_url = data.get("github_url")

                if github_url:
                    st.success(" Blog generated and saved to GitHub.")
                    st.markdown(
                        f'<a href="{github_url}" target="_blank"><button style="padding:8px 16px; background-color:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;">View Blog</button></a>',
                        unsafe_allow_html=True
                    )
                else:
                    st.success("Blog generated and saved to GitHub.")
            else:
                st.error(f"Failed! Status code: {response.status_code}")
                try:
                    st.json(response.json())
                except Exception:
                    st.text("Raw response:")
                    st.text(response.text)

        except Exception as e:
            st.error(f" Request to webhook failed: {str(e)}")
    else:
        st.warning(" Please enter a topic before generating the blog.")
