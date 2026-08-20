import streamlit as st
import pandas as pd
from pathlib import Path
import parts
import functions
import config

def month():
    base_folder = st.session_state[config.folder_key]

    files = base_folder.glob("*")
    # pages = []

    if not base_folder.exists():
        st.info(
            "The base folder does not exist."
        )

        st.stop()

    # for subfolder in sorted(base_folder.iterdir()):
    #     if subfolder.is_dir():

    #         pages.append(subfolder)

    folder = Path(f"{base_folder}/2026")
    files = folder.glob("*.xlsx")
    stats: list[str] = []

    for file in files:
        stats.append(file.name)


    if len(stats) < 1:
        st.info(
            "The folder needs at least one Excel file to start the analysis."
        )

        st.stop()


    if config.tab_key not in st.session_state:
        st.session_state[config.tab_key] = stats[5]


    st.tabs(stats, key=config.tab_key, on_change="rerun", default=stats[5])


    # ---------------------------------------------------------
    # READ EXCEL FILE
    # ---------------------------------------------------------

    try:
        file_name = st.session_state[config.tab_key]
        current_file = Path(f"{folder}/{file_name}")

        excel_data = pd.ExcelFile(
            current_file,
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

    st.sidebar.header("Year")

    sheet_name = st.sidebar.selectbox(
        "Worksheet",
        excel_data.sheet_names
    )


    data = config.setConfig(current_file, sheet_name)
    kpis = parts.kpisView(data)

    parts.tableView(data)
    parts.quantityView(data)
    parts.trendView(data)
    parts.variationView(data)
    parts.insightsView(data, kpis)


    # ---------------------------------------------------------
    # DOWNLOAD
    # ---------------------------------------------------------

    st.subheader("⬇️ Export")

    excel_output = functions.create_excel(data)

    st.download_button(
        label="📥 Download analyzed Excel",
        data=excel_output,
        file_name="spreadsheet_analysis.xlsx",
        mime=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        )
    )
