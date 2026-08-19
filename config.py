import streamlit as st
import pandas as pd
from functions.data import prepare_data
from functions.month import detect_month_column, detect_quantity_column
from functions.helpers import normalize_columns

def setConfig(uploaded_file, sheet_name):
    # ---------------------------------------------------------
    # LOAD SELECTED SHEET
    # ---------------------------------------------------------

    try:
        df = pd.read_excel(
            uploaded_file,
            sheet_name=sheet_name,
            engine="openpyxl"
        )

    except Exception as e:

        st.error(
            f"Error reading worksheet: {e}"
        )

        st.stop()


    df = normalize_columns(df)


    # ---------------------------------------------------------
    # COLUMN DETECTION
    # ---------------------------------------------------------

    detected_month = detect_month_column(df)
    detected_quantity = detect_quantity_column(df)

    st.sidebar.subheader("Columns")

    month_column = st.sidebar.selectbox(
        "Month column",
        df.columns,
        index=(
            list(df.columns).index(detected_month)
            if detected_month in df.columns
            else 0
        )
    )

    quantity_column = st.sidebar.selectbox(
        "Quantity column",
        df.columns,
        index=(
            list(df.columns).index(detected_quantity)
            if detected_quantity in df.columns
            else 0
        )
    )

    # ---------------------------------------------------------
    # PREPARE DATA
    # ---------------------------------------------------------

    data = prepare_data(
        df,
        month_column,
        quantity_column
    )


    if data.empty:
        st.error(
            "No valid month/quantity data was found. "
            "Check the selected columns."
        )

        st.stop()

    return data
