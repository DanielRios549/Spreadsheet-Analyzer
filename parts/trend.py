import streamlit as st
import plotly.express as px

def trendView(data):
    st.subheader("📈 Trend")

    fig_trend = px.line(
        data,
        x="Mês",
        y="Quantidade",
        markers=True,
        title="Quantity Trend"
    )

    fig_trend.update_traces(
        line=dict(
            width=4,
            color="#1f77b4"
        ),
        marker=dict(
            size=10
        )
    )

    st.plotly_chart(
        fig_trend,
        width=True
    )
