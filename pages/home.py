import streamlit as st

from common import ASSETS, first_existing, footer, sheet

sheet(1, "Ralph Long IV", label="Welcome")
st.markdown('<div class="meta">Computer Engineering · Georgia Institute of Technology</div>',
            unsafe_allow_html=True)
st.write("")

photo = first_existing("headshot.jpg", "headshot.jpeg", "headshot.png")
if photo:
    left, right = st.columns([1, 2], gap="large", vertical_alignment="center")
    with left.container(border=True):  # thin black frame, like a mounted photo
        st.image(str(ASSETS / photo), width="stretch")
        st.markdown('<div class="caption">Ralph Long IV · Atlanta, GA</div>', unsafe_allow_html=True)
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

# (button label, page file, short description) — each is a clickable button
SHEETS = [
    ("Sheet 02 · About Me", "pages/about.py", "Where I'm from and why I build hardware"),
    ("Sheet 03 · Career Goals", "pages/career.py", "My roadmap from Georgia Tech to silicon design"),
    ("Sheet 04 · Projects", "pages/projects.py", "E-ink display, data dashboard, polymer research"),
    ("Sheet 05 · Résumé", "pages/resume.py", "View or download my résumé"),
]
for row in (SHEETS[:2], SHEETS[2:]):
    cols = st.columns(2)
    for col, (label, page, desc) in zip(cols, row):
        with col:
            if st.button(label, key=page, width="stretch"):
                st.switch_page(page)
            st.caption(desc)

footer()
