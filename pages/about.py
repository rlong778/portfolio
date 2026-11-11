import streamlit as st

from common import ASSETS, first_existing, footer, sheet

sheet(2, "About Me")

st.write(
    "My name is Ralph Long IV. I'm from the city of Atlanta, and I'm a Computer Engineering "
    "student at the Georgia Institute of Technology. I have always had an interest in personal "
    "computing. The first computer I vividly remember was the original iPad. Its aluminum case "
    "and chassis felt futuristic and otherworldly at the time. Computers are a catalyst of "
    "progress that enable innovations in fields that sustain and better human life. I believe "
    "computers can ultimately be a source of good for everyone rather than the few. As I've "
    "gotten older, understanding how much good computers can do for everyone has inspired me to "
    "contribute and innovate in this space. I chose Computer Engineering because I wanted to be "
    "able to tangibly hold the things I'm working on. For me, that tangibility makes the work's "
    "contribution to society feel real."
)

st.markdown("### At Georgia Tech")
st.write(
    "At Georgia Tech, I'm a member of the John Mathers Honors Program and Lambda Delta Rho, the "
    "freshman branch of Georgia Tech's chapter of the National Society of Black Engineers. I'm "
    "already putting my hands-on mindset to work. For my Intro to Computing class, I built a "
    "Python web app with Streamlit that analyzes box office data."
)

photo = first_existing("about.jpg", "about.jpeg", "about.png")
if photo:
    st.image(str(ASSETS / photo), width="stretch")

st.markdown("### Outside of engineering")
st.write(
    "Outside of engineering, I spend my time hiking, lifting, and reading science fiction. "
    "Lifting has taught me that steady, consistent effort adds up over time. Hiking gives me "
    "space to slow down and think. Science fiction, from *Red Rising* to *The Murderbot "
    "Diaries*, keeps me imagining where technology could take us, and what it should and "
    "shouldn't become."
)

with st.container(border=True):
    st.markdown("#### Next up")
    st.write(
        "This coming summer, I plan to land a hardware internship where I can work on something "
        "tangible and real."
    )

footer()
