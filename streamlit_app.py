"""Ralph Long IV — ePortfolio.  Run locally with:  streamlit run streamlit_app.py"""
import streamlit as st

from common import apply_style

st.set_page_config(page_title="Ralph Long IV · ePortfolio", page_icon="📐", layout="centered")
apply_style()

pages = [
    st.Page("pages/home.py", title="Home", default=True),
    st.Page("pages/about.py", title="About Me"),
    st.Page("pages/career.py", title="Career Goals"),
    st.Page("pages/projects.py", title="Projects"),
    st.Page("pages/resume.py", title="Résumé"),
]

st.navigation(pages, position="top").run()
