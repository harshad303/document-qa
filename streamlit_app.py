import streamlit as st


# Show title and description.
st.title("📄 Document question answering")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management

lab1_page = st.Page("lab1.py", title="Lab1")
lab2_page = st.Page("lab2.py", title="Lab2")

pg = st.navigation([lab1_page, lab2_page])
st.set_page_config(page_title= "Lab2")
pg.run()