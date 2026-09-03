import streamlit as st


def load_css():

    # =========================================================
    # THEME
    # =========================================================

    theme = st.session_state.get("theme", "light")

    if theme == "dark":

        BG = "#0F172A"
        CARD = "#1E293B"
        CARD_HOVER = "#263449"
        SIDEBAR = "#111827"

        TEXT = "#F8FAFC"
        SUBTEXT = "#94A3B8"
        MUTED = "#64748B"

        BORDER = "#334155"
        BORDER_HOVER = "#475569"

        PRIMARY = "#3B82F6"
        PRIMARY_HOVER = "#2563EB"

        INPUT = "#1E293B"
        INPUT_BORDER = "#475569"

        SUCCESS_BG = "#14532D"
        SUCCESS_TEXT = "#86EFAC"

        WARNING_BG = "#78350F"
        WARNING_TEXT = "#FCD34D"

        DANGER_BG = "#7F1D1D"
        DANGER_TEXT = "#FCA5A5"

        CHIP_BG = "#1E293B"

        SHADOW = "0 10px 30px rgba(0,0,0,.25)"
        SHADOW_HOVER = "0 18px 45px rgba(0,0,0,.35)"

    else:

        BG = "#F8FAFC"
        CARD = "#FFFFFF"
        CARD_HOVER = "#FFFFFF"
        SIDEBAR = "#FFFFFF"

        TEXT = "#111827"
        SUBTEXT = "#6B7280"
        MUTED = "#94A3B8"

        BORDER = "#E5E7EB"
        BORDER_HOVER = "#BFDBFE"

        PRIMARY = "#2563EB"
        PRIMARY_HOVER = "#1D4ED8"

        INPUT = "#FFFFFF"
        INPUT_BORDER = "#CBD5E1"

        SUCCESS_BG = "#DCFCE7"
        SUCCESS_TEXT = "#166534"

        WARNING_BG = "#FEF3C7"
        WARNING_TEXT = "#92400E"

        DANGER_BG = "#FEE2E2"
        DANGER_TEXT = "#991B1B"

        CHIP_BG = "#F8FAFC"

        SHADOW = "0 8px 25px rgba(15,23,42,.06)"
        SHADOW_HOVER = "0 18px 45px rgba(15,23,42,.12)"

    # =========================================================
    # CSS
    # =========================================================

    st.markdown(
        f"""
<style>

@import url(
    'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);


/* =========================================================
   GLOBAL
========================================================= */

html,
body,
[class*="css"] {{

    font-family: "Inter", sans-serif;

}}

.stApp {{

    background: {BG};

    color: {TEXT};

    transition:
        background-color .25s ease,
        color .25s ease;

}}

.block-container {{

    max-width: 1280px;

    padding-top: 1.5rem;
    padding-bottom: 3rem;

    padding-left: 2rem;
    padding-right: 2rem;

}}


/* =========================================================
   STREAMLIT CHROME
========================================================= */

#MainMenu {{

    visibility: hidden;

}}

footer {{

    visibility: hidden;

}}

header {{

    visibility: hidden;

}}


/* =========================================================
   TEXT
========================================================= */

h1,
h2,
h3,
h4,
h5,
h6,
p,
label {{

    color: {TEXT};

}}

.stCaption,
[data-testid="stCaptionContainer"] {{

    color: {SUBTEXT};

}}


/* =========================================================
   SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {{

    background: {SIDEBAR};

    border-right: 1px solid {BORDER};

    width: 300px !important;

    min-width: 300px !important;

    max-width: 300px !important;

    transition:
        background-color .25s ease,
        border-color .25s ease;

}}

section[data-testid="stSidebar"] > div {{

    padding-top: 1.5rem;

}}

section[data-testid="stSidebar"] * {{

    color: {TEXT};

}}

section[data-testid="stSidebar"] hr {{

    border: none;

    border-top: 1px solid {BORDER};

    margin: 20px 0;

}}


/* Sidebar title */

.sidebar-title {{

    font-size: 22px;

    font-weight: 800;

    letter-spacing: -0.5px;

    color: {TEXT};

    margin-bottom: 5px;

}}

.sidebar-subtitle {{

    font-size: 13px;

    color: {SUBTEXT};

    margin-bottom: 20px;

}}


/* Sidebar cards */

.sidebar-card {{

    background: {CARD};

    border: 1px solid {BORDER};

    border-radius: 16px;

    padding: 16px;

    margin-bottom: 15px;

    box-shadow: {SHADOW};

    transition:
        transform .2s ease,
        box-shadow .2s ease,
        border-color .2s ease;

}}

.sidebar-card:hover {{

    transform: translateY(-2px);

    box-shadow: {SHADOW_HOVER};

    border-color: {BORDER_HOVER};

}}

.sidebar-heading {{

    font-size: 14px;

    font-weight: 700;

    color: {TEXT};

    margin-bottom: 8px;

}}

.sidebar-text {{

    font-size: 13px;

    line-height: 1.8;

    color: {SUBTEXT};

}}


/* =========================================================
   TOGGLE
========================================================= */

[data-testid="stSidebar"] [data-testid="stToggle"] {{

    margin-bottom: 8px;

}}


/* =========================================================
   NAVBAR
========================================================= */

.navbar {{

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding-bottom: 18px;

    margin-bottom: 10px;

    border-bottom: 1px solid {BORDER};

}}

.nav-left {{

    display: flex;

    align-items: center;

    gap: 12px;

    font-size: 21px;

    font-weight: 700;

    color: {TEXT};

}}

.nav-right {{

    font-size: 14px;

    color: {SUBTEXT};

}}

.logo-circle {{

    width: 42px;

    height: 42px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 12px;

    background: linear-gradient(
        135deg,
        {PRIMARY},
        #6366F1
    );

    color: white;

    font-size: 20px;

    box-shadow:
        0 6px 16px rgba(37,99,235,.25);

}}


/* =========================================================
   HERO
========================================================= */

.hero {{

    text-align: center;

    padding:
        48px
        20px
        25px
        20px;

}}

.hero-title {{

    font-size: 52px;

    line-height: 1.1;

    font-weight: 800;

    letter-spacing: -1.8px;

    color: {TEXT};

    margin-bottom: 16px;

}}

.hero-subtitle {{

    max-width: 760px;

    margin: auto;

    font-size: 18px;

    line-height: 1.8;

    color: {SUBTEXT};

}}

.hero-subtitle b {{

    color: {PRIMARY};

    font-weight: 700;

}}


/* =========================================================
   SEARCH CARD
========================================================= */

.search-card {{

    background: {CARD};

    border: 1px solid {BORDER};

    border-radius: 24px;

    padding: 30px;

    margin-top: 25px;

    margin-bottom: 35px;

    box-shadow: {SHADOW};

    transition:
        box-shadow .25s ease,
        border-color .25s ease;

}}

.search-card:hover {{

    border-color: {BORDER_HOVER};

    box-shadow: {SHADOW_HOVER};

}}


/* =========================================================
   TEXT INPUT
========================================================= */

.stTextInput input {{

    width: 100%;

    height: 58px;

    box-sizing: border-box;

    background: {INPUT};

    color: {TEXT};

    border: 1px solid {INPUT_BORDER};

    border-radius: 14px;

    padding-left: 18px;

    padding-right: 18px;

    font-size: 16px;

    transition:
        border-color .2s ease,
        box-shadow .2s ease;

}}

.stTextInput input::placeholder {{

    color: {MUTED};

}}

.stTextInput input:focus {{

    border: 2px solid {PRIMARY};

    box-shadow:
        0 0 0 4px rgba(37,99,235,.12);

}}


/* =========================================================
   BUTTONS
========================================================= */

.stButton > button {{

    width: 100%;

    min-height: 54px;

    border: none;

    border-radius: 14px;

    background: linear-gradient(
        135deg,
        {PRIMARY},
        #4F46E5
    );

    color: white;

    font-size: 16px;

    font-weight: 600;

    letter-spacing: .1px;

    box-shadow:
        0 6px 18px rgba(37,99,235,.20);

    transition:
        transform .2s ease,
        box-shadow .2s ease,
        filter .2s ease;

}}

.stButton > button:hover {{

    transform: translateY(-2px);

    filter: brightness(.96);

    box-shadow:
        0 10px 25px rgba(37,99,235,.30);

}}

.stButton > button:active {{

    transform: translateY(0);

}}


/* =========================================================
   SUGGESTION CHIPS
========================================================= */

.chip {{

    display: inline-block;

    padding: 8px 14px;

    margin:
        4px
        4px
        4px
        0;

    border-radius: 999px;

    background: {CHIP_BG};

    border: 1px solid {BORDER};

    color: {SUBTEXT};

    font-size: 13px;

    font-weight: 500;

    transition:
        background .2s ease,
        color .2s ease,
        border-color .2s ease;

}}

.chip:hover {{

    background: rgba(37,99,235,.08);

    color: {PRIMARY};

    border-color: {PRIMARY};

}}


/* =========================================================
   METRICS CONTAINER
========================================================= */

.metrics-container {{

    margin-top: 10px;

    margin-bottom: 35px;

}}


/* =========================================================
   METRIC CARD
========================================================= */

.metric-card {{

    min-height: 175px;

    background: {CARD};

    border: 1px solid {BORDER};

    border-radius: 20px;

    padding: 24px;

    text-align: center;

    box-shadow: {SHADOW};

    transition:
        transform .25s ease,
        box-shadow .25s ease,
        border-color .25s ease;

}}

.metric-card:hover {{

    transform: translateY(-5px);

    border-color: {BORDER_HOVER};

    box-shadow: {SHADOW_HOVER};

}}

.metric-icon {{

    width: 58px;

    height: 58px;

    margin: 0 auto 15px auto;

    border-radius: 16px;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 25px;

}}

.metric-value {{

    font-size: 30px;

    font-weight: 800;

    line-height: 1.2;

    color: {TEXT};

}}

.metric-title {{

    margin-top: 7px;

    font-size: 14px;

    color: {SUBTEXT};

    font-weight: 500;

}}


/* =========================================================
   RESULTS HEADER
========================================================= */

.results-title {{

    margin-top: 30px;

    margin-bottom: 20px;

    font-size: 27px;

    font-weight: 750;

    letter-spacing: -.5px;

    color: {TEXT};

}}


/* =========================================================
   RESULT CARD
========================================================= */

.result-card {{

    background: {CARD};

    border: 1px solid {BORDER};

    border-radius: 20px;

    padding: 24px;

    margin-bottom: 20px;

    box-shadow: {SHADOW};

    transition:
        transform .25s ease,
        box-shadow .25s ease,
        border-color .25s ease;

}}

.result-card:hover {{

    transform: translateY(-3px);

    border-color: {BORDER_HOVER};

    box-shadow: {SHADOW_HOVER};

}}

.result-header {{

    display: flex;

    justify-content: space-between;

    align-items: flex-start;

    gap: 20px;

}}

.result-title {{

    font-size: 20px;

    font-weight: 700;

    line-height: 1.4;

    color: {TEXT};

}}

.result-content {{

    margin-top: 18px;

    font-size: 15px;

    line-height: 1.8;

    color: {SUBTEXT};

}}

.result-footer {{

    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 15px;

    margin-top: 20px;

}}


/* =========================================================
   CATEGORY BADGE
========================================================= */

.category-badge {{

    display: inline-flex;

    align-items: center;

    padding: 7px 13px;

    border-radius: 999px;

    background: rgba(37,99,235,.10);

    color: {PRIMARY};

    border: 1px solid rgba(37,99,235,.15);

    font-size: 12px;

    font-weight: 600;

}}


/* =========================================================
   SCORE BADGES
========================================================= */

.score {{

    min-width: 68px;

    padding: 8px 12px;

    border-radius: 10px;

    text-align: center;

    font-size: 13px;

    font-weight: 700;

}}

.score-high {{

    background: {SUCCESS_BG};

    color: {SUCCESS_TEXT};

}}

.score-medium {{

    background: {WARNING_BG};

    color: {WARNING_TEXT};

}}

.score-low {{

    background: {DANGER_BG};

    color: {DANGER_TEXT};

}}


/* =========================================================
   CUSTOM PROGRESS BAR
========================================================= */

.progress-wrapper {{

    width: 100%;

    height: 8px;

    margin-top: 20px;

    margin-bottom: 8px;

    overflow: hidden;

    border-radius: 999px;

    background: {BORDER};

}}

.progress-bar {{

    height: 100%;

    border-radius: 999px;

    background: linear-gradient(
        90deg,
        {PRIMARY},
        #6366F1
    );

    transition:
        width .5s ease;

}}


/* =========================================================
   EXPANDER
========================================================= */

[data-testid="stExpander"] {{

    background: transparent;

    border: 1px solid {BORDER};

    border-radius: 12px;

}}

[data-testid="stExpander"] summary {{

    color: {TEXT};

    font-weight: 600;

}}

[data-testid="stExpander"] summary:hover {{

    color: {PRIMARY};

}}


/* =========================================================
   DIVIDER
========================================================= */

hr {{

    border: none;

    border-top: 1px solid {BORDER};

    margin:
        25px
        0;

}}


/* =========================================================
   ALERTS
========================================================= */

[data-testid="stAlert"] {{

    border-radius: 14px;

}}


/* =========================================================
   SPINNER
========================================================= */

[data-testid="stSpinner"] {{

    color: {PRIMARY};

}}


/* =========================================================
   FOOTER
========================================================= */

.footer {{

    text-align: center;

    margin-top: 60px;

    padding-top: 24px;

    border-top: 1px solid {BORDER};

    color: {SUBTEXT};

    font-size: 13px;

    line-height: 1.8;

}}


/* =========================================================
   ANIMATIONS
========================================================= */

.hero,
.search-card,
.metric-card,
.result-card {{

    animation:
        fadeUp .45s ease both;

}}

@keyframes fadeUp {{

    from {{

        opacity: 0;

        transform: translateY(15px);

    }}

    to {{

        opacity: 1;

        transform: translateY(0);

    }}

}}


/* =========================================================
   SCROLLBAR
========================================================= */

::-webkit-scrollbar {{

    width: 8px;

}}

::-webkit-scrollbar-track {{

    background: transparent;

}}

::-webkit-scrollbar-thumb {{

    background: {MUTED};

    border-radius: 999px;

}}

::-webkit-scrollbar-thumb:hover {{

    background: {SUBTEXT};

}}


/* =========================================================
   RESPONSIVE
========================================================= */

@media (max-width: 900px) {{

    .block-container {{

        padding-left: 1rem;

        padding-right: 1rem;

    }}

    .hero {{

        padding-top: 30px;

    }}

    .hero-title {{

        font-size: 38px;

    }}

    .hero-subtitle {{

        font-size: 16px;

    }}

    .search-card {{

        padding: 20px;

    }}

    .metric-card {{

        min-height: 150px;

        padding: 18px;

    }}

    .metric-value {{

        font-size: 25px;

    }}

    .result-title {{

        font-size: 18px;

    }}

    .nav-right {{

        display: none;

    }}

}}


/* =========================================================
   MOBILE SIDEBAR
========================================================= */

@media (max-width: 700px) {{

    section[data-testid="stSidebar"] {{

        width: 280px !important;

        min-width: 280px !important;

    }}

    .block-container {{

        padding-left: .8rem;

        padding-right: .8rem;

    }}

    .hero-title {{

        font-size: 32px;

        letter-spacing: -1px;

    }}

    .result-card {{

        padding: 18px;

    }}

    .result-header {{

        gap: 10px;

    }}

}}


/* =========================================================
   DARK MODE EXTRA POLISH
========================================================= */

body {{

    transition:
        background-color .25s ease,
        color .25s ease;

}}

</style>
""",
        unsafe_allow_html=True,
    )