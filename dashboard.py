import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    h1, h2, h3 {
        color: #FAFAFA;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Weather Analytics Dashboard")

conn = sqlite3.connect("data/weather.db")
df = pd.read_sql("SELECT * FROM weather", conn)

if df.empty:
    st.warning("Run the ETL pipeline first.")
else:
    df["time"] = pd.to_datetime(df["time"])

    st.sidebar.title("Filters")

    cities = sorted(df["city"].unique())
    selected_cities = st.sidebar.multiselect(
        "Cities",
        cities,
        default=cities[:5]  
    )

    filtered_df = df[df["city"].isin(selected_cities)]

    latest = filtered_df.sort_values("time").groupby("city").tail(1)

    st.subheader("Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Cities", len(selected_cities))
    col2.metric("Avg Temp (°C)", f"{latest['temperature'].mean():.1f}")
    col3.metric("Max Wind", f"{latest['windspeed'].max():.1f}")

    st.subheader("Temperature Trend")

    pivot_temp = filtered_df.pivot_table(
        index="time",
        columns="city",
        values="temperature"
    )

    st.line_chart(pivot_temp, height=300)

    st.subheader("Wind Speed Trend")

    pivot_wind = filtered_df.pivot_table(
        index="time",
        columns="city",
        values="windspeed"
    )

    st.line_chart(pivot_wind, height=300)

    st.subheader("Top Hottest Cities")

    ranking = latest.sort_values("temperature", ascending=False)

    st.dataframe(
        ranking[["city", "temperature", "windspeed"]],
        use_container_width=True
    )