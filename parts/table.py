import streamlit as st
import pandas as pd

def tableView(data):
    # ---------------------------------------------------------
    # DATA TABLE
    # ---------------------------------------------------------

    st.subheader("📋 Monthly Data")

    display_data = data.copy()

    display_data["Quantidade"] = display_data[
        "Quantidade"
    ].map(lambda x: f"{x:,.0f}")

    display_data["Variação"] = display_data[
        "Variação"
    ].map(
        lambda x:
        f"{x:.2f}%"
        if pd.notna(x)
        else "-"
    )

    st.dataframe(
        display_data[
            ["Mês", "Quantidade", "Variação"]
        ],
        width='stretch',
        hide_index=True
    )
