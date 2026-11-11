"""Shared look-and-feel helpers for every page."""
from pathlib import Path

import streamlit as st

ASSETS = Path(__file__).parent / "assets"

# Your links. Leave EMAIL empty to hide the email link.
GITHUB = "https://github.com/Rlong778"
LINKEDIN = "https://www.linkedin.com/in/ralphlongiv"
EMAIL = ""

CSS = """
<style>

/* manila paper with a faint drafting grid */
.stApp {
  background-color: #F3E5C0;
  background-image:
    linear-gradient(rgba(150,120,60,.13) 1px, transparent 1px),
    linear-gradient(90deg, rgba(150,120,60,.13) 1px, transparent 1px);
  background-size: 22px 22px;
}
header[data-testid="stHeader"] { background: rgba(243,229,192,.92); border-bottom: 1.5px solid #1E1E1E; }
.block-container { max-width: 900px; padding-top: 4.5rem; }

p, li { font-size: 1.02rem; line-height: 1.7; }

/* handwritten headings */
h1, h2, h3, h4,
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
  font-family: 'Architects Daughter', cursive !important;
  font-weight: 400 !important;
  color: #1E1E1E;
  letter-spacing: .02em;
}
h1 { font-size: 2.8rem !important; }

.stDownloadButton button, .stLinkButton a {
  border: 1.5px solid #1E1E1E !important;
  background: #F3E5C0 !important;
  color: #1E1E1E !important;
  font-family: 'Architects Daughter', cursive !important;
  font-size: 1.05rem !important;
}
.stDownloadButton button:hover, .stLinkButton a:hover { background: #1E1E1E !important; color: #F3E5C0 !important; }

/* "SHEET 01 — WELCOME" label above each page title */
.sheet {
  font-family: 'Architects Daughter', cursive;
  font-size: .95rem; letter-spacing: .14em; color: #2B4C7E;
  border-top: 1.5px solid #1E1E1E; border-bottom: 1px solid #1E1E1E;
  padding: 4px 0; margin-bottom: .4rem;
  display: flex; justify-content: space-between;
}
.meta { font-family: 'Architects Daughter', cursive; color: #2B4C7E; font-size: 1.02rem; margin-top: -.6rem; }
.caption { font-family: 'Architects Daughter', cursive; color: #444; font-size: .95rem; text-align: center; margin-top: -.4rem; }
.footer { font-family: 'Architects Daughter', cursive; text-align: center; border-top: 1.5px solid #1E1E1E;
          margin-top: 3rem; padding-top: .8rem; letter-spacing: .08em; }
.footer a { color: #1E1E1E; margin: 0 .6rem; }
a { color: #2B4C7E; }
</style>
"""


def apply_style():
    st.markdown(CSS, unsafe_allow_html=True)


def sheet(number, title):
    """Drafting-sheet label + page title."""
    st.markdown(
        f'<div class="sheet"><span>SHEET {number:02d}</span><span>{title.upper()}</span>'
        f'<span>R. LONG IV</span></div>',
        unsafe_allow_html=True,
    )
    st.title(title)


def meta(text):
    st.markdown(f'<div class="meta">{text}</div>', unsafe_allow_html=True)


def figure(filename, caption=None):
    """Show an image from assets/ (silently skipped if the file isn't there yet)."""
    path = ASSETS / filename
    if not path.exists():
        return
    st.image(str(path), width="stretch")
    if caption:
        st.markdown(f'<div class="caption">{caption}</div>', unsafe_allow_html=True)


def first_existing(*names):
    for n in names:
        if (ASSETS / n).exists():
            return n
    return None


def footer():
    links = [f'<a href="{LINKEDIN}" target="_blank">LinkedIn</a>',
             f'<a href="{GITHUB}" target="_blank">GitHub</a>']
    if EMAIL:
        links.append(f'<a href="mailto:{EMAIL}">Email</a>')
    st.markdown(
        f'<div class="footer">{"".join(links)}<br>'
        f'<span style="font-size:.85rem;opacity:.7">© 2026 Ralph Long IV · built with Python &amp; Streamlit</span></div>',
        unsafe_allow_html=True,
    )
