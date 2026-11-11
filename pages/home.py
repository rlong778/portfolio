import streamlit as st

from common import ASSETS, first_existing, footer, sheet

sheet(1, "Ralph Long IV")
st.markdown('<div class="meta">Computer Engineering · Georgia Institute of Technology</div>',
            unsafe_allow_html=True)
st.write("")

photo = first_existing("headshot.jpg", "headshot.jpeg", "headshot.png")
if photo:
    left, right = st.columns([1, 2], gap="large")
    left.image(str(ASSETS / photo), width="stretch")
    body = right
else:
    body = st.container()

with body:
    st.markdown("## Welcome")
    st.write(
        "Hi, my name is Ralph Long IV, and I'm a Computer Engineering student attending the "
        "Georgia Institute of Technology. I'm passionate about hiking, lifting, and reading sci-fi "
        "novels. I plan to work on silicon design for consumer electronics, with a focus on "
        "maximizing performance and lowering cost. My favorite thing about personal computers is "
        "their ability to maximize our personal creativity. I believe in consumer-focused hardware "
        "with the satisfaction of the customer as the goal. Please explore my hobbies, interests, "
        "and the projects I've built."
    )

st.write("")
st.markdown("### Explore the sheets")
c1, c2 = st.columns(2)
with c1.container(border=True):
    st.page_link("pages/about.py", label="Sheet 02 · About Me")
    st.caption("Where I'm from and why I build hardware")
with c2.container(border=True):
    st.page_link("pages/career.py", label="Sheet 03 · Career Goals")
    st.caption("My roadmap from Georgia Tech to silicon design")
c3, c4 = st.columns(2)
with c3.container(border=True):
    st.page_link("pages/projects.py", label="Sheet 04 · Projects")
    st.caption("E-ink display, data dashboard, polymer research")
with c4.container(border=True):
    st.page_link("pages/resume.py", label="Sheet 05 · Résumé")
    st.caption("View or download my résumé")

footer()
