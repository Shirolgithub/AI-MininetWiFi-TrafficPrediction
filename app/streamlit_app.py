import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

DATASET = "data/mobile_network_traffic.csv"

st.title("AI-Driven Traffic Prediction Dashboard")

st.subheader("Mobile Network Traffic Analysis")

try:

    df = pd.read_csv(DATASET)

    st.write("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Traffic Load Trend")

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df["Traffic_Load_Mbps"])

    ax.set_xlabel("Samples")

    ax.set_ylabel("Traffic Load (Mbps)")

    ax.set_title("Traffic Trend")

    st.pyplot(fig)

    st.subheader("Network Statistics")

    avg_traffic = df["Traffic_Load_Mbps"].mean()

    max_traffic = df["Traffic_Load_Mbps"].max()

    avg_latency = df["Latency_ms"].mean()

    st.metric(
        "Average Traffic Load",
        f"{avg_traffic:.2f} Mbps"
    )

    st.metric(
        "Maximum Traffic Load",
        f"{max_traffic:.2f} Mbps"
    )

    st.metric(
        "Average Latency",
        f"{avg_latency:.2f} ms"
    )

    st.subheader("Congestion Alert")

    if max_traffic > 80:

        st.error("High Network Congestion Detected!")

    else:

        st.success("Network Operating Normally")

except Exception as e:

    st.error(f"Error Loading Dataset: {e}")
