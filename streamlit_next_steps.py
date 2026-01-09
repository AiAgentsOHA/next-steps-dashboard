"""
OceanHub OH7 Next Steps Action Board - Streamlit Dashboard
Embeds the validated pipeline outreach dashboard with Gmail integration.

Run with: streamlit run streamlit_next_steps.py
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="OceanHub OH7 | Next Steps",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit UI elements for clean presentation
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp > header {display: none;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    [data-testid="stToolbar"] {display: none;}
    [data-testid="stDecoration"] {display: none;}
    .stApp {background: #030712;}
    iframe {border: none !important;}
</style>
""", unsafe_allow_html=True)

# Read the HTML file
try:
    with open('oceanhub_next_steps.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
except FileNotFoundError:
    # Fallback: try alternate path
    try:
        with open('/home/claude/oceanhub_next_steps.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        html_content = """
        <html>
        <body style="background:#030712;color:#fff;font-family:sans-serif;padding:40px;text-align:center;">
        <h1>⚠️ Dashboard HTML not found</h1>
        <p>Please ensure oceanhub_next_steps.html is in the same directory as this script.</p>
        </body>
        </html>
        """

# Render the HTML dashboard
components.html(html_content, height=2000, scrolling=True)
