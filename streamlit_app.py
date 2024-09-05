import streamlit as st


# Show title and description.
st.title("📄 Document question answering")

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management

lab1_page = st.Page("lab1.py", title="Lab1")
lab2_page = st.Page("lab2.py", title="Lab2")

pg = st.navigation([lab1_page, lab2_page])
st.set_page_config(page_title= "Lab2")
pg.run()