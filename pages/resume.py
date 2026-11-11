import streamlit as st

from common import ASSETS, footer, sheet

sheet(5, "Résumé")

pdf = ASSETS / "Ralph_Long_IV_Resume.pdf"
st.download_button(
    "Download résumé (PDF)",
    data=pdf.read_bytes(),
    file_name="Ralph_Long_IV_Resume.pdf",
    mime="application/pdf",
)
st.write("")

with st.container(border=True):
    st.image(str(ASSETS / "resume.png"), width="stretch")

footer()
