import streamlit as st
from pathlib import Path
# from openpyxl import load_workbook
import config
import views


# ---------------------------------------------------------
# Spreadsheet Analyzer
# ---------------------------------------------------------

title = "Spreadsheet Analyzer"

st.set_page_config(
    page_title=title,
    page_icon="📊",
    layout="wide"
)

st.title(f"📊 {title}")
st.markdown(
    "Upload an Excel spreadsheet and analyze quantities, monthly trends "
    "and variations."
)

base_folder = Path("data") # TODO: Add Env Var

if config.folder_key not in st.session_state:
    st.session_state[config.folder_key] = base_folder

pages = [
    st.Page(views.month, title="Month"),
    st.Page(views.year, title="Year")
]

nav = st.navigation(
    pages,
    position="top",
    expanded=False
)

nav.run()
