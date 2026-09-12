import streamlit as st
import pandas as pd
import os

st.title("AI Crime Detection Dashboard")

if os.path.exists("intrusion_log.csv"):

    df = pd.read_csv("intrusion_log.csv")

    st.subheader("Intrusion Logs")

    st.dataframe(df)

    st.metric(
        "Total Intrusions",
        len(df)
    )

    st.metric(
        "Unique Persons",
        df["Person_ID"].nunique()
    )

else:
    st.warning(
        "No intrusion data available."
    )