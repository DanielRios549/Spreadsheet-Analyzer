import streamlit as st
import pandas as pd
# from openpyxl import load_workbook
from functions.data import create_excel
from config import setConfig
from parts import kpisView, quantityView, dataView, insightsView, variationView, trendView

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Spreadsheet Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Spreadsheet Analyzer")
st.markdown(
    "Upload an Excel spreadsheet and analyze quantities, monthly trends "
    "and variations."
)

# ---------------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------------

uploaded_file = st.file_uploader(
    "📁 Upload your Excel file",
    type=["xlsx", "xlsm"]
)

if uploaded_file is None:

    st.info(
        "Upload an Excel spreadsheet to start the analysis."
    )

    st.markdown("""
### Example

Your spreadsheet can look like:

| Mês | Quantidade |
|---|---:|
| Janeiro | 5.943 |
| Fevereiro | 6.459 |
| Março | 8.230 |
| Abril | 8.300 |
| Maio | 8.200 |
| Junho | 9.354 |
| Julho | 7.880 |
| Agosto | |
| Setembro | |
""")

    st.stop()


# ---------------------------------------------------------
# READ EXCEL
# ---------------------------------------------------------

try:
    excel_data = pd.ExcelFile(
        uploaded_file,
        engine="openpyxl"
    )

except Exception as e:

    st.error(
        f"Could not read the Excel file: {e}"
    )

    st.stop()


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.header("⚙️ Configuration")

sheet_name = st.sidebar.selectbox(
    "Worksheet",
    excel_data.sheet_names
)

data = setConfig(uploaded_file, sheet_name)
kpis = kpisView(data)

dataView(data)
quantityView(data)
trendView(data)
variationView(data)
insightsView(data, kpis)


# ---------------------------------------------------------
# DOWNLOAD
# ---------------------------------------------------------

st.subheader("⬇️ Export")

excel_output = create_excel(data)

st.download_button(
    label="📥 Download analyzed Excel",
    data=excel_output,
    file_name="spreadsheet_analysis.xlsx",
    mime=(
        "application/vnd.openxmlformats-officedocument."
        "spreadsheetml.sheet"
    )
)
