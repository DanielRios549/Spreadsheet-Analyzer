import streamlit as st

def insightsView(data, kpis: dict):
    st.subheader("💡 Automatic Insights")

    largest_increase = data.loc[
        data["Variação"].idxmax()
    ]

    largest_decrease = data.loc[
        data["Variação"].idxmin()
    ]
    print(kpis)

    st.write(
        f"🔹 **Highest quantity:** "
        f"{kpis.get('max_month')} ({kpis.get('maximum'):,.0f})"
    )

    st.write(
        f"🔹 **Lowest quantity:** "
        f"{kpis.get('min_month')} ({kpis.get('minimum'):,.0f})"
    )

    st.write(
        f"🔹 **Largest monthly increase:** "
        f"{largest_increase['Mês']} "
        f"({largest_increase['Variação']:.1f}%)"
    )

    st.write(
        f"🔹 **Largest monthly decrease:** "
        f"{largest_decrease['Mês']} "
        f"({largest_decrease['Variação']:.1f}%)"
    )