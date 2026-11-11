import streamlit as st

from common import figure, footer, sheet

sheet(3, "Career Goals")

st.markdown("## Where I want to go")
st.write(
    "My long-term goal is to design silicon for consumer electronics at a company like Apple or "
    "NVIDIA. I want to build chips that deliver more performance at a lower cost, so powerful "
    "computing reaches more people."
)

figure("fig_roadmap.png", "Fig. 1: my four-year roadmap, from foundation to chip design")

st.markdown("## How I'll get there")

# (year, theme, text) — add or edit rows here
YEARS = [
    ("Year 1 · 2026–27", "Build the foundation",
     "I'm strengthening my math and programming base with calculus, linear algebra, and Digital "
     "System Design (ECE 2020). This spring, I'll join Silicon Jackets, Georgia Tech's chip "
     "design club, to get early hands-on experience with how chips are designed. I'm also "
     "pursuing a Summer 2027 internship by attending the NSBE Fall Regional Conference and "
     "spring career fairs, with my résumé reviewed by the Career Center first."),
    ("Year 2 · 2027–28", "Connect hardware and software",
     "Courses like Computer Organization & Programming (CS 2110), Digital Design Lab (ECE 2031), "
     "and Programming Hardware/Software Systems (ECE 2035) will show me how code meets circuits. "
     "The summer before junior year, I plan to study abroad. I've done it once before, and "
     "seeing how other cultures use technology shapes how I think about designing for people."),
    ("Year 3 · 2028–29", "Specialize",
     "I'll start my threads with Embedded Systems Design (ECE 4180) and VLSI & Advanced Digital "
     "Design (ECE 3150). I'll also join undergraduate research through the Vertically Integrated "
     "Projects (VIP) program, and work toward a spot in a circuits research lab like ICSRL."),
    ("Year 4 · 2029–30", "Go deep on chips",
     "I'll finish with Digital Integrated Circuits (ECE 4420), Advanced Computer Architecture "
     "(ECE 4100), and Advanced VLSI Systems (ECE 4130), plus my senior design project. I'll "
     "graduate in Spring 2030 ready for a silicon design role."),
]

for year, theme, text in YEARS:
    with st.container(border=True):
        st.markdown(f"#### {year}: {theme}")
        st.write(text)

st.markdown("## Skills I still need to build")
SKILLS = [
    ("Hardware description languages (Verilog/SystemVerilog)",
     "through Silicon Jackets and my digital design courses"),
    ("Circuit and VLSI design tools", "through my thread courses and research"),
    ("Computer architecture", "through ECE 3058 and ECE 4100"),
    ("Industry experience", "through internships each summer"),
]
for skill, how in SKILLS:
    st.markdown(f"- **{skill}:** {how}")

footer()
