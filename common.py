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
.stButton button {
  font-family: 'Architects Daughter', cursive !important;
  font-size: 1.2rem !important; padding: .9rem 1rem !important;
  border: 1.5px solid #1E1E1E !important; background: #F3E5C0 !important;
}
.stButton button p { font-family: 'Architects Daughter', cursive !important; font-size: 1.2rem !important; }
.stButton button:hover { background: #1E1E1E !important; color: #F3E5C0 !important; }
.stButton button:hover p { color: #F3E5C0 !important; }
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

/* decorative e-note toolbar, fixed to the left edge */
.toolbar {
  position: fixed; left: 0; top: 60px; bottom: 0; width: 62px; z-index: 50;
  background: #EAD9AE; border-right: 1.5px solid #1E1E1E;
  display: flex; flex-direction: column; align-items: center; justify-content: space-evenly;
  padding: 10px 0; pointer-events: none; user-select: none;
}
.tool { display: flex; flex-direction: column; align-items: center; gap: 1px; }
.tool svg { width: 21px; height: 21px; fill: none; stroke: #1E1E1E; stroke-width: 1.5;
            stroke-linecap: round; stroke-linejoin: round; }
.tool span { font-family: 'Architects Daughter', cursive; font-size: 10px; color: #1E1E1E; opacity: .75; }
@media (max-width: 1080px) { .toolbar { display: none; } }   /* hide where it would crowd the page */

/* decorative pencil standing upright in the bottom-right corner, tip up */
.pencil { position: fixed; right: 26px; bottom: 18px; width: 40px; height: 250px;
          z-index: 40; pointer-events: none; }
.pencil svg { position: absolute; width: 250px; left: 50%; top: 50%;
              transform: translate(-50%, -50%) rotate(90deg);
              filter: drop-shadow(-2px 3px 0 rgba(30,30,30,.18)); }
@media (max-width: 1080px) { .pencil { display: none; } }   /* keep it off narrow screens */
</style>
"""


# Hand-drawn #2 pencil, used as decoration in the bottom-right corner
PENCIL_SVG = """
<svg viewBox="0 0 300 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <g stroke="#1E1E1E" stroke-width="1.6" stroke-linejoin="round">
    <polygon points="4,20 34,9 34,31" fill="#E9C9A0"/>              <!-- sharpened wood -->
    <polygon points="4,20 14,16.3 14,23.7" fill="#3A3A3A"/>         <!-- graphite tip -->
    <rect x="34" y="9" width="196" height="22" fill="#F2B632"/>      <!-- yellow body -->
    <line x1="34" y1="16" x2="230" y2="16" stroke-width="0.9" opacity=".55"/>
    <line x1="34" y1="24" x2="230" y2="24" stroke-width="0.9" opacity=".55"/>
    <rect x="230" y="8" width="30" height="24" fill="#C9C9C4"/>      <!-- metal ferrule -->
    <line x1="240" y1="8" x2="240" y2="32" stroke-width="1"/>
    <line x1="250" y1="8" x2="250" y2="32" stroke-width="1"/>
    <path d="M260,8 h24 q10,0 10,12 q0,12 -10,12 h-24 z" fill="#D9776B"/>  <!-- eraser -->
  </g>
  <text x="70" y="24.5" font-family="Architects Daughter, cursive" font-size="9" fill="#1E1E1E">No. 2 · HB</text>
</svg>
"""


# Decorative e-note toolbar down the left edge (purely visual, not clickable)
_I = {  # simple 24x24 line icons
    "Pen":    '<path d="M4 20l3-1 11-11-2-2L5 17z"/><path d="M14 6l2 2"/>',
    "Marker": '<path d="M6 18l2-6 8-8 4 4-8 8z"/><path d="M4 20h7"/>',
    "Eraser": '<path d="M5 15l8-8 6 6-6 6H9z"/><path d="M9 19h11"/>',
    "Lasso":  '<ellipse cx="12" cy="9" rx="8" ry="5" stroke-dasharray="2.5 2"/><path d="M8 13c-2 3 0 6 3 5"/>',
    "Text":   '<path d="M5 6h14M12 6v13M9 19h6"/>',
    "Ruler":  '<rect x="3" y="9" width="18" height="6"/><path d="M7 9v3M11 9v3M15 9v3M19 9v2"/>',
    "Shape":  '<rect x="4" y="4" width="9" height="9"/><circle cx="15.5" cy="15.5" r="4.5"/>',
    "Image":  '<rect x="3" y="5" width="18" height="14"/><path d="M3 16l5-5 4 4 3-3 6 6"/><circle cx="16" cy="9" r="1.4"/>',
    "Undo":   '<path d="M9 7L4 12l5 5"/><path d="M4 12h10a6 6 0 0 1 0 12" transform="translate(0,-6)"/>',
    "Redo":   '<path d="M15 7l5 5-5 5"/><path d="M20 12H10a6 6 0 0 0 0 12" transform="translate(0,-6)"/>',
    "Zoom":   '<circle cx="10" cy="10" r="6"/><path d="M15 15l5 5M8 10h4M10 8v4"/>',
    "Layers": '<path d="M12 4l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    "Pages":  '<rect x="6" y="3" width="12" height="16"/><path d="M9 21h11V7"/>',
    "More":   '<circle cx="6" cy="12" r="1.3"/><circle cx="12" cy="12" r="1.3"/><circle cx="18" cy="12" r="1.3"/>',
}
TOOLBAR_HTML = '<div class="toolbar">' + "".join(
    f'<div class="tool"><svg viewBox="0 0 24 24">{svg}</svg><span>{name}</span></div>'
    for name, svg in _I.items()
) + "</div>"


def apply_style():
    st.markdown(CSS, unsafe_allow_html=True)
    st.markdown(TOOLBAR_HTML, unsafe_allow_html=True)
    st.markdown(f'<div class="pencil">{PENCIL_SVG}</div>', unsafe_allow_html=True)


def sheet(number, title, label=None):
    """Drafting-sheet label + page title."""
    st.markdown(
        f'<div class="sheet"><span>SHEET {number:02d}</span><span>{(label or title).upper()}</span>'
        f'<span>RALPH LONG IV</span></div>',
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
