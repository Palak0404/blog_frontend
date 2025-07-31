import streamlit as st
import requests
import json

st.set_page_config(page_title="AI Blog Generator", layout="wide")
st.title("AI Blog Generator")

topic = st.text_input("Enter your blog topic:")
model_choice = st.selectbox("Choose Model:", ["gemini", "gpt-4o-azure"])

If st.button(" Generate Blog"):
    If topic:
        webhook_url = "https://n8n-production-1992.up.railway.app/webhook/blog-generator"
        headers = {"Content-Type": "application/json"}
        payload = {"topic": topic.strip(), "model": model_choice}

        Try:
            response = requests.post(webhook_url, json=payload, headers=headers)

            if response.status_code == 200:
                data = response.json()
                github_url = data.get("github_url")

                if github_url:
                    st. markdown(
                        f'Blog generated and saved to GitHub: <a href="{github_url}" target="_blank"><b>View Blog</b></a>',
                        unsafe_allow_html=True
                    )
                Else:
                    st.success("Blog generated and saved to GitHub.")
            Else:
                st.error(f" Failed! Status code: {response.status_code}")
                Try:
                    st.json(response.json())
                Except Exception:
                    st.text("Raw response:")
                    st.text(response.text)

        Except Exception as e:
            st.error(f" Request to webhook failed: {str(e)}")
    Else:
        st.warning("Please enter a topic before generating the blog.")
