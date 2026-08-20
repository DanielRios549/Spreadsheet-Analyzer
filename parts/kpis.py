import streamlit as st

def kpisView(data):
    # ---------------------------------------------------------
    # KPI CALCULATIONS
    # ---------------------------------------------------------

    total = data["Quantidade"].sum()
    average = data["Quantidade"].mean()

    maximum = data["Quantidade"].max()
    minimum = data["Quantidade"].min()

    max_month = data.loc[
        data["Quantidade"].idxmax(),
        "Mês"
    ]

    min_month = data.loc[
        data["Quantidade"].idxmin(),
        "Mês"
    ]

    first_value = data.iloc[0]["Quantidade"]
    last_value = data.iloc[-1]["Quantidade"]

    overall_growth = (
        (last_value / first_value) - 1
    ) * 100 if first_value != 0 else 0


    # ---------------------------------------------------------
    # DASHBOARD KPIs
    # ---------------------------------------------------------

    st.subheader("📌 Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Total",
        f"{total:,.0f}"
    )

    col2.metric(
        "Monthly Average",
        f"{average:,.0f}"
    )

    col3.metric(
        "Highest",
        f"{maximum:,.0f}",
        max_month
    )

    col4.metric(
        "Lowest",
        f"{minimum:,.0f}",
        min_month
    )

    col5.metric(
        "Overall Growth",
        f"{overall_growth:.2f}%"
    )

    return {
        "min_month": min_month,
        "max_month": max_month,
        "minimum": minimum,
        "maximum": maximum
    }
