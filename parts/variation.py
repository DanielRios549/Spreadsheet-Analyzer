import streamlit as st
import plotly.express as px

def variationView(data):
    variation_data = data.dropna(
        subset=["Variação"]
    ).copy()

    variation_data["Cor"] = variation_data[
        "Variação"
    ].apply(
        lambda x: "Increase"
        if x >= 0
        else "Decrease"
    )

    st.subheader("📉 Month-over-Month Variation")

    fig_variation = px.bar(
        variation_data,
        x="Mês",
        y="Variação",
        color="Cor",
        text="Variação",
        color_discrete_map={
            "Increase": "#2ca02c",
            "Decrease": "#d62728"
        }
    )

    fig_variation.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )

    fig_variation.update_layout(
        yaxis_title="Variation (%)",
        xaxis_title="Month"
    )

    st.plotly_chart(
        fig_variation,
        width=True
    )
