import streamlit as st

from common import ASSETS, figure, first_existing, footer, meta, sheet

sheet(4, "Projects")
st.write(
    "A running record of what I've built and researched. This page grows as I do. "
    "New projects are added to the list below as I finish them."
)

# --- Featured: Discovery Project -------------------------------------------
st.markdown("## Discovery Project: E-Ink Calendar & Weather Display")
meta("ECE Discovery Studio · Fall 2026 · In progress")

st.markdown("### The Problem")
st.write(
    "As a freshman juggling six classes, office hours, and club meetings, I found myself "
    "constantly checking my phone just to see what was next, and getting pulled into "
    "distractions every time. I wanted a way to see my day at a glance without picking up a "
    "screen designed to keep my attention. My goal was a small desk display that shows my "
    "calendar and the day's weather, runs for a long time on a single charge, and stays out of "
    "the way."
)

st.markdown("### The Process")
st.write(
    "The key design decision was the display. I chose an e-ink screen, the same technology used "
    "in e-readers, because it only uses power when the image changes. A calendar only needs to "
    "refresh a few times a day, so e-ink lets the display run far longer on one battery than an "
    "LCD ever could. It's also easy to read in any light and looks more like paper than a screen."
)
figure("fig_eink_diagram.png", "Fig. 2: how data flows from the internet to the e-ink screen")
st.write(
    "The display is powered by a small, low-cost microcontroller that connects to the internet, "
    "pulls in my calendar events and the local forecast, and draws them on the screen. Between "
    "updates, the board is designed to sleep, using almost no power. The biggest engineering "
    "trade-off has been balancing how often the screen updates against how long the battery "
    "lasts: more frequent updates keep information fresh, but every refresh costs energy."
)
figure("fig_tradeoff.png", "Fig. 3: the core trade-off, freshness vs. battery life")

st.markdown("### The Outcome")
build_photo = first_existing("discovery.jpg", "discovery.jpeg", "discovery.png")
if build_photo:
    st.image(str(ASSETS / build_photo), width="stretch")
st.write("*In progress. This section will be updated with results and photos after the "
         "Discovery Project Showcase.*")

st.divider()

# --- More projects: add a new dict to this list to add a project ------------
PROJECTS = [
    {
        "title": "Box Office Data Dashboard",
        "meta": "Python · Streamlit · pandas · Fall 2026",
        "images": [("boxoffice.png", "Screenshot of the dashboard")],
        "text": (
            "For my Intro to Computing (CS 1301) Web Development lab, I built an interactive web "
            "app that analyzes and visualizes box office data for 1,000 films spanning 30 years. "
            "Using pandas, I cleaned, filtered, and aggregated the revenue data to uncover how box "
            "office trends shifted across three decades. I then designed interactive charts and "
            "tables with user filters, so visitors can explore the records themselves instead of "
            "reading a static report. It was my first time building something people could click "
            "through instead of just running in a terminal, and it taught me how to turn raw data "
            "into a tool someone else can actually use."
        ),
    },
    {
        "title": "Self-Driving Lab for the Discovery of Novel Polymers",
        "meta": "Python · Data Analysis · AM2 Lab, Georgia Tech · 2024",
        "images": [("fig_sdl_loop.png", "Fig. 4: the self-driving lab loop, where my scripts fit")],
        "text": (
            "As a Project ENGAGES Scholar, I spent 15 hours a week in Georgia Tech's AM2 Lab, "
            "contributing to a self-driving lab effort that uses automation to speed up the "
            "discovery of new polymer materials. I wrote Python scripts to process and visualize "
            "tensile strength data from mechanical tests of newly developed polymers, helping turn "
            "raw test results into insights the team could act on. Working alongside graduate "
            "students showed me what real research looks like day to day, and the project "
            "advanced to the regional level of competition."
        ),
    },
]

for p in PROJECTS:
    with st.container(border=True):
        st.markdown(f"## {p['title']}")
        meta(p["meta"])
        st.write(p["text"])
        for img, cap in p["images"]:
            figure(img, cap)

footer()
