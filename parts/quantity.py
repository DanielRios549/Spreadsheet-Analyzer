import streamlit as st
import plotly.express as px

def quantityView(data):
    # ---------------------------------------------------------
    # CHART 1 - QUANTITY BY MONTH
    # ---------------------------------------------------------

    st.subheader("📊 Quantity by Month")

    fig = px.bar(
        data,
        x="Mês",
        y="Quantidade",
        text="Quantidade",
        title="Monthly Quantity",
        color="Quantidade",
        color_continuous_scale="Blues"
    )

    fig.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Quantity",
        showlegend=False
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )
