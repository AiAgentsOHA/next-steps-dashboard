"""
OceanHub OH7 Next Steps Action Board - Streamlit Dashboard
Run: streamlit run streamlit_next_steps.py
"""
import streamlit as st
import streamlit.components.v1 as components
import os

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

# Find HTML file
html_paths = [
    'oceanhub_next_steps_complete.html',
    '/home/claude/oceanhub_next_steps_complete.html',
    '/mnt/user-data/outputs/oceanhub_next_steps_complete.html'
]

html_content = None
for p in html_paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            html_content = f.read()
        break

if html_content:
    components.html(html_content, height=2500, scrolling=True)
else:
    st.error("Dashboard HTML not found. Place oceanhub_next_steps_complete.html in the same directory.")
